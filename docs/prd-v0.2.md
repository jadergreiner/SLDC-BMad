# PRD v0.2 — SDLC Orchestrator with BMad

**Status:** baseline de requisitos aprovado para planejamento, não autorização de infraestrutura.
**Data:** 2026-11-08.

## Visão
Plugin privado ChatGPT para SDLC completo com BMad oficial como referência e extensão por comitês multiagentes, workflows adaptativos, aprovação humana, auditoria e execução supervisionada.

## Requisitos funcionais
RF-01 Gestão de projetos; RF-02 Catálogo de agentes; RF-03 Deliberação multiagente; RF-04 Workflows adaptativos; RF-05 Requisitos; RF-06 Arquitetura; RF-07 Engenharia; RF-08 Qualidade; RF-09 Aprovações; RF-10 Integrações; RF-11 Reconciliação; RF-12 Memória; RF-13 Auditoria; RF-14 Operação; RF-15 Evolução.

## Requisitos não funcionais
Segurança e menor privilégio; idempotência quando tecnicamente suportada; auditabilidade; detecção de falhas parciais; extensibilidade; observabilidade; portabilidade; compatibilidade; integridade e privacidade.

## Contratos C-01 a C-08
- **C-01 Autorização:** operação externa requer autorização humana válida vinculada a projeto, recurso, ação e versão do plano.
- **C-02 Execução:** intenção identificável e evidência verificável; não confundir declaração com efeito real.
- **C-03 Reconciliação:** conferir destino antes de retentar resultado ambíguo; bloquear se inseguro.
- **C-04 Memória:** contexto especializado subordinado à fonte canônica mais recente.
- **C-05 Consenso:** registrar dissenso material e escalar se não solucionado após rodadas limitadas.
- **C-06 Compatibilidade:** fixar versão BMad e exigir regressão/aprovação para upgrade.
- **C-07 Segurança:** documentos e saídas externas são dados não confiáveis; não podem ampliar autoridade.
- **C-08 Auditoria:** transições vinculadas a ator, versão, autorização, resultado e evidência.

## Limites de V1
Sem merge automático, deploy autônomo em produção, alterações destrutivas não supervisionadas, alteração do núcleo oficial BMad ou transações distribuídas presumidas.

## AT-01 a AT-18
01 preservar BMad; 02 selecionar agentes; 03 escalar divergências; 04 bloquear escrita sem autorização; 05 restringir escopo; 06 PR sem merge; 07 falha parcial; 08 idempotência; 09 memória invalidada; 10 DoD por risco; 11 rastreabilidade; 12 upgrade controlado; 13 prompt injection; 14 segregação por projeto; 15 revogação; 16 concorrência; 17 resposta perdida após commit; 18 revalidação de fontes alteradas.

**Atenção:** os testes são requisitos de homologação; não há alegação de testes executados.
