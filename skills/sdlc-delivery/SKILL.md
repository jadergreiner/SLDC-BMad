---
name: sdlc-delivery
description: Use para decompor PRDs em épicos e histórias, planejar Scrum/Kanban, preparar branches, PRs, CI, testes, rollout e entregas supervisionadas conforme BMad.
---

# Delivery controlado

## Seleção ágil
Permitir Scrum, Kanban ou fluxo contínuo conforme o projeto. Priorizar pequenas unidades entregáveis e critérios testáveis. Cada história: objetivo, contexto, dependências, critérios Gherkin quando adequado, testes e link ao requisito/ADR.

## GitHub
Sem merge automático. Apenas criar branch, commit, issue ou PR quando o usuário autorizou explicitamente a ação e o recurso e uma ferramenta realmente permitir a execução. Antes de escrever, confirmar repo, base branch, paths e plano; evitar segredos e operações destrutivas. Depois, reler commit/PR/issue pelo ID retornado e distinguir preparado de realizado.

## CI e rollout
Recomendar lint, testes unitários, integração, contratos, segurança, rollback e monitoramento de acordo com risco. Execução de CI externa requer aprovação específica quando não coberta por autorização. Produção autônoma bloqueada nesta versão.

## DoD
Critérios de aceite satisfeitos; testes e artefatos acessíveis; link de requisito -> ADR -> branch/PR -> teste -> release; gates válidos; bloqueios críticos resolvidos. Não inferir que testes passaram sem logs ou status reais.

## Evidência por artefato
IDs imutáveis quando disponíveis, URL real (não inventada), versão/hash, status e momento. Para ferramentas indisponíveis criar somente planos ou textos locais, nunca alegar persistência externa.
