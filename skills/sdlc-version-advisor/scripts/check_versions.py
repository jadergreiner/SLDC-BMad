#!/usr/bin/env python3
"""Read-only SDLC/BMad version advisor. Uses Python standard library only.

Never installs dependencies, checks out code, or changes the workspace.
"""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

VERSION = re.compile(r"^v?(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-([0-9A-Za-z.-]+))?(?:\+[0-9A-Za-z.-]+)?$")
REPO = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
DEFAULT_SDL_REPO = "jadergreiner/SLDC-BMad"
DEFAULT_BMAD_REPO = "bmad-code-org/BMAD-METHOD"


def parse_version(value):
    if not isinstance(value, str):
        raise ValueError("version must be a string")
    match = VERSION.fullmatch(value.strip())
    if not match:
        raise ValueError(f"invalid semantic version: {value!r}")
    major, minor, patch, prerelease = match.groups()
    return (int(major), int(minor), int(patch), prerelease)


def compare(current, candidate):
    """SemVer comparison with prerelease ordering (build metadata ignored)."""
    a, b = parse_version(current), parse_version(candidate)
    if a[:3] != b[:3]:
        return (a[:3] > b[:3]) - (a[:3] < b[:3])
    if a[3] is None or b[3] is None:
        return (a[3] is None) - (b[3] is None)
    def ids(s):
        return s.split('.')
    for x, y in zip(ids(a[3]), ids(b[3])):
        if x == y:
            continue
        xn, yn = x.isdigit(), y.isdigit()
        if xn and yn:
            return (int(x)>int(y))-(int(x)<int(y))
        if xn != yn:
            return -1 if xn else 1
        return (x>y)-(x<y)
    return (len(ids(a[3]))>len(ids(b[3])))-(len(ids(a[3]))<len(ids(b[3])))


def level(current, target):
    a, b = parse_version(current), parse_version(target)
    if compare(target, current) <= 0:
        return "none"
    if b[0] != a[0]:
        return "major"
    if b[1] != a[1]:
        return "minor"
    if b[2] != a[2]:
        return "patch"
    return "prerelease"


def get_json(url, token=None):
    if not url.startswith("https://api.github.com/"):
        raise ValueError("Only GitHub official API allowed")
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "sdlc-version-advisor/1.0", "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = "Bearer " + token
    req = Request(url, headers=headers)
    with urlopen(req, timeout=10) as response:
        return json.load(response)


def valid_repo(name):
    if not REPO.fullmatch(name):
        raise ValueError("Repository must use owner/name format")
    return name


def source_release(repo, token=None):
    """Stable release only; do not consider previews as official upgrade recommendations."""
    valid_repo(repo)
    return get_json(f"https://api.github.com/repos/{repo}/releases/latest", token)


def source_manifest(repo, ref="main", token=None):
    valid_repo(repo)
    if not re.fullmatch(r"[A-Za-z0-9_.\-/]+", ref) or ".." in ref:
        raise ValueError("Invalid ref")
    data = get_json(f"https://api.github.com/repos/{repo}/contents/plugin.json?ref={ref}", token)
    import base64
    if data.get("encoding") != "base64":
        raise ValueError("Unexpected GitHub contents encoding")
    raw = base64.b64decode(data["content"])
    return json.loads(raw.decode("utf-8")), data.get("sha")


def check_item(name, current, upstream, source_url, evidence, target_kind):
    status = "unknown"
    change = "none"
    decision = "investigate"
    note = "Unable to classify."
    if current is None:
        note = "Local version was not supplied; do not infer the installed version."
    elif upstream is None:
        note = "Upstream version was not verifiable. Do not claim current or outdated."
    else:
        order = compare(current, upstream)
        status = "update_available" if order < 0 else "current" if order == 0 else "local_ahead"
        change = level(current, upstream)
        if order < 0:
            decision = "manual_review_required"
            note = ("Major upgrade: require architecture and regression review." if change == "major"
                else "Review changelog, compatibility, security and smoke/regression tests before approval.")
        elif order == 0:
            decision, note = "no_change", "Versions match; content/commit drift still requires a separate integrity check."
        else:
            decision, note = "investigate", "Local version newer than source; check branch, release policy or unpublished changes."
    return {"component":name,"installed_version":current,"upstream_version":upstream,"status":status,
            "change_level":change,"recommendation":decision,"notes":note,"source":source_url,"evidence":evidence,
            "target_kind":target_kind,"auto_update":False}


