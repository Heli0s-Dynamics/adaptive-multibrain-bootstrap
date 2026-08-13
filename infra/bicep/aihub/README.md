# AIHub Azure desired state

This resource-group-scoped module is a reviewable desired-state contract for one
AIHub user-assigned managed identity and one RBAC-enabled Key Vault. The vault has
purge protection, 90-day soft delete, and public network access disabled.

The module intentionally contains no role assignments, federated credentials,
secret values, private endpoint or DNS resources, compute, broker, Foundry model,
provider registration, resource-group creation, or deployment command. With public
access disabled and no private endpoint in this slice, the vault data plane is
deliberately unreachable until a separately reviewed networking phase exists.

Pull requests only compile the module without Azure authentication. The manual
workflow is disabled until an administrator creates and protects `azure-dev`,
configures environment-scoped OIDC variables, sets an exact existing resource
group, and enables the repository admission variable documented in
[`docs/ACTIVATION.md`](../../../docs/ACTIVATION.md). It runs resource-group
`what-if` only and uploads redacted evidence; it has no apply path.

Any deployment requires a separate protected workflow, exact target and artifact
binding, cost/security review, and explicit approval. This draft does not grant or
request that authority.
