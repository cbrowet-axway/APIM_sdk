# swagger_client.APIDiscoveryApi

All URIs are relative to *https://localhost/api/portal/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discovery_apis_get**](APIDiscoveryApi.md#discovery_apis_get) | **GET** /discovery/apis | Lists all APIs/services virtualised in the API Server.
[**discovery_oauthresources_get**](APIDiscoveryApi.md#discovery_oauthresources_get) | **GET** /discovery/oauthresources | Gets a list OAuth protected resources and their associated scopes.
[**discovery_scopes_get**](APIDiscoveryApi.md#discovery_scopes_get) | **GET** /discovery/scopes | Retrieves every resource on the API Server that is protected by OAuth, and the scopes that cover those resources
[**discovery_sdk_id_platform_get**](APIDiscoveryApi.md#discovery_sdk_id_platform_get) | **GET** /discovery/sdk/{id}/{platform} | Generates an SDK package for the specified API based on the type of the client requested
[**discovery_swagger_api_id_id_get**](APIDiscoveryApi.md#discovery_swagger_api_id_id_get) | **GET** /discovery/swagger/api/id/{id} | Retrieves an extended Swagger feed for the specified API.
[**discovery_swagger_api_name_get**](APIDiscoveryApi.md#discovery_swagger_api_name_get) | **GET** /discovery/swagger/api/{name} | Retrieves an extended Swagger feed for the specified API.
[**discovery_swagger_apis_get**](APIDiscoveryApi.md#discovery_swagger_apis_get) | **GET** /discovery/swagger/apis | Convenience method for retrieving all Swagger feeds for all virtualised services.
[**discovery_swagger_apis_id_image_get**](APIDiscoveryApi.md#discovery_swagger_apis_id_image_get) | **GET** /discovery/swagger/apis/{id}/image | Retrieves the API image
[**discovery_swagger_apis_id_service_definition_get**](APIDiscoveryApi.md#discovery_swagger_apis_id_service_definition_get) | **GET** /discovery/swagger/apis/{id}/service-definition | Retrieves the service definition of the API. 


# **discovery_apis_get**
> list[DiscoveryAPI] discovery_apis_get()

Lists all APIs/services virtualised in the API Server.

Lists all APIs/services virtualised in the API Server. API Administrators see all APIs/services. Users see APIs/services for their organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.APIDiscoveryApi(swagger_client.ApiClient(configuration))

try:
    # Lists all APIs/services virtualised in the API Server.
    api_response = api_instance.discovery_apis_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIDiscoveryApi->discovery_apis_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DiscoveryAPI]**](DiscoveryAPI.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_oauthresources_get**
> discovery_oauthresources_get()

Gets a list OAuth protected resources and their associated scopes.

Gets a list OAuth protected resources and their associated scopes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.APIDiscoveryApi(swagger_client.ApiClient(configuration))

try:
    # Gets a list OAuth protected resources and their associated scopes.
    api_instance.discovery_oauthresources_get()
except ApiException as e:
    print("Exception when calling APIDiscoveryApi->discovery_oauthresources_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_scopes_get**
> list[OAuthProtectedResource] discovery_scopes_get()

Retrieves every resource on the API Server that is protected by OAuth, and the scopes that cover those resources

Retrieves every resource on the API Server that is protected by OAuth, and the scopes that cover those resources. Only API Administrators will be able to retrieve information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.APIDiscoveryApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves every resource on the API Server that is protected by OAuth, and the scopes that cover those resources
    api_response = api_instance.discovery_scopes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIDiscoveryApi->discovery_scopes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OAuthProtectedResource]**](OAuthProtectedResource.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_sdk_id_platform_get**
> discovery_sdk_id_platform_get(id, platform, packagename=packagename)

Generates an SDK package for the specified API based on the type of the client requested

Generates a client SDK package for the specified API based on the platform. Supported platform are Android, iOS-swift, NodeJS, Titanium

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.APIDiscoveryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The name of the API to generate the client SDK package for
platform = 'platform_example' # str | Generated client type, one of: android, iOS-swift, nodejS, titanium
packagename = 'com.axway' # str | Java package name generated only for Android platform. It must be a valid java package name. (optional) (default to com.axway)

try:
    # Generates an SDK package for the specified API based on the type of the client requested
    api_instance.discovery_sdk_id_platform_get(id, platform, packagename=packagename)
except ApiException as e:
    print("Exception when calling APIDiscoveryApi->discovery_sdk_id_platform_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The name of the API to generate the client SDK package for | 
 **platform** | **str**| Generated client type, one of: android, iOS-swift, nodejS, titanium | 
 **packagename** | **str**| Java package name generated only for Android platform. It must be a valid java package name. | [optional] [default to com.axway]

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_swagger_api_id_id_get**
> discovery_swagger_api_id_id_get(id, filename=filename, swagger_version=swagger_version, extensions=extensions)

Retrieves an extended Swagger feed for the specified API.

Retrieves an extended Swagger feed for the specified API. API Administrators will always see the API. Users will only see the API if it is available for their organization.If __filename__ is supplied, the download will use it as the `Content-Disposition` filename attachment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.APIDiscoveryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique ID of the API to return
filename = 'filename_example' # str | Override the default filename for download (optional)
swagger_version = '1.1' # str | The Swagger version of the feed, either 1.1 (default) or 2.0. (optional) (default to 1.1)
extensions = true # bool | If true, extensions such as the x-axway object are returned in the Swagger definitions (default=true) (optional) (default to true)

try:
    # Retrieves an extended Swagger feed for the specified API.
    api_instance.discovery_swagger_api_id_id_get(id, filename=filename, swagger_version=swagger_version, extensions=extensions)
except ApiException as e:
    print("Exception when calling APIDiscoveryApi->discovery_swagger_api_id_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique ID of the API to return | 
 **filename** | **str**| Override the default filename for download | [optional] 
 **swagger_version** | **str**| The Swagger version of the feed, either 1.1 (default) or 2.0. | [optional] [default to 1.1]
 **extensions** | **bool**| If true, extensions such as the x-axway object are returned in the Swagger definitions (default&#x3D;true) | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_swagger_api_name_get**
> discovery_swagger_api_name_get(name, filename=filename, api_version=api_version, swagger_version=swagger_version, extensions=extensions)

Retrieves an extended Swagger feed for the specified API.

Retrieves an extended Swagger feed for the specified API. API Administrators will always see the API. Users will only see the API if it is available for their organization.If __filename__ is supplied, the download will use it as the `Content-Disposition` filename attachment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.APIDiscoveryApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | The name of the API to return
filename = 'filename_example' # str | Override the default filename for download (optional)
api_version = 'api_version_example' # str | The version of the API. Should always be provided if there is more than one version (optional)
swagger_version = '1.1' # str | The Swagger version of the feed, either 1.1 (default) or 2.0. (optional) (default to 1.1)
extensions = true # bool | If true, extensions such as the x-axway object are returned in the Swagger definitions (default=true) (optional) (default to true)

try:
    # Retrieves an extended Swagger feed for the specified API.
    api_instance.discovery_swagger_api_name_get(name, filename=filename, api_version=api_version, swagger_version=swagger_version, extensions=extensions)
except ApiException as e:
    print("Exception when calling APIDiscoveryApi->discovery_swagger_api_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the API to return | 
 **filename** | **str**| Override the default filename for download | [optional] 
 **api_version** | **str**| The version of the API. Should always be provided if there is more than one version | [optional] 
 **swagger_version** | **str**| The Swagger version of the feed, either 1.1 (default) or 2.0. | [optional] [default to 1.1]
 **extensions** | **bool**| If true, extensions such as the x-axway object are returned in the Swagger definitions (default&#x3D;true) | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_swagger_apis_get**
> discovery_swagger_apis_get(api_version=api_version, swagger_version=swagger_version, extensions=extensions, field=field, op=op, value=value)

Convenience method for retrieving all Swagger feeds for all virtualised services.

Convenience method for retrieving all Swagger feeds for all virtualised services that are visible to the authenticated user.  The list of APIs can be filtered using the expression: field=__field__&op=__op__&value=__value__.  Optionally, you can add a logical operation for all expressions, using the form: &lop=AND|OR.  By default, the logical operation is AND.  Multiple expression filters can be used, specifying field, op, and value for each filter. The __field__ is one of:  id :        Matches the API by the specified ID  name :        Matches the API by the specified name  description :        Matches the API by the specified description  summary :        Matches the API by the specified summary  version :        Matches the API by the specified version  type :        Matches the API by the specified type. Type can be 'rest' or 'wsdl'  resourcepath :        Matches the API by the specified inbound path  taggroup :        Matches the API by the specified tag group  tag :        Matches the API by the specified tag value  methodtaggroup :        Matches the API by the specified method tag group, i.e. if the API contains a method that contains a tag group matching that specified  methodtag :        Matches the API by the specified method tag value, i.e. if the API contains a method that contains a tag value matching that specified  The __op__ is an operation and is one of:  eq :    Equal  ne :    Not equal  gt :     Greater than  lt :     Less than  ge :     Greater than or equal  le :     Less than or equal  like :    Like  gele :     Greater than or equal to, and less than or equal to; the __value__ should be a lower-minimum and upper-maximum separated by comma, e.g: value=5,10  The __value__ will be compared against the __field__, according to the supplied __op__. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.APIDiscoveryApi(swagger_client.ApiClient(configuration))
api_version = 'api_version_example' # str | The Swagger API version (optional)
swagger_version = '1.2' # str | The Swagger version (optional) (default to 1.2)
extensions = true # bool | If true, extensions such as the x-axway object are returned in the Swagger definitions (default=true) (optional) (default to true)
field = ['field_example'] # list[str] | Filter field name. (optional)
op = ['op_example'] # list[str] | Filter operation. (optional)
value = ['value_example'] # list[str] | Filter value (optional)

try:
    # Convenience method for retrieving all Swagger feeds for all virtualised services.
    api_instance.discovery_swagger_apis_get(api_version=api_version, swagger_version=swagger_version, extensions=extensions, field=field, op=op, value=value)
except ApiException as e:
    print("Exception when calling APIDiscoveryApi->discovery_swagger_apis_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The Swagger API version | [optional] 
 **swagger_version** | **str**| The Swagger version | [optional] [default to 1.2]
 **extensions** | **bool**| If true, extensions such as the x-axway object are returned in the Swagger definitions (default&#x3D;true) | [optional] [default to true]
 **field** | [**list[str]**](str.md)| Filter field name. | [optional] 
 **op** | [**list[str]**](str.md)| Filter operation. | [optional] 
 **value** | [**list[str]**](str.md)| Filter value | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_swagger_apis_id_image_get**
> discovery_swagger_apis_id_image_get(id)

Retrieves the API image



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.APIDiscoveryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The API identifier

try:
    # Retrieves the API image
    api_instance.discovery_swagger_apis_id_image_get(id)
except ApiException as e:
    print("Exception when calling APIDiscoveryApi->discovery_swagger_apis_id_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The API identifier | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_swagger_apis_id_service_definition_get**
> discovery_swagger_apis_id_service_definition_get(id)

Retrieves the service definition of the API. 



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.APIDiscoveryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The API identifier

try:
    # Retrieves the service definition of the API. 
    api_instance.discovery_swagger_apis_id_service_definition_get(id)
except ApiException as e:
    print("Exception when calling APIDiscoveryApi->discovery_swagger_apis_id_service_definition_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The API identifier | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

