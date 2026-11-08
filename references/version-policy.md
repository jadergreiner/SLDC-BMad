# Política de verificação e proposta de atualização (SDLC/BMad)

- **Fonte SDLC:** `jadergreiner/SLDC-BMad`, `plugin.json` da branch canônica ou release fixado; comparar SemVer e, quando possível, `commit SHA` e changelog.
- **Fonte BMad:** repositório oficial `bmad-code-org/BMAD-METHOD`, somente releases estáveis (não draft/prerelease); versão local deve ser comprovada por instalação/manifest/lockfile, nunca deduzida do PRD.
- **SemVer:** patch = revisão limitada; minor = possível alteração de novos comportamentos; major = possível quebra de contratos. Em todos os casos exigir leitura do changelog e regressão. A classificação é indicativa, não garante compatibilidade.
- **Drift sem version bump:** alertar quando SHA/artefatos diferirem mantendo versão; não instalar de branch mutável sem aprovação.
- **Source unavailable:** `UNKNOWN` e evidência da falha de consulta; nunca reportar `CURRENT` sem comparação confiável.
- **Aprovação:** propor upgrade com versão de origem, versão de destino, changelog, diff, testes AT-01–AT-18, riscos C-01–C-08, plano de rollback e gate. Nenhuma atualização automática.
- **Periodicidade:** somente em solicitação expressa ou disparo de automação externa devidamente configurada. A skill não monitora em background.
- **Ações permitidas antes da aprovação:** leituras remotas/locais somente, sem efeitos de escrita; verificar autorização de acesso ao repositório privado quando aplicável.
