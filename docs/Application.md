# Application

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the application | [optional] 
**name** | **str** | The display name for the application | 
**description** | **str** | Descriptive text for the application | [optional] 
**organization_id** | **str** | The organization identifier to which the application belongs | 
**phone** | **str** | Contact phone number of the application | [optional] 
**email** | **str** | The contact email address associated with the application | [optional] 
**created_by** | **str** | The unique identifier for user that created the application | [optional] 
**managed_by** | **list[str]** | A list of unique identifier for users that manages the application | [optional] 
**created_on** | **int** | Epoch/Unix time stamp when the application was created | [optional] 
**enabled** | **bool** | Flag to indicate if this application is enabled or not | [optional] [default to False]
**image** | **str** | URI of the image to be used for this application, this field only indicates that the application has an image assigned to it. In order to retrieve the actual image use the following URL /api/portal/applications/{id}/image/ | [optional] 
**state** | **str** | Flag to indicate if an application has been approved by the API Manager admin or if delegated then the org admin | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


