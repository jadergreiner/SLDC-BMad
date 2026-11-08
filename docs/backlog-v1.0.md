# Backlog técnico v1.0

**Estado:** planejamento; nenhuma história implementada por esta aprovação.
**Baseline:** PRD v0.2, ADR-001 a ADR-009, C-01 a C-08.

## Épicos, histórias e dependências
- EP-01 Fundação: US-001 estrutura; US-002 contratos; US-003 compatibilidade BMad; US-004 testes isolados.
- EP-02 Persistência: US-005 modelo PostgreSQL; US-006 máquina de estados; US-007 leases/fencing; US-008 idempotência/auditoria. Depende EP-01.
- EP-03 Segurança: US-009 PEP; US-010 aprovações escopadas; US-011 revogação/expiração; US-012 proteção contra prompt injection. Depende contratos e identidade.
- EP-04 Orquestração: US-013 workflows; US-014 seleção de agentes; US-015 deliberações; US-016 recuperação de execução. Depende EP-02 e EP-03.
- EP-05 BMad Runner: US-017 adaptador oficial; US-018 isolamento; US-019 workflow real; US-020 evidências. Depende EP-01, EP-03 e EP-04.
- EP-06 GitHub: US-021 autenticação; US-022 branch/commit/PR; US-023 verificação e resposta perdida. Depende EP-03 e EP-02.
- EP-07 Notion/Drive: US-024 Notion; US-025 Drive; US-026 sincronização/reconciliação. Depende contratos e autorização.
- EP-08 Memória: US-027 índice contextual; US-028 proveniência; US-029 invalidação/rastreabilidade. Depende persistência.
- EP-09 Operação: US-030 risco/DoD; US-031 observabilidade; US-032 quotas. Integração incremental.
- EP-10 Homologação: US-033 AT-01–18; US-034 testes adversariais; US-035 dossiê e aprovação de release. Depende integração dos épicos anteriores.

## Gates
- **G0 Design Ready:** contratos, baseline e revisão de segurança.
- **G1 Core Secure:** estado durável, políticas e testes negativos.
- **G2 Vertical Slice:** BMad real + branch/PR autorizado + evidências.
- **G3 Data Integrity:** Notion/Drive, falhas parciais e proveniência.
- **G4 Operational Readiness:** riscos, logs, quotas e resposta a falhas.
- **G5 Release Approval:** 18 cenários com evidências, riscos residuais aceitos e liberação humana.

## Primeiro lote
US-001, US-002, US-003 e US-004. Não altera plugin nem provisiona recursos sem autorização específica.
