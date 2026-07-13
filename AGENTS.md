# HELIOS agent operating contract

## Required behavior

- Work through a branch and pull request; never mutate `main` directly.
- Keep learning bounded by `config/aihub/policy.json`.
- Treat `state/aihub/` as reviewable derived state, not hidden memory.
- Preserve rollback information in workflow artifacts.
- Run tests before proposing changes.
- Never commit API keys, access tokens, tenant secrets, recovery keys, or generated credentials.

## Agent roles

- **Hermes:** task generation, routing experiments, lightweight learning, summaries.
- **XCore:** evaluation, pruning, regression detection, policy enforcement.
- **Guardian:** rejects unsafe state transitions, secret exposure, destructive workstation actions, and unreviewed cloud deployment.

## Azure boundary

Azure workflows use OpenID Connect and what-if first. Deployment requires a separate protected environment, explicit approval, and a dedicated deployment workflow.