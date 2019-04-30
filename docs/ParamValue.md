# ParamValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The parameter name. | [optional] 
**param_type** | **str** | The type of parameter type.  Can be one of: *body*, *query*, *path*, *form*, or *header*. | [optional] 
**type** | **str** | The parameter data type.  Can be one of: *string*, *integer*, etc. | [optional] 
**value** | **str** | The parameter value.  Can be a regular value, or a selector, e.g.: ${params.path.id}. | [optional] 
**required** | **bool** | Indicates whether or not the parameter is required for the backend API. | [optional] [default to False]
**exclude** | **bool** | Indicates whether or not the parameter is excluded for the backend API. | [optional] [default to False]
**additional** | **bool** | Indicates whether or not the parameter is an additional parameter (does not replace an existing parameter). | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


