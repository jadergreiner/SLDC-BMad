# Contrato compartilhado de saída dos agentes (v1)

Todo parecer de agente ou adaptador deve informar `agent_id`, `agent_version`, `official_role` (se aplicável), `project_id`, `decision_id`, `execution_mode` (`real_tool_verified` ou `simulated_perspective`), `recommendation` (`APPROVE`, `APPROVE_WITH_CONDITIONS`, `REJECT`, `ESCALATE`), `arguments`, `evidence_refs`, `risks`, `objections`, `confidence_qualitative`, `open_questions`, `blocking_conditions`, `source_versions`.

Somente `real_tool_verified` com identificadores de execução e evidências de ferramenta comprova execução real. Sem fonte: `not_verified`. Não usar consenso dos especialistas para substituir autorização humana; registrar R0, R1 e R2 e escalar dissenso material.

C-01 a C-08 aplicam-se integralmente. O catálogo oficial de papéis é um mapeamento de coordenação, não instalação do BMad original.
