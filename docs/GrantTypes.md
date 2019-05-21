# GrantTypes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier | [optional] 
**title** | **str** | Schema title | [optional] 
**description** | **str** | Description of the Schema | [optional] 
**format** | **str** | The format ex: int32, int64, float, double, byte, binary, date, date-time or password | [optional] 
**required** | **list[str]** | Specifies if the parameter is required | [optional] 
**properties** | [**dict(str, SchemaObject)**](SchemaObject.md) | Not used because our model does not support inline nested types | [optional] 
**items** | [**SchemaObject**](SchemaObject.md) | if the schema is an array specifies the items type | [optional] 
**example** | **object** | if the schema is an array specifies the items type | [optional] 
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
**collection_format** | **str** |  | [optional] 
**discriminator** | **str** |  | [optional] 
**implicit** | [**Implicit**](Implicit.md) | The Implicit Grant flow definition. | [optional] 
**authorization_code** | [**AuthorizationCode**](AuthorizationCode.md) | The Authorization Code Grant flow definition. | [optional] 
**ref** | **str** | A Reference to a definition on definitions object | [optional] 
**default** | **object** | Default value for this schema if it is applicable | [optional] 
**type** | **str** | The type ex: array , boolean, integer , null , number, object, string | [optional] 
**enum** | **list[object]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


