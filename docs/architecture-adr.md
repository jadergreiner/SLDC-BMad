# Architecture Design Review — ADRs 001–009

**Estado:** aprovados como baseline para planejamento detalhado; não provisionar recursos.

| ADR | Decisão |
|---|---|
| 001 | PostgreSQL como autoridade transacional, gerenciado; Aurora PostgreSQL como opção AWS |
| 002 | Policy Enforcement Point (PEP) externo aos agentes e políticas de escopo mínimo |
| 003 | Máquina de estados durável; processamento assíncrono, conciliação e exceções explícitas |
| 004 | BMad oficial com versão fixada, runner isolado por execução/projeto e agente de programação compatível |
| 005 | Adaptadores para GitHub, Notion e Drive com validate/execute/verify/reconcile |
| 006 | Memória por proveniência, validade e fontes canônicas |
| 007 | Logs, métricas, traces e trilha de auditoria |
| 008 | Backend modular com referência AWS (ECS/Fargate, Step Functions Standard, SQS, S3, Aurora, Terraform), sem provisão |
| 009 | Quotas, timeouts, concorrência e orçamento operacional |

## Arquitetura
ChatGPT/plugin → Control Plane → PEP/Approval Manager → BMad Runner/Connector Adapters → Durable State & Evidence Ledger.

## Invariantes
Nenhum efeito externo sem autorização válida; aprovação vinculada a plano e recurso; nenhum merge automático; resultado ambíguo exige consulta ao destino; não alegar exactly-once universal; memória não substitui evidência canônica.

## Parâmetros sugeridos, não homologados
3 rodadas deliberativas; até 6 agentes; 1 execução de escrita por projeto; autorização por 24 horas; runner 30 minutos; até 3 retries seguros. Revalidar na implementação.
