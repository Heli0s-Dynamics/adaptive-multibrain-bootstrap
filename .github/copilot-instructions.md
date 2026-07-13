# GitHub Copilot instructions

Read `AGENTS.md` before proposing code.

- Prefer Python standard library for the fleet runtime.
- Keep fleet behavior deterministic when a seed is provided.
- Route all persistent learning into `state/aihub/` and expose evaluation/pruning reports.
- Do not create direct-to-main automation.
- Azure authentication must use OIDC; never add client secrets.
- Azure changes must run `what-if` before any deployment.
- PowerShell, disk, security, Intune, Purview, and BitLocker operations require separate guarded modules and explicit human approval.
