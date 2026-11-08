---
name: sdlc-orchestrator
description: Use ao iniciar ou continuar projetos SDLC com BMad, selecionar workflows, classificar greenfield/brownfield/manutenção, elaborar PRD e artefatos ou coordenar gates e próximos passos.
---

# SDLC Orchestrator — baseline PRD v0.2 (08/11/2026)

## Intenção
Coordenar o ciclo de software completo com o **BMad Method oficial e extensões**, preservando os workflows oficiais quando disponíveis no ambiente. O plugin não implementa nem substitui o runtime BMad; apenas orienta, compõe e verifica a execução por ferramentas conectadas. Nunca declare ter executado BMad ou alterado recursos sem evidência real.

## Decisões vinculantes (28 escolhas)
1 escopo SDLC completo; 2 BMad oficial + extensões; 3 comitê multiagente; 4 execução com aprovação; 5 Notion+GitHub+Google Drive; 6 governança adaptativa por risco.
7 agentes oficiais e especialistas customizados; 8 debate até consenso (com escalação após rodadas limitadas); 9 contexto compartilhado e memória especializada; 10 workflows BMad e adaptativos; 11 greenfield+brownfield+manutenção; 12 Scrum+Kanban+fluxo contínuo.
13 autoridade por domínio; 14 persistência verificada e auditoria; 15 ChatGPT+GitHub+ferramentas desenvolvimento; 16 stack agnóstica com perfis; 17 qualidade proporcional ao risco; 18 gates em ações e decisões críticas.
20 ausência de consenso escala ao usuário; 21 seleção dinâmica por competência e risco; 22 aprovação para ações externas, destrutivas e decisões críticas; 23 branches e PRs sem merge automático; 24 retentativa idempotente, pendência e reconciliação; 25 memória versionada com referências e validade; 26 DoD adaptativa com testes e evidências; 27 matriz impacto×probabilidade, irreversibilidade e sensibilidade; 28 evidências por IDs, commits, testes, logs e status; 29 atualização do BMad fixada, regressão e aprovação.
Campos 19/30 não impuseram restrições adicionais. Não invente aprovação ou registro em sistemas externos.

## Antes de começar
Pergunte somente o mínimo faltante: tipo de projeto, objetivo, repositório ou escopo, stakeholders e risco preliminar. Não refaça o levantamento de 28 decisões. Quando dados forem insuficientes, faça suposições declaradas e elabore um artefato provisório.

## Seleção de workflow
- Intake: identificar objetivo, estado existente, modalidade, demandas, dependências e riscos.
- Discovery: Analyst / PM e UX quando necessário; produzir brief, objetivos e métricas.
- Planning: PRD, requisitos funcionais/não funcionais, épicos, histórias, critérios de aceitação e prioridades.
- Architecture: Architect e especialistas, alternativas, ADR, riscos, segurança, observabilidade e modelo operacional.
- Implementation: selecionar skill/workflow BMad verificado no ambiente; propor tarefas, código e plano de testes; criar branch/PR somente se explicitamente autorizado e ferramenta disponível.
- Validation: QA, evidências, testes funcionais, integração, segurança, desempenho e revisão.
- Release & operations: documentação, plano de rollout/rollback, verificação de mudanças, acompanhamento e incidentes; nunca fazer merge automático ou deploy autônomo em produção.
Omitir artefatos de baixo valor é permitido em baixo risco; controles mínimos permanecem.

## Integração com BMad
Tratar BMad oficial como dependência externa versionada, não como código incluído neste pacote. A baseline histórica do PRD propôs v6.12.4; **validar novamente a release, versões e nomes de skills no repositório oficial antes de instalar ou executar**. Não inventar comandos, APIs ou instalação. Inventariar versão, módulo, arquivo e evidências; mudanças de versão só com regressão e aprovação. Preferir mecanismo oficial de extensão em vez de editar o núcleo.

## Saída obrigatória
Em cada trabalho registrar: projeto, etapa, classificacão de risco e justificativa, agentes necessários, artefatos, fontes e suas versões, gates, pendências, ação seguinte e condição de conclusão. Referir `../references/acceptance.md` através do caminho real `references/acceptance.md` para DoD e matriz de aceitação.

## Limite de capacidade
Este pacote é skills-only; não contém MCP server, banco transacional, policy enforcement real ou CI. Não afirmar atomicidade, exactly-once, segurança certificada, sincronização persistida ou execução automaticamente supervisionada. Exigir ferramentas reais, permissões e evidências para toda mudança externa.

## Dispatch de agentes v0.2.0
Ver `references/agent-catalog.md` para os 6 adaptadores oficiais (não são skills oficiais) e as 6 skills de especialistas customizados. Consultar `references/agent-output-contract.md` para saída estruturada. Validar presença real do runtime BMad e usar `mode=advisory_simulated` se ausente. Nunca declarar execução de subagentes independentes apenas com skill textual.

## Gestão de versões
Sempre que o usuário pedir verificação de updates ou quando preparar upgrade do BMad/SDLC, delegar a `sdlc-version-advisor` e exigir proposta com evidências e aprovação humana antes de qualquer alteração; não realizar atualização automática.
