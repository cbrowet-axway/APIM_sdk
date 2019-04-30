# TokenRequestEndpoint

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
**url** | **str** | The URL of the authorization endpoint for the authentication code grant flow. The value should be in a URL format. | [optional] 
**client_id_name** | **str** | An optional alternative name to standard \&quot;client_id\&quot; OAuth2 parameter. | [optional] 
**client_secret_name** | **str** | An optional alternative name to standard \&quot;client_secret\&quot; OAuth2 parameter. | [optional] 
**ref** | **str** | A Reference to a definition on definitions object | [optional] 
**default** | **object** | Default value for this schema if it is applicable | [optional] 
**type** | **str** | The type ex: array , boolean, integer , null , number, object, string | [optional] 
**enum** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


