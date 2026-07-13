# Adaptive Multibrain Bootstrap

GitHub-first control plane for the HELIOS / XTier workstation, Azure platform, Copilot/Codex collaboration, and the Hermes/XCore agent fleet.

## Foundation now in this repository

- bounded Hermes/XCore learning and pruning runtime
- pull-request-only fleet state updates
- GitHub Copilot repository instructions
- Codex project sandbox and agent boundaries
- CI tests and secret scanning
- Azure OIDC what-if workflow
- subscription-scope Bicep resource-group baseline

## Safety model

Agents may evaluate, learn, prune, write reports, create branches, and open pull requests. They may not push directly to `main`, deploy Azure from the learning workflow, format disks, alter BitLocker, or write plaintext secrets.

## Start locally

```powershell
python -m unittest discover -s tests -v
python scripts/fleet_runtime.py --cycles 8 --seed 64
```

## Start in GitHub

1. Merge the foundation pull request after CI passes.
2. Open **Actions → Hermes XCore Learning → Run workflow**.
3. Review the generated fleet-state pull request.
4. Configure the Azure OIDC variables described in `docs/ACTIVATION.md` before running Azure what-if.

The larger workstation, GUI, DevDrive, Microsoft 365, Intune, Purview, Foundry, and installer modules remain separate approval-gated phases.