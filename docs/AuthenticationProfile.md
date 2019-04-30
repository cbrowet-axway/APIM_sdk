# AuthenticationProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name of the Profile | [optional] 
**is_default** | **bool** | Indicates that this is the default profile.  There can be only one default. | [optional] [default to False]
**parameters** | **dict(str, object)** | Parameters for the backend authentication profile | [optional] 
**type** | **str** | Type of backend authentication. Possible values: *none*, *http_basic*, *http_digest*, *apiKey*, *oauth*, and *ssl*. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


