# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the user | [optional] 
**organization_id** | **str** | The unique identifier for the organization to which the user belongs | [optional] 
**name** | **str** | The user&#39;s name | [optional] 
**description** | **str** | A description of the user | [optional] 
**login_name** | **str** | A unique login name for the user | [optional] 
**email** | **str** | An email address for the user | [optional] 
**phone** | **str** | The user&#39;s phone number | [optional] 
**mobile** | **str** | The user&#39;s mobile number | [optional] 
**role** | **str** | The user&#39;s role, one of: user, oadmin, or admin | [optional] 
**image** | **str** | The user&#39;s photo. To update the image, please refer to the API. | [optional] 
**enabled** | **bool** | Indicates whether or not the user account is enabled or not | [optional] [default to False]
**created_on** | **int** | Epoch/Unix time stamp when the organization was created | [optional] 
**state** | **str** | The current state of the account, one of: approved, pending | [optional] 
**type** | **str** | Indicates the type of user. Possible values: internal, external | [optional] 
**auth_attrs** | [**AuthenticatedUserAttributes**](AuthenticatedUserAttributes.md) |  | [optional] 
**dn** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


