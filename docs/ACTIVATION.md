# Activation

## GitHub

1. Require pull requests for `main`.
2. Require the `validate` CI job.
3. Restrict direct pushes to `main`.
4. Merge the foundation PR.
5. Run **Hermes XCore Learning** manually with 8 cycles.
6. Review and merge only the generated `state/aihub` pull request if the evaluation report passes.

## Azure OIDC

Pull requests run unauthenticated Bicep compilation only. They receive no OIDC
token, Azure identifiers, provider keys, or service connection.

Before anyone can run the manual AIHub resource-group what-if:

1. Create the `azure-dev` GitHub environment manually and add required reviewers,
   branch control for `main`, and an appropriate wait/approval policy. Do not rely
   on workflow execution to auto-create an unprotected environment.
2. Create a user-assigned managed identity or Entra application with a federated
   credential that exactly matches this repository and `azure-dev` environment.
3. Set these environment variables (not secrets):

   - `AZURE_CLIENT_ID`
   - `AZURE_TENANT_ID`
   - `AZURE_SUBSCRIPTION_ID`
   - `AZURE_RESOURCE_GROUP` (one exact pre-existing dev resource group)

4. Grant only the existing resource-group scope needed for ARM what-if. ARM
   what-if requires deployment-capable permissions, so restrict the identity to
   this fixed reviewed workflow and environment; never expose it to pull requests
   or arbitrary pipelines.
5. Only after the protected environment and variables are verified, set the
   repository variable `AZURE_WHATIF_ENABLED=true`.
6. Dispatch **Azure OIDC What-If** from `main`. Review the seven-day sanitized
   artifact. The workflow has no deployment command.

`infra/bicep/aihub/main.bicep` describes only an AIHub managed identity and private,
RBAC-enabled Key Vault. Networking, role assignments, federation, secret values,
compute, Foundry resources, and deployment are separate reviewed phases. Once the
vault has public access disabled, data-plane access requires an approved private
endpoint/DNS path and a trusted VNet-connected operator.

A deployment requires a separate protected workflow and explicit approval. Do not
add `az deployment * create` to the what-if workflow.

## Copilot and Codex

Copilot reads `.github/copilot-instructions.md`. Codex reads `.codex/config.toml`
and `AGENTS.md`. Both are prohibited from direct-main writes, secrets, disk
formatting, BitLocker changes, or Azure deployment through the learning workflow.
