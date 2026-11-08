import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from check_versions import compare, level, check

class VersionAdvisorTests(unittest.TestCase):
    def test_semver(self):
        self.assertLess(compare("0.2.0", "0.3.0"),0)
        self.assertEqual(compare("1.2.3+build1","v1.2.3+build2"),0)
        self.assertLess(compare("1.0.0-rc.2", "1.0.0"),0)
        self.assertLess(compare("1.0.0-rc.2", "1.0.0-rc.10"),0)
        self.assertEqual(level("0.2.0","0.3.0"),"minor")
        self.assertEqual(level("6.12.4","7.0.0"),"major")
    def test_upgrade_proposal_no_changes(self):
        with tempfile.TemporaryDirectory() as d:
            f=Path(d)/"plugin.json"; f.write_text(json.dumps({"name":"sdlc-bmad","version":"0.2.0"}))
            result=check(f,"6.12.4",fetch_manifest=lambda repo,ref:({"name":"sdlc-bmad","version":"0.3.0"},"abc"),fetch_release=lambda repo:{"tag_name":"v7.0.0","draft":False,"prerelease":False})
            self.assertTrue(all(x["status"]=="update_available" for x in result["findings"]))
            self.assertTrue(all(not x["auto_update"] for x in result["findings"]))
            self.assertFalse(result["updates_applied"])
    def test_failure_is_unknown(self):
        with tempfile.TemporaryDirectory() as d:
            f=Path(d)/"plugin.json"; f.write_text(json.dumps({"name":"sdlc-bmad","version":"0.2.0"}))
            def fail(*args): raise OSError("offline")
            result=check(f,fetch_manifest=fail,fetch_release=fail)
            self.assertEqual(len(result["errors"]),2)
            self.assertTrue(all(x["status"]=="unknown" for x in result["findings"]))
    def test_upstream_identity_mismatch(self):
        with tempfile.TemporaryDirectory() as d:
            f=Path(d)/"plugin.json"; f.write_text(json.dumps({"name":"sdlc-bmad","version":"0.2.0"}))
            result=check(f,fetch_manifest=lambda a,b:({"name":"other","version":"9.9.9"},"bad"),fetch_release=lambda a:{"tag_name":"v6.12.4","draft":False,"prerelease":False})
            self.assertEqual(result["findings"][0]["status"],"unknown")

if __name__=="__main__": unittest.main()
