# SDLC + BMad

Repositório de código-fonte e documentação do plugin privado ChatGPT **SDLC + BMad v0.1.0**.

**Estado:** plugin baseado em cinco skills. O backend transacional, runner BMad real, conectores próprios e infraestrutura AWS **não foram implementados nem provisionados**.

## Conteúdo
- `plugin.json`: manifesto do plugin (metadados pessoais omitidos para publicação pública).
- `skills/`: cinco skills atuais extraídas da versão publicada.
- `docs/decisions.md`: 28 escolhas das três rodadas.
- `docs/prd-v0.2.md`: PRD e contratos C-01 a C-08.
- `docs/architecture-adr.md`: ADRs 001–009 aprovados para planejamento.
- `docs/backlog-v1.0.md`: 10 épicos, 35 histórias técnicas e gates G0–G5.

## Operação
Discovery → PRD → Arquitetura → Comitê → Aprovação humana → Execução supervisionada → Evidências → Auditoria.

**Atenção:** esta versão oferece instruções de planejamento, revisão e produção de artefatos, não autorização ou execução segura por backend. Não declarar que ferramentas externas foram executadas quando não houver evidências.

## Evolução
Primeiro concluir US-001 a US-004 e gate G0. Posteriormente desenvolver PEP, estado durável, runner isolado e adaptadores. Não realizar merges automáticos nem deploy autônomo de produção.

Referência: https://github.com/bmad-code-org/BMAD-METHOD
