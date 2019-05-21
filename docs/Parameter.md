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
**default_value** | **object** | Provides a default value for the parameter | [optional] 
**max_length** | **int** | Indicates the maximum length of a parameter of type &#39;string&#39; | [optional] 
**min_length** | **int** | Indicates the minimum length of a parameter of type &#39;string&#39;. If not present, assumed default value is 0. | [optional] 
**pattern** | **str** | Specifies a valid regular expression against which a parameter of type &#39;string&#39; is validated. | [optional] 
**exclusive_minimum** | **bool** | If true, specifies that the value of the number parameter must be greater than the specified minimum value, otherwise the value must be great than, or equal to, the specified minimum value. | [optional] [default to False]
**exclusive_maximum** | **bool** | If true, specifies that the value of the number parameter must be less than the specified maximum value, otherwise the value must be less than, or equal to, the specified maximum value. | [optional] [default to False]
**minimum** | **object** | Specifies the minimum possible value of the number parameter. | [optional] 
**maximum** | **object** | Specifies the maximum possible value of the number parameter. | [optional] 
**multiple_of** | [**Number**](Number.md) | Specifies that the value of the number parameter must be divisible by this value. Must be an integer value &gt; 0 | [optional] 
**max_items** | **int** | Specifies the maximum number of items permitted for array parameters. Must be an integer value greater than, or equal to 0 | [optional] 
**min_items** | **int** | Specifies the minimum number of items permitted for array parameters. Must be an integer value greater than, or equal to 0 | [optional] 
**unique_items** | **bool** | Specifies whether or not all array items should be unique. | [optional] [default to False]
**collection_format** | **str** | Specifies the format of array parameters. Possible values: [ csv, ssv, tsv, pipes, multi ]. | [optional] 
**schema** | [**SchemaObject**](SchemaObject.md) | The response schema | [optional] 
**enum** | **list[object]** |  | [optional] 
**param_type** | **str** | The parameter type, e.g. query, form, path, body, header | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


