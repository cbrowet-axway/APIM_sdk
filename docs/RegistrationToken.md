# RegistrationToken

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The registration code | [optional] 
**organization_id** | **str** | Unique identifier for the organization who the registration code applies to | [optional] 
**expiry** | **int** | Epoch/Unix time stamp when the registration code will expire | [optional] 
**created_on** | **int** | Epoch/Unix time stamp when the registration code was created | [optional] 
**created_by** | **str** | The unique identifier for user that created the registration code | [optional] 
**user_quota** | **int** | The remaining number of users that can use the registration code for self registration to an organization | [optional] 
**max_users** | **int** | The total number of users that can use the registration code for self registration to an organization since the code has been created | [optional] 
**enabled** | **bool** | Flag disables registration code so that it can no longer be used for registration | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


