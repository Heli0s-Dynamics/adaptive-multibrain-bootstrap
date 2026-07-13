# Activation

## GitHub

1. Require pull requests for `main`.
2. Require the `validate` CI job.
3. Restrict direct pushes to `main`.
4. Merge the foundation PR.
5. Run **Hermes XCore Learning** manually with 8 cycles.
6. Review and merge only the generated `state/aihub` pull request if the evaluation report passes.

## Azure OIDC

Create a user-assigned managed identity or Entra application with a federated credential matching this repository and the protected environment.

Create GitHub environments:

- `azure-dev`
- `azure-test`
- `azure-prod`

Set environment variables, not secrets:

- `AZURE_CLIENT_ID`
- `AZURE_TENANT_ID`
- `AZURE_SUBSCRIPTION_ID`

Grant the identity only the scope required for the environment. Run **Azure OIDC What-If** before creating a separate approved deployment workflow.

## Copilot and Codex

Copilot reads `.github/copilot-instructions.md`. Codex reads `.codex/config.toml` and `AGENTS.md`. Both are prohibited from direct-main writes, secrets, disk formatting, BitLocker changes, or Azure deployment through the learning workflow.
