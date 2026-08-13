targetScope = 'resourceGroup'

@description('Protected environment suffix.')
@allowed([
  'dev'
  'test'
  'prod'
])
param environment string = 'dev'

@description('Azure deployment location inherited from the existing resource group.')
param location string = resourceGroup().location

@description('Tags applied to AIHub bootstrap resources.')
param tags object = {}

var workloadIdentityName = 'id-helios-aihub-${environment}'
var keyVaultName = 'kvhai${environment}${uniqueString(resourceGroup().id)}'
var commonTags = union(tags, {
  Project: 'HELIOS'
  Workload: 'AIHub'
  Environment: environment
  ManagedBy: 'Bicep'
})

resource workloadIdentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: workloadIdentityName
  location: location
  tags: commonTags
}

resource keyVault 'Microsoft.KeyVault/vaults@2023-07-01' = {
  name: keyVaultName
  location: location
  tags: commonTags
  properties: {
    tenantId: tenant().tenantId
    enableRbacAuthorization: true
    enablePurgeProtection: true
    softDeleteRetentionInDays: 90
    publicNetworkAccess: 'Disabled'
    networkAcls: {
      bypass: 'None'
      defaultAction: 'Deny'
    }
    sku: {
      family: 'A'
      name: 'standard'
    }
  }
}

output workloadIdentityName string = workloadIdentity.name
output keyVaultName string = keyVault.name
