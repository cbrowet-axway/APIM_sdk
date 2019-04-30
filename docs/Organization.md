# Organization

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the organization | [optional] 
**name** | **str** | The name of the organization | 
**description** | **str** | The description of the organization | [optional] 
**email** | **str** | The contact email address associated with the organization | [optional] 
**image** | **str** | URI of the image to be used for this organization. To update the image, please refer to the API. | [optional] 
**restricted** | **bool** | Indicates that the organization is restricted.  Users in a restricted organization cannot see other users, and users cannot register for the organization using tokens.  Default is &#39;false&#39;. | [optional] [default to False]
**virtual_host** | **str** | The virtual host associated with the organization | [optional] 
**phone** | **str** | Contact phone number of the organization | [optional] 
**enabled** | **bool** | Flag to indicate if this organization is enabled or not | [optional] [default to False]
**development** | **bool** | Flag to indicate if this organization is enabled or not for API development. | [optional] [default to False]
**dn** | **str** |  | [optional] 
**created_on** | **int** | Epoch/Unix time stamp when the organization was created | [optional] 
**start_trial_date** | **int** | Epoch/Unix time stamp when the trial starts | [optional] 
**end_trial_date** | **int** | Epoch/Unix time stamp when the trial expires | [optional] 
**trial_duration** | **int** | Length of the trial in days | [optional] 
**is_trial** | **bool** | Indicates if this Org is a trial or not | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


