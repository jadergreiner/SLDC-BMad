# SDLC + BMad

Plugin privado ChatGPT, versão **0.2.0**, com 17 skills: cinco de orquestração e governança, seis adaptadores dos papéis BMad oficiais e seis especialistas customizados.

**Importante:** adaptadores não são as skills oficiais BMad; sua execução real exige runtime BMad instalado e verificado. Sem runtime, as análises são perspectivas simuladas, não subagentes independentes.

## Componentes
- `plugin.json`: manifesto portátil.
- `skills/`: skills de orquestração, especialistas e adaptadores.
- `references/agent-catalog.md`: seleção dinâmica e modos de execução.
- `references/agent-output-contract.md`: contrato de saída dos agentes.
- `docs/`: PRD v0.2, decisões, ADRs e backlog de implementação.

## Regras
As 28 decisões, os contratos C-01 a C-08 e os ADRs 001–009 permanecem preservados. A execução externa exige autorização humana; não há merge automático ou deploy autônomo em produção. O backend transacional/PEP/runner não faz parte deste plugin skills-only.

Fonte BMad: https://github.com/bmad-code-org/BMAD-METHOD
