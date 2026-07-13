# HELIOS agent operating contract

## Source-of-truth map

- `Heli0s-Dynamics/adaptive-multibrain-bootstrap` is the cross-repository control plane, policy catalog, Azure/GitHub bootstrap, and Hermes/XCore learning coordinator.
- `M0nado/helios-platform` is the canonical HELIOS / Monado product and execution platform.
- `M0nado/Helios-Control-Center` owns the operator GUI and command surface.
- `M0nado/helios-ai-hub` owns AI orchestration services and model/agent adapters.
- `M0nado/helios-monado-blade` owns the Monado Blade engine and themed interaction layer.
- `Yolkster64/hermes-fleet-platforms` is the companion fleet implementation until its stable modules are promoted into the canonical platform.

Read `config/integrations/repositories.json` before making cross-repository changes.

## Required behavior

- Work through a branch and pull request; never mutate `main` directly.
- Keep learning bounded by `config/aihub/policy.json`.
- Treat `state/aihub/` as reviewable derived state, not hidden memory.
- Preserve rollback information in workflow artifacts.
- Run tests and integration-contract validation before proposing changes.
- Never commit API keys, access tokens, tenant secrets, recovery keys, or generated credentials.
- Use the normalized event contract for communication between GitHub, Azure, Microsoft Copilot, Copilot Studio, Codex, Hermes/XCore, and platform services.
- Do not make satellite repositories competing sources of truth; integrate them through packages, contracts, or explicitly tracked migrations.

## Agent roles

- **Hermes:** task generation, routing experiments, lightweight learning, summaries, and normalized event production.
- **XCore:** evaluation, pruning, regression detection, contract validation, and policy enforcement.
- **Copilot:** repository-local implementation and review assistance under `.github/copilot-instructions.md`.
- **Codex:** bounded implementation, tests, refactors, and issue/PR work under `.codex/config.toml` and this contract.
- **Microsoft Copilot / Copilot Studio:** business-facing orchestration through the Azure integration broker and Microsoft Graph; no direct repository mutation.
- **Guardian:** rejects unsafe state transitions, secret exposure, destructive workstation actions, unreviewed tenant changes, and unreviewed cloud deployment.

## Communication boundary

GitHub is the engineering source of truth. Azure provides federated identity, the integration broker, queues/topics, Key Vault, Foundry, telemetry, and deployment. Microsoft Graph and Copilot Studio connect Teams, SharePoint, Power Platform, Fabric, and Microsoft 365 only through least-privilege app identities and governed connectors.

## Azure boundary

Azure workflows use OpenID Connect and what-if first. Deployment requires a separate protected environment, explicit approval, cost/security review, and a dedicated deployment workflow. Microsoft Graph permissions and Copilot Studio connectors require explicit tenant-admin consent and must be tracked in GitHub issues.