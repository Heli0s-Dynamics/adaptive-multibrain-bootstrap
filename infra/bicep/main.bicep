targetScope = 'subscription'

@description('Azure deployment location')
param location string = deployment().location

@description('Environment suffix')
@allowed(['dev', 'test', 'prod'])
param environment string = 'dev'

@description('Project prefix')
param prefix string = 'helios'

var groups = [
  '${prefix}-${environment}-core'
  '${prefix}-${environment}-ai'
  '${prefix}-${environment}-data'
  '${prefix}-${environment}-security'
]

resource resourceGroups 'Microsoft.Resources/resourceGroups@2024-03-01' = [for name in groups: {
  name: 'rg-${name}'
  location: location
  tags: {
    Project: 'HELIOS'
    Environment: environment
    ManagedBy: 'Bicep'
  }
}]

output resourceGroupNames array = [for group in resourceGroups: group.name]
