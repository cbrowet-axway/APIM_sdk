# Parameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The parameter name. | [optional] 
**type** | **str** | The parameter data type, e.g. *boolean*, *byte*, *date*, *double*, *float*, *integer*, *long*, *string*, or a type name found in [APIDefinition models](APIDefinition.html#models). | [optional] 
**format** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**required** | **bool** | Indicates that the parameter is required | [optional] [default to False]
**allow_multiple** | **bool** | Indicates that the parameter can be included multiple times (e.g. query or form) | [optional] [default to False]
**items** | [**SchemaObject**](SchemaObject.md) |  | [optional] 
**default_value** | **str** | Provides a default value for the parameter | [optional] 
**schema** | [**SchemaObject**](SchemaObject.md) | The response schema | [optional] 
**param_type** | **str** | The parameter type, e.g. query, form, path, body, header | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


