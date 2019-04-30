# VirtualizedAPI

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the virtualized API. | 
**organization_id** | **str** | The organization that created the virtualized API. | 
**api_id** | **str** | The identifier of the API that was virtualized.  This is the only attribute that is required to create a virtualized API. | 
**name** | **str** | The name of this virtualized API. | 
**version** | **str** | The API version. | 
**api_routing_key** | **str** | The key for routing between two APIs on the same path. | 
**vhost** | **str** | The virtual host of this virtualized API. | 
**path** | **str** | The path that services this virtualized API. | 
**description_type** | **str** | Type of descripton to use.  One of: _manual_, _markdown_, _url_, or _original_ (default). | 
**description_manual** | **str** | Markdown string to use as the description of the API. | 
**description_markdown** | **str** | Markdown file to use as the description of the API within the API Catalog. | 
**description_url** | **str** | External URL to use as the description of the API. | 
**summary** | **str** | A short summary description of the API. | 
**retired** | **bool** | Immediately retires the virtualized API. | [default to False]
**expired** | **bool** | Immediately expires the virtualized API. | [default to False]
**image** | **str** | URI of the image to be used for this virtualized API. To update the image, please refer to the API. | 
**retirement_date** | **int** | Date to retire the virtualized API.  If _retired_ is true, this is the date on which it was retired. | 
**deprecated** | **bool** | Immediately deprecates the virtualized API.  If deprecated, then _retiredOn_ is optionally used to retire the virtualized API on the specified date. | [default to False]
**state** | **str** | The state of the virtualized API.  One of: unpublished, pending, or published. | 
**created_on** | **int** | Epoch/Unix time stamp when the virtualized API was created. | [optional] 
**created_by** | **str** | The unique identifier for user that created the virtualized API. | [optional] 
**cors_profiles** | [**list[CORSProfile]**](CORSProfile.md) | The suite of CORS Profiles for this virtualized API. | 
**security_profiles** | [**list[SecurityProfile]**](SecurityProfile.md) | The suite of Security Profiles for this virtualized API. | 
**authentication_profiles** | [**list[AuthenticationProfile]**](AuthenticationProfile.md) | The suite of Security Profiles for this virtualized API. | 
**inbound_profiles** | [**dict(str, InboundProfiles)**](InboundProfiles.md) | The inbound profiles that apply to the virtualized API.  There must always a *\\_default* profile. | 
**outbound_profiles** | [**dict(str, OutboundProfiles)**](OutboundProfiles.md) | The outbound profiles that apply to the virtualized API.  There must always a *\\_default* profile. | [optional] 
**service_profiles** | [**dict(str, ServiceProfiles)**](ServiceProfiles.md) | The inbound profiles that apply to the virtualized API.  There must always a *\\_default* profile. | 
**ca_certs** | [**list[CACert]**](CACert.md) | The outbound profiles that apply to the virtualized API.  There must always a *\\_default* profile. | 
**tags** | **dict(str, list[str])** | The list of tags associated with this API. Each tag can have multiple values | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


