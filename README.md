# Adaptive Multibrain Bootstrap

Central control-plane repository for JP's combined AI/software/cloud/local development stack.

This repo is the project spine for bringing together:

- GitHub, GitHub CLI, GitHub Actions, Codespaces, and repository automation
- OpenAI Codex / ChatGPT-assisted development workflows
- Microsoft Copilot, Microsoft 365, Copilot Studio, Copilot Designer, Power Apps, Power BI, and Fabric
- Azure CLI, Azure resources, Azure AI Foundry, containers, identity, storage, and monitoring
- Local Windows workstation workflows, secure profiles, VHDX vaults, scripts, and dev environments
- Optional external AI collaborators such as Claude, Gemini, and other model/agent layers

## Mission

Build one clear, modular project system instead of scattered tools. The repo should become the place where local setup, cloud setup, AI agent workflows, documentation, and deployment automation all meet.

## Current Phase

Phase 0: Project spine and architecture map.

Before building production code, this repo should define:

1. What systems exist.
2. What each system is responsible for.
3. How local tools connect to cloud tools.
4. How AI assistants are allowed to operate.
5. How secrets, credentials, repositories, environments, and deployments are protected.

## Primary Repositories Found

- `Heli0s-Dynamics/adaptive-multibrain-bootstrap` — new control-plane/bootstrap repo.
- `Yolkster64/trading-platform-api` — larger existing repo candidate for trading/platform API work.

## Immediate Next Steps

1. Fill out `/docs/PROJECT_CONTROL_PLANE.md`.
2. Fill out `/docs/SYSTEM_ARCHITECTURE.md`.
3. Add local bootstrap scripts under `/scripts/local`.
4. Add Azure bootstrap scripts under `/scripts/azure`.
5. Add GitHub/Codespaces setup under `/.devcontainer` and `/.github/workflows`.
6. Decide whether existing code belongs here or stays in separate product repos.