def check(manifest, bmad_version=None, sdlc_repo=DEFAULT_SDL_REPO, bmad_repo=DEFAULT_BMAD_REPO, ref="main", fetch_manifest=source_manifest, fetch_release=source_release):
    local = json.loads(Path(manifest).read_text(encoding="utf-8"))
    if local.get("name") != "sdlc-bmad":
        raise ValueError("Expected the SDLC plugin manifest (name=sdlc-bmad)")
    local_version = local.get("version")
    parse_version(local_version)
    if bmad_version:
        parse_version(bmad_version)
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    outcomes = []
    errors = []
    try:
        remote, sha = fetch_manifest(sdlc_repo, ref)
        if remote.get("name") != local["name"]:
            raise ValueError("Upstream package identity mismatch")
        up = remote["version"]
        parse_version(up)
        outcomes.append(check_item("sdlc-bmad",local_version,up,f"https://github.com/{sdlc_repo}/blob/{ref}/plugin.json",{"manifest_blob_sha":sha,"checked_at":now},"source_manifest"))
    except (ValueError, KeyError, OSError, URLError, HTTPError, json.JSONDecodeError) as exc:
        errors.append({"component":"sdlc-bmad","error":type(exc).__name__,"message":str(exc)[:300]})
        outcomes.append(check_item("sdlc-bmad",local_version,None,f"https://github.com/{sdlc_repo}",{"checked_at":now},"source_manifest"))
    try:
        release = fetch_release(bmad_repo)
        if release.get("draft") or release.get("prerelease"):
            raise ValueError("Non-stable release returned by latest endpoint")
        up = release["tag_name"]
        parse_version(up)
        outcomes.append(check_item("bmad-method",bmad_version,up,release.get("html_url",f"https://github.com/{bmad_repo}/releases"),{"tag":up,"published_at":release.get("published_at"),"checked_at":now},"stable_release"))
    except (ValueError, KeyError, OSError, URLError, HTTPError, json.JSONDecodeError) as exc:
        errors.append({"component":"bmad-method","error":type(exc).__name__,"message":str(exc)[:300]})
        outcomes.append(check_item("bmad-method",bmad_version,None,f"https://github.com/{bmad_repo}/releases",{"checked_at":now},"stable_release"))
    return {"schema_version":"1.0.0", "checked_at":now,"mode":"read_only","updates_applied":False,
            "findings":outcomes,"errors":errors,"gate":"human_approval_required_before_any_upgrade",
            "required_before_upgrade":["verify release notes and source provenance","validate compatibility with plugin skills and official BMad workflows","test security and regressions","produce plan and diff","obtain explicit human approval"]}


def main(argv=None):
    parser=argparse.ArgumentParser(description="Read-only SDLC+BMad upstream version comparison; never updates anything")
    parser.add_argument("--manifest",default="plugin.json",help="Path to locally installed plugin manifest")
    parser.add_argument("--bmad-version",default=None,help="Verified locally installed BMad version; leave absent if unknown")
    parser.add_argument("--sdlc-repo",default=DEFAULT_SDL_REPO)
    parser.add_argument("--bmad-repo",default=DEFAULT_BMAD_REPO)
    parser.add_argument("--sdlc-ref",default="main")
    parser.add_argument("--output",choices=["json","text"],default="text")
    args=parser.parse_args(argv)
    try:
        valid_repo(args.sdlc_repo);valid_repo(args.bmad_repo)
        result=check(args.manifest,args.bmad_version,args.sdlc_repo,args.bmad_repo,args.sdlc_ref)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"Input error: {exc}",file=sys.stderr)
        return 2
    if args.output=="json":
        print(json.dumps(result,ensure_ascii=False,indent=2))
    else:
        print("SDLC+BMad version advisor (READ ONLY) —",result["checked_at"])
        for item in result["findings"]:
            print(f"- {item['component']}: local={item['installed_version'] or 'unknown'}, upstream={item['upstream_version'] or 'unknown'}, status={item['status']}, change={item['change_level']}")
            print(f"  Recommendation: {item['recommendation']}. {item['notes']} Source: {item['source']}")
        if result["errors"]:
            print("Some sources could not be checked; do not infer update status.")
        print("No updates applied. Human approval is mandatory for any upgrade.")
    return 0 if not result["errors"] else 1

if __name__=="__main__":
    raise SystemExit(main())
