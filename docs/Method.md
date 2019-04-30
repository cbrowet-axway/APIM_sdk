# Method

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The method identifier | [optional] 
**api_id** | **str** | The API identifier to which this method belongs | [optional] 
**path** | **str** | The API path | [optional] 
**verb** | **str** | The HTTP verb | [optional] 
**name** | **str** | The name of the operation | [optional] 
**summary** | **str** | A short summary description of the operation | [optional] 
**description** | **str** | A detailed description of the operation | [optional] 
**return_type** | **str** | The return type of the method, e.g. void, array, or a type found in models | [optional] 
**parameters** | [**list[Parameter]**](Parameter.md) | A list of accepted parameters | [optional] 
**response_codes** | [**list[ResponseCode]**](ResponseCode.md) | A list of possible response messages and their meanings | [optional] 
**consumes** | **list[str]** | The content types that the operation consumes | [optional] 
**produces** | **list[str]** | The content types that the operation produces | [optional] 
**properties** | **dict(str, str)** | A list of properties associated with this API Method. The list of properties may vary, depending on the type of the parent API. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


