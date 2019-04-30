# SwaggerSecurityDevice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type identifier for the device. Possible Values: HTTPBasicSecurityDevice, OAuthSecurityDevice, AWSRESTRequestSecurityDevice, AWSQueryStringRequestSecurityDevice, APIKeyOnlySecurityDevice, APIKeyAndSecretSecurityDevice, TwoWaySSLSecurityDevice | [optional] 
**type_display_name** | **str** | Textual display name for the device | [optional] 
**name** | **str** | Name of the device | [optional] 
**order** | **int** | Order of preference, zero being highest. Devices will attempt to authenticate the incoming request using this order of preference. | [optional] 
**scopes** | **list[str]** | The list of scopes defined for the security device. | [optional] 
**scope_matching** | **str** | Specifies how scopes will be matched. Possible values: [ Any, All ] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


