# VirtualizedMethodExport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the method. | [optional] 
**virtualized_api_id** | **str** | The identifier of the [VirtualizedAPI](VirtualizedAPI.html). | [optional] 
**name** | **str** | The virtualized method name.  This defaults to the original [APIDefinition](APIDefinition.html) method name. | [optional] 
**api_id** | **str** | The reference identifier for the original [APIDefinition](APIDefinition.html) that was virtualized. | [optional] 
**api_method_id** | **str** | The reference identifier for the original API [APIDefinition](APIDefinition.html) method that was virtualized. | [optional] 
**summary** | **str** | A summary of the API Method. | [optional] 
**description_type** | **str** | The source for the method&#39;s description.  One of: *original*, *manual*, *markdown*, or *url*.  Defaults to *original*. | [optional] 
**description_manual** | **str** | Specifies a manual description, which can be markdown text. | [optional] 
**description_markdown** | **str** | specifies a markdown file to use for description. | [optional] 
**description_url** | **str** | Specifies a URL to use instead of description text. | [optional] 
**tags** | **dict(str, list[str])** | The list of tags associated with this API method. Each tag can have multiple values. | [optional] 
**op** | **str** | Internal use only. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


