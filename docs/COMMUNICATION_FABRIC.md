# HELIOS / Monado Unified Communication Fabric

## Purpose

Give GitHub Copilot, Codex, Hermes/XCore, Microsoft Copilot, Copilot Studio, Azure services, and the Monado/HELIOS repositories one governed communication model.

## Authority model

- `Heli0s-Dynamics/adaptive-multibrain-bootstrap`: control plane, shared policy, integration contracts, GitHub/Azure bootstrap, fleet evaluation.
- `M0nado/helios-platform`: canonical product and execution platform.
- Satellite repositories: bounded modules with explicit ownership in `config/integrations/repositories.json`.

No satellite repository should silently redefine the product architecture.

## Communication layers

1. **GitHub engineering plane**
   - Issues define scoped work.
   - Pull requests carry implementation and evidence.
   - Actions emit normalized events and artifacts.
   - Copilot and Codex follow `AGENTS.md`, repository instructions, and path-specific policies.

2. **Agent plane**
   - Hermes generates/routs bounded tasks and summaries.
   - XCore evaluates, prunes, detects regressions, and validates policy.
   - Learning state is reviewable Git data; raw evidence remains workflow artifacts or governed Azure storage.

3. **Azure integration plane**
   - GitHub authenticates using workload identity federation.
   - An Azure Function or Container App acts as the integration broker.
   - Service Bus provides durable commands/events; Event Grid distributes notifications.
   - Key Vault holds connector secrets; Application Insights and Log Analytics hold telemetry.
   - Azure AI Foundry hosts approved model/agent deployments and evaluations.

4. **Microsoft business plane**
   - Microsoft Copilot and Copilot Studio call approved broker APIs or custom connectors.
   - Microsoft Graph publishes governed cards/messages to Teams and evidence/runbooks to SharePoint.
   - Power Platform and Fabric consume approved APIs and curated datasets, never raw repository credentials.
   - Purview labels and retention apply to published operational evidence.

5. **HELIOS / Monado execution plane**
   - `M0nado/helios-platform` consumes approved commands and emits platform events.
   - Control Center displays state and exposes approved commands.
   - AIHub adapts model providers and agent runtimes.
   - Monado Blade owns themed interaction and engine contracts.

## Event contract

All systems exchange `config/integrations/event-contract.schema.json` envelopes. Payloads must include correlation, environment, classification, links, and a bounded object payload. Secrets and recovery material are prohibited.

## Command safety

Commands that change disks, BitLocker, WDAC/AppLocker, firewall policy, Entra/RBAC, Intune, Purview, production Azure, or secrets must include:

- explicit requested operation;
- target/environment;
- human approval record;
- dry-run/what-if evidence when supported;
- rollback plan;
- correlation ID and audit link.

Microsoft Copilot and Copilot Studio may request an operation but cannot bypass GitHub/Azure approval gates.

## Activation sequence

1. Merge the GitHub fleet foundation.
2. Merge the matching contract PR in `M0nado/helios-platform`.
3. Protect `main` and Azure environments.
4. Configure Azure OIDC variables.
5. Deploy the integration broker with Bicep what-if and approval.
6. Register Microsoft Graph/Copilot Studio connectors with least privilege.
7. Run an end-to-end development event: GitHub issue → broker → platform acknowledgement → Teams test message → evidence artifact.
8. Enable Hermes/XCore evaluation only after the contract test passes.