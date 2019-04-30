# Authorization

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
**pass_as** | **str** | Denotes how the API key must be passed. Valid values are &#39;header&#39; or &#39;query&#39;. | [optional] 
**keyname** | **str** | The name of the header or query parameter to be used when passing the API key. | [optional] 
**scopes** | [**list[Scope]**](Scope.md) | The list of OAuth scopes. | [optional] 
**grant_types** | [**GrantTypes**](GrantTypes.md) | The OAuth grant types. | [optional] 
**ref** | **str** | A Reference to a definition on definitions object | [optional] 
**default** | **object** | Default value for this schema if it is applicable | [optional] 
**type** | **str** | The authorization type.  One of: basicAuth, apiKey, oauth2, none | [optional] 
**enum** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


