# OAuthClient

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The client ID to be used in OAuth flows | [optional] 
**cert** | **str** | The PEM encodeded certificate used in JWT flow | [optional] 
**secret** | **str** | The client application secret to be used in OAuth flows | [optional] 
**type** | **str** | OAuth defines two client types, based on their ability to authenticate securely with the authorization server. Possible values public or confidential | [optional] 
**enabled** | **bool** | Flag disables the OAuth credentials so they can&#39;t be used in authentication | [optional] [default to False]
**redirect_urls** | **list[str]** | The URL where the server will redirect the to present authorization codes or access tokens depending on the OAuth flow being executed | [optional] 
**cors_origins** | **list[str]** | The domains to allow access for browser-based clients | [optional] 
**created_by** | **str** | The unique identifier for user that generated the OAuth credentials | [optional] 
**created_on** | **int** | Epoch/Unix time stamp when the OAuth credentials was created | [optional] 
**application_id** | **str** | The application identifier associated with the OAuth credential | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


