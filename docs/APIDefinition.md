# APIDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier. | [optional] 
**name** | **str** | The name of the API. | [optional] 
**summary** | **str** | A summary of the API. | [optional] 
**description** | **str** | A detailed description of the API. | [optional] 
**version** | **str** | The API version. | [optional] 
**base_path** | **str** | The base path is where the API service is hosted. | [optional] 
**_resource_path** | **str** | The resource path is applied to **basePath** to provide the prefix for all API methods. | [optional] 
**models** | **dict(str, object)** | The models/schema the that the API | [optional] 
**consumes** | **list[str]** | The content types that the API consumes | [optional] 
**produces** | **list[str]** | The content types that the API produces | [optional] 
**integral** | **bool** | Indicates that the API definition is integral to a frontend API; that the API was imported to define the frontend API. | [optional] [default to False]
**created_on** | **int** | Epoch/Unix time stamp when the organization was created. | [optional] 
**created_by** | **str** | The identifier of the user that created the API. | [optional] 
**organization_id** | **str** | The [Organization](Organization.html) identifier. | [optional] 
**service_type** | **str** | Indicates the type of service being imported. Possible values: rest, wsdl. | [optional] 
**has_original_definition** | **bool** | Indicates whether or not an original definition is available | [optional] [default to False]
**import_url** | **str** | Specifies the URL used to import the backend API definition. | [optional] 
**properties** | **dict(str, str)** | A list of properties associated with this API. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


