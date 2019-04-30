# OAuthResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the oauth protected resource | 
**application_id** | **str** | The unique identifier for the application who has access to this resource | 
**uriprefix** | **str** | The uri prefix which this oauth protected resource relates to | [optional] 
**scopes** | **list[str]** | Set of scope strings that have been resolved from querying the OAuth Resource Service at the uri prefix | [optional] 
**enabled** | **bool** | Flag to indicate if this oauth protected resource is enabled or not | [optional] [default to False]
**is_default** | **bool** |  | [optional] [default to False]
**scope** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


