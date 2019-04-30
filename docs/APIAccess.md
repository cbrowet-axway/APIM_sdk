# APIAccess

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for approval decisions (includes pending approvals) | [optional] 
**api_id** | **str** | Virtualised REST API unique id | [optional] 
**created_by** | **str** | The unique identifier for user that requested access | [optional] 
**state** | **str** | Pending or approved state | [optional] 
**created_on** | **int** | Epoch/Unix time stamp when the approval decision was created  | [optional] 
**enabled** | **bool** | Flag disables access to an API for organization or application | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


