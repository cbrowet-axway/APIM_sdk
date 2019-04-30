# APIKey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID which is used to identify the API Key. You include it in each request, so it&#39;s not a secret. | [optional] 
**application_id** | **str** | The ID which is used to identify an application. You include it in each request, so it&#39;s not a secret. | [optional] 
**secret** | **str** | Each  API Key ID has a Secret Key associated with it. This key is just a long string of characters that can be used to calculate the digital signature that can be included in requests. Your Secret Key is a secret do not distribute. | [optional] 
**enabled** | **bool** | Flag disables the API key so can&#39;t be used in authentication | [optional] [default to False]
**created_by** | **str** | The unique identifier for user that generated the API Key | [optional] 
**created_on** | **int** | Epoch/Unix time stamp when the API key was created | [optional] 
**deleted_on** | **int** | Epoch/Unix time stamp when the API key was deleted | [optional] 
**cors_origins** | **list[str]** | The domains to allow access for browser-based clients | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


