# AuthorizationCode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier | [optional] 
**title** | **str** | Schema title | [optional] 
**description** | **str** | Description of the Schema | [optional] 
**format** | **str** | The format ex: int32, int64, float, double, byte, binary, date, date-time or password | [optional] 
**required** | **list[str]** | Specifies if the parameter is required | [optional] 
**properties** | [**dict(str, SchemaObject)**](SchemaObject.md) | Not used beacause our model does not support inline nested types | [optional] 
**items** | [**SchemaObject**](SchemaObject.md) | if the schema is an array specifies the items type | [optional] 
**example** | **object** | if the schema is an array specifies the items type | [optional] 
**discriminator** | **str** |  | [optional] 
**token_request_endpoint** | [**TokenRequestEndpoint**](TokenRequestEndpoint.md) | The login endpoint definition. | [optional] 
**token_endpoint** | [**TokenEndpoint**](TokenEndpoint.md) | The login endpoint definition. | [optional] 
**ref** | **str** | A Reference to a definition on definitions object | [optional] 
**default** | **object** | Default value for this schema if it is applicable | [optional] 
**type** | **str** | The type ex: array , boolean, integer , null , number, object, string | [optional] 
**enum** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


