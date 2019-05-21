# swagger_client.APIRepositoryApi

All URIs are relative to *https://localhost/api/portal/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apirepo_get**](APIRepositoryApi.md#apirepo_get) | **GET** /apirepo | Get the list of API
[**apirepo_id_delete**](APIRepositoryApi.md#apirepo_id_delete) | **DELETE** /apirepo/{id} | Deletes an API.
[**apirepo_id_download_get**](APIRepositoryApi.md#apirepo_id_download_get) | **GET** /apirepo/{id}/download | Downloads an API by ID.
[**apirepo_id_get**](APIRepositoryApi.md#apirepo_id_get) | **GET** /apirepo/{id} | Get an API by ID
[**apirepo_id_methods_get**](APIRepositoryApi.md#apirepo_id_methods_get) | **GET** /apirepo/{id}/methods | Queries the list of API methods
[**apirepo_id_methods_method_id_delete**](APIRepositoryApi.md#apirepo_id_methods_method_id_delete) | **DELETE** /apirepo/{id}/methods/{methodId} | Delete an API method
[**apirepo_id_methods_method_id_get**](APIRepositoryApi.md#apirepo_id_methods_method_id_get) | **GET** /apirepo/{id}/methods/{methodId} | Get API method by ID.
[**apirepo_id_methods_method_id_put**](APIRepositoryApi.md#apirepo_id_methods_method_id_put) | **PUT** /apirepo/{id}/methods/{methodId} | Update an API method
[**apirepo_id_methods_post**](APIRepositoryApi.md#apirepo_id_methods_post) | **POST** /apirepo/{id}/methods | Create an API method
[**apirepo_id_put**](APIRepositoryApi.md#apirepo_id_put) | **PUT** /apirepo/{id} | Updates an API
[**apirepo_import_from_external_post**](APIRepositoryApi.md#apirepo_import_from_external_post) | **POST** /apirepo/importFromExternal | Create one or more backend APIs for an external service
[**apirepo_import_from_gw_post**](APIRepositoryApi.md#apirepo_import_from_gw_post) | **POST** /apirepo/importFromGw | Create an API definition by importing a PolicyStudio-registered web service (REST or WSDL) hosted on the the API Gateway
[**apirepo_import_from_url_post**](APIRepositoryApi.md#apirepo_import_from_url_post) | **POST** /apirepo/importFromUrl | Create an API by loading a file from URL.
[**apirepo_import_post**](APIRepositoryApi.md#apirepo_import_post) | **POST** /apirepo/import | Create an API by uploading a file
[**apirepo_post**](APIRepositoryApi.md#apirepo_post) | **POST** /apirepo | Create an API definition


# **apirepo_get**
> list[APIDefinition] apirepo_get(filename=filename, field=field, op=op, value=value)

Get the list of API

Get the list of API from the API repository.  The list of API can be filtered using the expression: field=__field__&op=__op__&value=__value__.  Optionally, you can add a logical operation for all expressions, using the form: &lop=AND|OR.  By default, the logical operation is AND.  Multiple expression filters can be used, specifying field, op, and value for each filter. The __field__ is one of:  id :    Matches the API by ID  name :    Matches the API by name  description :    Matches the API by description  version :    Matches the API by version  createdOn :      The date the backend API was created/imported on, time in ms, e.g.: 1372755998542  resourcePath :      Matches the API by resourcePath  basePath :      Matches the API by basePath  organization :      Matches the API by it's organization identifier  The __op__ is an operation and is one of:  eq :    Equal  ne :    Not equal  gt :     Greater than  lt :     Less than  ge :     Greater than or equal  le :     Less than or equal  like :    Like  gele :     Greater than or equal to, and less than or equal to; the __value__ should be a lower-minimum and upper-maximum separated by comma, e.g: value=5,10  The __value__ will be compared against the __field__, according to the supplied __op__.  

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
api_instance = swagger_client.APIRepositoryApi(swagger_client.ApiClient(configuration))
filename = 'filename_example' # str |  (optional)
field = ['field_example'] # list[str] | Filter field name. (optional)
op = ['op_example'] # list[str] | Filter operation. (optional)
value = ['value_example'] # list[str] | Filter value (optional)

try:
    # Get the list of API
    api_response = api_instance.apirepo_get(filename=filename, field=field, op=op, value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIRepositoryApi->apirepo_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**|  | [optional] 
 **field** | [**list[str]**](str.md)| Filter field name. | [optional] 
 **op** | [**list[str]**](str.md)| Filter operation. | [optional] 
 **value** | [**list[str]**](str.md)| Filter value | [optional] 

### Return type

[**list[APIDefinition]**](APIDefinition.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apirepo_id_delete**
> apirepo_id_delete(id)

Deletes an API.

Deletes a backend API.

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
api_instance = swagger_client.APIRepositoryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The API identifier.

try:
    # Deletes an API.
    api_instance.apirepo_id_delete(id)
except ApiException as e:
    print("Exception when calling APIRepositoryApi->apirepo_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The API identifier. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apirepo_id_download_get**
> apirepo_id_download_get(id, filename, original)

Downloads an API by ID.

Downloads an API by ID.  If __filename__ is not supplied, the API name will be used.  If the API was imported using [/import](#importApisFromFile) or [/import](#createApiFromUrl), then it is possible to download the original API definition by setting __original__ to __true__.

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
api_instance = swagger_client.APIRepositoryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
filename = 'filename_example' # str | Override the default filename for download
original = false # bool | If true, and the API was imported, this will download the original definition (default to false)

try:
    # Downloads an API by ID.
    api_instance.apirepo_id_download_get(id, filename, original)
except ApiException as e:
    print("Exception when calling APIRepositoryApi->apirepo_id_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **filename** | **str**| Override the default filename for download | 
 **original** | **bool**| If true, and the API was imported, this will download the original definition | [default to false]

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apirepo_id_get**
> APIDefinition apirepo_id_get(id)

Get an API by ID



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
api_instance = swagger_client.APIRepositoryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get an API by ID
    api_response = api_instance.apirepo_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIRepositoryApi->apirepo_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**APIDefinition**](APIDefinition.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apirepo_id_methods_get**
> list[Method] apirepo_id_methods_get(id, field=field, op=op, value=value)

Queries the list of API methods

Get the list of API methods from the API repository.  The list of methods can be filtered using the expression: field=__field__&op=__op__&value=__value__.  Optionally, you can add a logical operation for all expressions, using the form: &lop=AND|OR.  By default, the logical operation is AND.  Multiple expression filters can be used, specifying field, op, and value for each filter. The __field__ is one of:  id :    Matches the API by ID  name :    Matches the API by name  The __op__ is an operation and is one of:  eq :    Equal  ne :    Not equal  gt :     Greater than  lt :     Less than  ge :     Greater than or equal  le :     Less than or equal  like :    Like  gele :     Greater than or equal to, and less than or equal to; the __value__ should be a lower-minimum and upper-maximum separated by comma, e.g: value=5,10  The __value__ will be compared against the __field__, according to the supplied __op__.  

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
api_instance = swagger_client.APIRepositoryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
field = ['field_example'] # list[str] | Filter field name. (optional)
op = ['op_example'] # list[str] | Filter operation. (optional)
value = ['value_example'] # list[str] | Filter value (optional)

try:
    # Queries the list of API methods
    api_response = api_instance.apirepo_id_methods_get(id, field=field, op=op, value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIRepositoryApi->apirepo_id_methods_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **field** | [**list[str]**](str.md)| Filter field name. | [optional] 
 **op** | [**list[str]**](str.md)| Filter operation. | [optional] 
 **value** | [**list[str]**](str.md)| Filter value | [optional] 

### Return type

[**list[Method]**](Method.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apirepo_id_methods_method_id_delete**
> apirepo_id_methods_method_id_delete(id, method_id)

Delete an API method

Deletes a backend API method.

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
api_instance = swagger_client.APIRepositoryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The API identifier.
method_id = 'method_id_example' # str | The method identifier.

try:
    # Delete an API method
    api_instance.apirepo_id_methods_method_id_delete(id, method_id)
except ApiException as e:
    print("Exception when calling APIRepositoryApi->apirepo_id_methods_method_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The API identifier. | 
 **method_id** | **str**| The method identifier. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apirepo_id_methods_method_id_get**
> Method apirepo_id_methods_method_id_get(id, method_id)

Get API method by ID.

Retrieves a method for a given API.

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
api_instance = swagger_client.APIRepositoryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The API identifier.
method_id = 'method_id_example' # str | The API method ID.

try:
    # Get API method by ID.
    api_response = api_instance.apirepo_id_methods_method_id_get(id, method_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIRepositoryApi->apirepo_id_methods_method_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The API identifier. | 
 **method_id** | **str**| The API method ID. | 

### Return type

[**Method**](Method.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apirepo_id_methods_method_id_put**
> Method apirepo_id_methods_method_id_put(id, method_id, method)

Update an API method



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
api_instance = swagger_client.APIRepositoryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The API identifierentifier to create a method.
method_id = 'method_id_example' # str | The method identifier.
method = swagger_client.Method() # Method | The method to update.

try:
    # Update an API method
    api_response = api_instance.apirepo_id_methods_method_id_put(id, method_id, method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIRepositoryApi->apirepo_id_methods_method_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The API identifierentifier to create a method. | 
 **method_id** | **str**| The method identifier. | 
 **method** | [**Method**](Method.md)| The method to update. | 

### Return type

[**Method**](Method.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apirepo_id_methods_post**
> Method apirepo_id_methods_post(id, method)

Create an API method



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
api_instance = swagger_client.APIRepositoryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The API identifierentifier to create a method.
method = swagger_client.Method() # Method | The method to create.

try:
    # Create an API method
    api_response = api_instance.apirepo_id_methods_post(id, method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIRepositoryApi->apirepo_id_methods_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The API identifierentifier to create a method. | 
 **method** | [**Method**](Method.md)| The method to create. | 

### Return type

[**Method**](Method.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apirepo_id_put**
> APIDefinition apirepo_id_put(id, body=body)

Updates an API



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
api_instance = swagger_client.APIRepositoryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The API identifier.
body = swagger_client.APIDefinition() # APIDefinition |  (optional)

try:
    # Updates an API
    api_response = api_instance.apirepo_id_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIRepositoryApi->apirepo_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The API identifier. | 
 **body** | [**APIDefinition**](APIDefinition.md)|  | [optional] 

### Return type

[**APIDefinition**](APIDefinition.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apirepo_import_from_external_post**
> list[APIDefinition] apirepo_import_from_external_post(organization_id, connector_id, name, description, api)

Create one or more backend APIs for an external service

Create one or more backend APIs for an external service. External APIs are imported via a connector. If the connector configuration specifies that all external APIs should be merged into a single new backend API, the name and description parameters are applied to this new API. Alternatively, if the connector specifies that a separate backend API should be created for each external API, the name and description parameters are ignored, and the names and descriptions of the new backend APIs are taken from the external service definitions.

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
api_instance = swagger_client.APIRepositoryApi(swagger_client.ApiClient(configuration))
organization_id = 'organization_id_example' # str | The API development organization that owns the new APIs
connector_id = 'connector_id_example' # str | The API connector through which new APIs should be created
name = 'name_example' # str | The name of the merged API (see description)
description = 'description_example' # str | A description of the merged API (see description)
api = 'api_example' # str | List of external APIs to be imported

try:
    # Create one or more backend APIs for an external service
    api_response = api_instance.apirepo_import_from_external_post(organization_id, connector_id, name, description, api)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIRepositoryApi->apirepo_import_from_external_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The API development organization that owns the new APIs | 
 **connector_id** | **str**| The API connector through which new APIs should be created | 
 **name** | **str**| The name of the merged API (see description) | 
 **description** | **str**| A description of the merged API (see description) | 
 **api** | **str**| List of external APIs to be imported | 

### Return type

[**list[APIDefinition]**](APIDefinition.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apirepo_import_from_gw_post**
> APIDefinition apirepo_import_from_gw_post(id, name, organization_id, instance=instance, host=host, port=port, username=username, password=password)

Create an API definition by importing a PolicyStudio-registered web service (REST or WSDL) hosted on the the API Gateway

Imports an API definition from a Policy Studio REST or WSDL service hosted on the API Gateway. On import, a Swagger representation of the original API definition is retained, but the API is converted to an internal format for processing.

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
api_instance = swagger_client.APIRepositoryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the PolicyStudio-registered service to import.
name = 'name_example' # str | The service name.
organization_id = 'organization_id_example' # str | The API development organization ID that owns the import.
instance = 'instance_example' # str |  (optional)
host = 'host_example' # str |  (optional)
port = 'port_example' # str |  (optional)
username = 'username_example' # str |  (optional)
password = 'password_example' # str |  (optional)

try:
    # Create an API definition by importing a PolicyStudio-registered web service (REST or WSDL) hosted on the the API Gateway
    api_response = api_instance.apirepo_import_from_gw_post(id, name, organization_id, instance=instance, host=host, port=port, username=username, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIRepositoryApi->apirepo_import_from_gw_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the PolicyStudio-registered service to import. | 
 **name** | **str**| The service name. | 
 **organization_id** | **str**| The API development organization ID that owns the import. | 
 **instance** | **str**|  | [optional] 
 **host** | **str**|  | [optional] 
 **port** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 
 **password** | **str**|  | [optional] 

### Return type

[**APIDefinition**](APIDefinition.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apirepo_import_from_url_post**
> APIDefinition apirepo_import_from_url_post(organization_id, type, url, name=name, file_name=file_name, username=username, password=password)

Create an API by loading a file from URL.

Imports an API definition from a valid standard Swagger or WADL definition from the specified __url__.  It is possible to supply an optional __username__ and __password__ if the __url__ requires HTTP Basic authentication.  On import, the original API definition is retained, but the API is converted to an internal format for processing. The API name currently defaults to the filename but this will be deprecated in a future release. The name parameter should be used to name the API and will be required in a future release.

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
api_instance = swagger_client.APIRepositoryApi(swagger_client.ApiClient(configuration))
organization_id = 'organization_id_example' # str | The API development organization ID that owns the import.
type = 'type_example' # str | The type of import, one of: swagger, wadl, raml.
url = 'url_example' # str | The URL to import.
name = 'name_example' # str | The name of the API. (optional)
file_name = 'file_name_example' # str | The file name of the import. (optional)
username = 'username_example' # str | HTTP Basic username to use for connection. (optional)
password = 'password_example' # str | HTTP Basic password to use for connection. (optional)

try:
    # Create an API by loading a file from URL.
    api_response = api_instance.apirepo_import_from_url_post(organization_id, type, url, name=name, file_name=file_name, username=username, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIRepositoryApi->apirepo_import_from_url_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The API development organization ID that owns the import. | 
 **type** | **str**| The type of import, one of: swagger, wadl, raml. | 
 **url** | **str**| The URL to import. | 
 **name** | **str**| The name of the API. | [optional] 
 **file_name** | **str**| The file name of the import. | [optional] 
 **username** | **str**| HTTP Basic username to use for connection. | [optional] 
 **password** | **str**| HTTP Basic password to use for connection. | [optional] 

### Return type

[**APIDefinition**](APIDefinition.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apirepo_import_post**
> APIDefinition apirepo_import_post(organization_id, name, type, file)

Create an API by uploading a file

Imports an API definition from a valid standard Swagger or WADL definition.  On import, the original API definition is retained, but the API is converted to an internal format for processing.

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
api_instance = swagger_client.APIRepositoryApi(swagger_client.ApiClient(configuration))
organization_id = 'organization_id_example' # str | The API development organization ID that owns the import.
name = 'name_example' # str | The API name.
type = 'type_example' # str | The type of import, one of: swagger, wadl, raml
file = '/path/to/file.txt' # file | The API definition file to import

try:
    # Create an API by uploading a file
    api_response = api_instance.apirepo_import_post(organization_id, name, type, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIRepositoryApi->apirepo_import_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The API development organization ID that owns the import. | 
 **name** | **str**| The API name. | 
 **type** | **str**| The type of import, one of: swagger, wadl, raml | 
 **file** | **file**| The API definition file to import | 

### Return type

[**APIDefinition**](APIDefinition.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apirepo_post**
> APIDefinition apirepo_post(api)

Create an API definition

When creating an API, the __name__ and __basePath__ are required.

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
api_instance = swagger_client.APIRepositoryApi(swagger_client.ApiClient(configuration))
api = swagger_client.APIDefinition() # APIDefinition | The API resource to create.

try:
    # Create an API definition
    api_response = api_instance.apirepo_post(api)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIRepositoryApi->apirepo_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | [**APIDefinition**](APIDefinition.md)| The API resource to create. | 

### Return type

[**APIDefinition**](APIDefinition.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

