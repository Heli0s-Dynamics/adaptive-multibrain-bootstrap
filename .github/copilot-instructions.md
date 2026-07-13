# GitHub Copilot instructions

Read `AGENTS.md`, `config/integrations/repositories.json`, and `docs/COMMUNICATION_FABRIC.md` before proposing code.

## Repository role

This repository is the cross-repository HELIOS control plane. `M0nado/helios-platform` is the canonical product/execution platform. Do not duplicate product modules here when they belong in the platform.

## Engineering rules

- Prefer Python standard library for the bounded fleet runtime and typed C#/.NET contracts for long-lived platform services.
- Keep fleet behavior deterministic when a seed is provided.
- Route persistent learning into `state/aihub/` and expose evaluation/pruning reports.
- Use the normalized integration event schema for cross-repository and Azure/Microsoft communication.
- Do not create direct-to-main automation or hidden cross-repository writes.
- Azure authentication must use OIDC; never add client secrets.
- Azure changes must run Bicep `what-if` before deployment.
- Microsoft Graph, Copilot Studio, Teams, SharePoint, Power Platform, Fabric, Purview, and Intune integrations require least-privilege tenant identities and explicit admin consent.
- PowerShell, disk, security, Intune, Purview, and BitLocker operations require separate guarded modules and explicit human approval.
- Changes spanning repositories must identify the owning repository and produce separate reviewable pull requests.