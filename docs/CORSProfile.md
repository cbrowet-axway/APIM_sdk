# CORSProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name of the Profile | [optional] 
**is_default** | **bool** | Indicates that this is the default profile.  There can be only one default. | [optional] [default to False]
**origins** | **list[str]** | List of origins for this CORS Profile | [optional] 
**allowed_headers** | **list[str]** | List of headers... | [optional] 
**exposed_headers** | **list[str]** | List of headers... | [optional] 
**support_credentials** | **bool** | Specifies whether or credentials are supported for APIs/API Methods employing this CORS Profile. | [optional] [default to False]
**max_age_seconds** | **int** | Specifies the amount of time responses to OPTIONS requests are stored, in seconds, in the preflight result cache | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


