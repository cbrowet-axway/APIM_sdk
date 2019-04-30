# ApplicationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the application request | [optional] 
**name** | **str** | The display name for the application | [optional] 
**description** | **str** | Descriptive text for the application | [optional] 
**organization_id** | **str** | The organization identifier to which the application request belongs | [optional] 
**phone** | **str** | Contact phone number of the application | [optional] 
**email** | **str** | The contact email address associated with the application | [optional] 
**image** | **str** | URI of the image to be used for this application, this field only indicates that the application has an image assigned to it. In order to retrieve the actual image use the following URL /api/portal/organizations/{uid of org}/image/ | [optional] 
**apis** | **list[str]** | A list of unqiue API identifiers to which the application wants to use. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


