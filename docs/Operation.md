# Operation

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
**http_method** | **str** | The HTTP method | [optional] 
**nickname** | **str** | The nickname of the operation | [optional] 
**summary** | **str** | A short summary description of the operation | [optional] 
**notes** | **str** | A detailed description of the operation | [optional] 
**response_class** | **str** | The return type of the method, e.g. void, array, or a type found in models | [optional] 
**error_responses** | [**list[ErrorResponse]**](ErrorResponse.md) | A list of possible response messages and their meanings | [optional] 
**consumes** | **list[str]** | The content types that the operation consumes | [optional] 
**produces** | **list[str]** | The content types that the operation produces | [optional] 
**authorizations** | **dict(str, list[object])** | Authorizations | [optional] 
**tags** | **dict(str, list[str])** | The list of tags associated with this API operation. Each tag can have multiple values | [optional] 
**security_profile** | [**SwaggerSecurityProfile**](SwaggerSecurityProfile.md) | The security profile associated with the API Method. This profile will override the profile associated with the API | [optional] 
**documentation_url** | **str** | The documentation URL for the operation | [optional] 
**cors** | **bool** | Indicates that the API is CORS enabled | [optional] [default to False]
**parameters** | [**list[Parameter]**](Parameter.md) | A list of accepted parameters | [optional] 
**ref** | **str** | A Reference to a definition on definitions object | [optional] 
**default** | **object** | Default value for this schema if it is applicable | [optional] 
**type** | **str** | The return type of the method, e.g. void, array, or a type found in models | [optional] 
**enum** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


