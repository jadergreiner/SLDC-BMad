# Catálogo de agentes e modos

## Adaptadores de papéis oficiais (não incluem o código original)
- bmad-analyst-adapter → Analyst / discovery
- bmad-product-manager-adapter → Product Manager / PRD
- bmad-product-owner-adapter → Product Owner / histórias
- bmad-architect-adapter → Architect / ADR
- bmad-developer-adapter → Developer / implementação
- bmad-ux-designer-adapter → UX Designer / experiência

## Especialistas customizados (instruções próprias)
- specialist-data-architect
- specialist-cloud-architect
- specialist-security-engineer
- specialist-qa-test-architect
- specialist-sre-devops
- specialist-business-risk-analyst

## Seleção dinâmica
Analyst e PM em discovery; PO em histórias; Architect em decisões estruturais; Developer em implementação; UX para jornadas. Convocar Data quando houver armazenamento, ingestão, modelagem ou consistência; Cloud em infraestrutura ou custo; Security em identidade/dados sensíveis/efeito externo; QA para homologação, testes e qualidade; SRE em operação, deploy ou falhas; Business Risk para efeitos financeiros, clientes ou continuidade. Selecionar por risco e competência, registrar motivo e permitir contestação.

## Modo executado vs simulado
`real_tool_verified` somente quando skill/workflow oficial estiver instalado, runtime compatível executado, retorno e evidências verificáveis. Até lá, o plugin produz uma revisão por perspectivas especializadas simuladas, não processos autônomos independentes.

## Compatibilidade
O catálogo deve consultar e verificar a instalação exata do BMad antes de invocar um workflow, sem inferir APIs ou caminhos. Não contém MCP server, container runner ou provisionamento.
