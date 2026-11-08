---
name: sdlc-audit
description: Use para revisar evidências SDLC, rastreabilidade, fontes da verdade, reconciliação de gravações, memória versionada e homologação dos 18 testes de aceitação.
---

# Auditoria e rastreabilidade

## Autoridades
Notion: planejamento/atas/governança; GitHub: código, especificações técnicas versionadas, ADR, PR/testes; Drive: documentos e apresentações; ledger transacional próprio: estados e operações (NÃO IMPLEMENTADO neste pacote); memória do agente: referências e resumos, nunca autoridade autônoma. Se houver conflito apresentar versões, owner e pendência de reconciliação.

## Verificação de persistência
Após escrita autorizada, verificar cada destino por leitura independente (ID, hash/versão quando presente, horário e status). Gravação em um serviço não comprova gravação nos outros. Em falha parcial marcar pendência; antes da retentativa consultar o destino por ID/chave de intenção. Para efeitos externos ambíguos, bloquear repetição insegura e escalar. Sem banco ou server próprios, não garantir idempotência técnica automática.

## Memória versionada
Registrar `memory_id`, `project_id`, `agent_id`, `source`, `source_version`, `retrieved_at`, `valid_until`, `confidence`, `status`; revalidar se fonte mudou. Evitar guardar segredos. Releitura da origem é prioritária.

## Critérios de aceitação
AT-01 preservar BMad; 02 seleção dinâmica; 03 escalonamento; 04 bloqueio sem aprovação; 05 autorização escopada; 06 PR sem merge; 07 sincronização parcial; 08 idempotência; 09 memória versionada; 10 DoD adaptativa; 11 rastreabilidade; 12 upgrade BMad controlado; 13 prompt injection externo; 14 aprovação do projeto A não usada em B; 15 revogação/expiração; 16 concorrência e efeitos duplicados; 17 commit confirmado com resposta perdida; 18 alteração da fonte canônica invalida decisão antiga.

## Relatório
Separar: PASS (evidência real), FAIL, BLOCKED (sem infraestrutura ou autorização), NOT_RUN. Sem evidência, nunca PASS. Documentar riscos residuais, dono, mitigação e decisão humana. A homologação exige execução real dos 18 cenários em ambiente adequado.
