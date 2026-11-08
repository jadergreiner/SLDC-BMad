---
name: bmad-committee
description: Use para convocar um comitê multiagente BMad, revisar PRD, arquitetura, ADR ou decisões críticas, promover contestação técnica e registrar consenso ou divergências.
---

# Comitê BMad com especialistas

## Composição
Preservar agentes oficiais da versão BMad disponível. Papéis lógicos comuns: Analyst, PM, PO, Architect, Developer, UX. Não alegar que são processos isolados se estiver apenas simulando suas perspectivas no modelo atual. Convocar especialistas customizados conforme necessidade: Data Architect, Cloud Architect, Security Engineer, QA/Test Architect (preferir módulo oficial disponível), SRE/DevOps, Business Risk Analyst. Mediador organiza processo e **não inventa unanimidade**.

## Debate
- R0: posições independentes, com hipótese, trade-offs, riscos, evidência, confiança qualitativa e objeções.
- R1: contestação cruzada com identificação de incoerência e riscos residuais.
- R2: revisão, convergência ou dissenso, decisão proposta e critérios de verificação.
- Se persistir discordância material após três rodadas, **ESCALAR ao usuário**. O limite encerra a discussão, nunca força consenso. Solicitação humana pode convocar novas rodadas.
- Consenso não autoriza escrita externa, merge, deploy, operações destrutivas ou acesso ampliado.

## Formato
Título, projeto, assunto, agentes (papel e competência), evidências e fontes, R0/R1/R2, matriz de objeções, decisões consensuais, dissensos, owner e plano de verificação. Distinguir fatos extraídos de fontes, hipóteses e conclusões inferidas. Preservar histórico e alternativas rejeitadas em ADR quando apropriado.

## Impedimento
Não afirmar reunião real de agentes independentes quando a ferramenta não foi chamada. Escrever 'revisão por perspectivas especializadas simuladas' se essas perspectivas tiverem sido produzidas por uma única execução. Sempre validar riscos que dependam de informação externa recente.

## Catálogo v0.2.0 e despacho
Para parecer específico, selecionar individualmente skills `specialist-data-architect`, `specialist-cloud-architect`, `specialist-security-engineer`, `specialist-qa-test-architect`, `specialist-sre-devops` e/ou `specialist-business-risk-analyst`. Para papeis BMad oficiais, usar os seis adaptadores `bmad-*-adapter`, jamais assumir que esses arquivos são o runtime oficial. Consultar `references/agent-catalog.md` e `references/agent-output-contract.md`. Identificar explicitamente modo real verificado ou perspectivas simuladas. Preservar R0, R1, R2, dissenso e bloqueios críticos.
