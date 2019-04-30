# swagger_client.APIProxyRegistrationApi

All URIs are relative to *https://localhost/api/portal/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**proxies_export_id_get**](APIProxyRegistrationApi.md#proxies_export_id_get) | **GET** /proxies/export/{id} | Downloads an API export.
[**proxies_export_post**](APIProxyRegistrationApi.md#proxies_export_post) | **POST** /proxies/export | Creates an API export.
[**proxies_get**](APIProxyRegistrationApi.md#proxies_get) | **GET** /proxies | Queries a list of frontend API.
[**proxies_grantaccess_post**](APIProxyRegistrationApi.md#proxies_grantaccess_post) | **POST** /proxies/grantaccess | Macro function to grant API access.
[**proxies_id_delete**](APIProxyRegistrationApi.md#proxies_id_delete) | **DELETE** /proxies/{id} | Deletes an API proxy.
[**proxies_id_deprecate_post**](APIProxyRegistrationApi.md#proxies_id_deprecate_post) | **POST** /proxies/{id}/deprecate | Deprecates the API.
[**proxies_id_get**](APIProxyRegistrationApi.md#proxies_id_get) | **GET** /proxies/{id} | Gets a frontend API by ID.
[**proxies_id_image_get**](APIProxyRegistrationApi.md#proxies_id_image_get) | **GET** /proxies/{id}/image | Gets the image for the API.
[**proxies_id_image_post**](APIProxyRegistrationApi.md#proxies_id_image_post) | **POST** /proxies/{id}/image | Set the image for the frontend API.
[**proxies_id_operations_get**](APIProxyRegistrationApi.md#proxies_id_operations_get) | **GET** /proxies/{id}/operations | Gets a list of methods that are avilable to the API proxy.
[**proxies_id_operations_operation_id_delete**](APIProxyRegistrationApi.md#proxies_id_operations_operation_id_delete) | **DELETE** /proxies/{id}/operations/{operationId} | Deletes an API method by ID.
[**proxies_id_operations_operation_id_get**](APIProxyRegistrationApi.md#proxies_id_operations_operation_id_get) | **GET** /proxies/{id}/operations/{operationId} | Gets an API method by ID.
[**proxies_id_operations_operation_id_put**](APIProxyRegistrationApi.md#proxies_id_operations_operation_id_put) | **PUT** /proxies/{id}/operations/{operationId} | Updates an API proxy operation.
[**proxies_id_publish_post**](APIProxyRegistrationApi.md#proxies_id_publish_post) | **POST** /proxies/{id}/publish | Publish the API.
[**proxies_id_put**](APIProxyRegistrationApi.md#proxies_id_put) | **PUT** /proxies/{id} | Updates an API proxy.
[**proxies_id_undeprecate_post**](APIProxyRegistrationApi.md#proxies_id_undeprecate_post) | **POST** /proxies/{id}/undeprecate | Undeprecates the API.
[**proxies_id_unpublish_post**](APIProxyRegistrationApi.md#proxies_id_unpublish_post) | **POST** /proxies/{id}/unpublish | Unpublish the API.
[**proxies_import_from_url_post**](APIProxyRegistrationApi.md#proxies_import_from_url_post) | **POST** /proxies/importFromUrl | Imports a previously exported API.
[**proxies_import_post**](APIProxyRegistrationApi.md#proxies_import_post) | **POST** /proxies/import | Imports a previously exported API.
[**proxies_post**](APIProxyRegistrationApi.md#proxies_post) | **POST** /proxies | Creates a new API proxy from a backend API.
[**proxies_promote_post**](APIProxyRegistrationApi.md#proxies_promote_post) | **POST** /proxies/promote | Invokes the internal API promotion policy for the specified API.
[**proxies_upgrade_id_post**](APIProxyRegistrationApi.md#proxies_upgrade_id_post) | **POST** /proxies/upgrade/{id} | Upgrades an existing frontend API to a newer frontend API.


# **proxies_export_id_get**
> APIPromotion proxies_export_id_get(id, filename)

Downloads an API export.

The API export is produced from [/exportApis](APIProxyRegistration.html#APIProxyRegistrationexportApis).  If __filename__ is supplied, the download will use it as the `Content-Disposition` filename attachment.

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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The export identifier.
filename = 'filename_example' # str | The export will be downloaded using a Content-Dispostion using the supplied filename

try:
    # Downloads an API export.
    api_response = api_instance.proxies_export_id_get(id, filename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_export_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The export identifier. | 
 **filename** | **str**| The export will be downloaded using a Content-Dispostion using the supplied filename | 

### Return type

[**APIPromotion**](APIPromotion.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_export_post**
> proxies_export_post(id, password, filename)

Creates an API export.

Creates an export for use in promoting the API to a new environment.  The export contains the frontend [VirtualizedAPI](VirtualizedAPI.html), their settings, and all backend [APIDefinition](APIDefinition.html) that are required for the frontend API.  If **password** is supplied, the exported file will be encrypted with the password.  If successful, returns **201 Created**, and the HTTP `Location` header contain the of the URL of the export. The export is temporary, and may only be downloaded once.

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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
id = ['id_example'] # list[str] | The frontend API identifier(s) to export.
password = 'password_example' # str | Encrypts the list of API using the password.
filename = 'filename_example' # str | Optional filename to use in response.

try:
    # Creates an API export.
    api_instance.proxies_export_post(id, password, filename)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_export_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)| The frontend API identifier(s) to export. | 
 **password** | **str**| Encrypts the list of API using the password. | 
 **filename** | **str**| Optional filename to use in response. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_get**
> list[VirtualizedAPI] proxies_get(field=field, op=op, value=value)

Queries a list of frontend API.

Returns a list of API that are visible to the authenticated user.  The list of API can be filtered using the expression: field=__field__&op=__op__&value=__value__.  Optionally, you can add a logical operation for all expressions, using the form: &lop=AND|OR.  By default, the logical operation is AND.  Multiple expression filters can be used, specifying field, op, and value for each filter. The __field__ is one of:  name :      The name of the API  apiid :      Matches the API if the API is virtualized from the specified backend API  createdOn :      The date the user was created on, time in ms, e.g.: 1372755998542  deprecated :      The deprecated state of the API, one of: true or false  retired :      The retired state of the API, one of: true or false  state :      The API's state, one of: unpublished, pending, or published  The __op__ is an operation and is one of:  eq :      Equal  ne :      Not equal  gt :      Greater than  lt :      Less than  ge :      Greater than or equal  le :      Less than or equal  like :      Like  gete :      Greater than or equal to, and less than or equal to; the __value__ should be a lower-minimum and upper-maximum separated by comma, e.g: value=5,10  The __value__ will be compared against the __field__, according to the supplied __op__. 

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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
field = ['field_example'] # list[str] | Filter field name. (optional)
op = ['op_example'] # list[str] | Filter operation. (optional)
value = ['value_example'] # list[str] | Filter value (optional)

try:
    # Queries a list of frontend API.
    api_response = api_instance.proxies_get(field=field, op=op, value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | [**list[str]**](str.md)| Filter field name. | [optional] 
 **op** | [**list[str]**](str.md)| Filter operation. | [optional] 
 **value** | [**list[str]**](str.md)| Filter value | [optional] 

### Return type

[**list[VirtualizedAPI]**](VirtualizedAPI.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_grantaccess_post**
> proxies_grantaccess_post(action, api_id, grant_org_id, grant_api_id)

Macro function to grant API access.

Function to macro-apply access to selected API.  The access can be granted to organizations or entities having access to specified API. If **action** is _all_orgs_, access will be granted to all organizations; if **action** is _orgs_, access will be granted to the organization(s) specified by **grantOrganizations**; if **action** is _orgs\\_with\\_apis_, access will be granted to the organizations with access to the apis specified by **grantApis**.

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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
action = 'action_example' # str | Grant action to perform. Possible values are: all\\_orgs, orgs, and orgs\\_with\\_apis.
api_id = ['api_id_example'] # list[str] | List of API ID to which access will be granted.
grant_org_id = ['grant_org_id_example'] # list[str] | List of target organization ID to which access to _apiId_ will be granted (action is _orgs_)
grant_api_id = ['grant_api_id_example'] # list[str] | List of API ID to which access to to _apiId_ will be granted (action is _orgs\\_with\\_apis_).

try:
    # Macro function to grant API access.
    api_instance.proxies_grantaccess_post(action, api_id, grant_org_id, grant_api_id)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_grantaccess_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| Grant action to perform. Possible values are: all\\_orgs, orgs, and orgs\\_with\\_apis. | 
 **api_id** | [**list[str]**](str.md)| List of API ID to which access will be granted. | 
 **grant_org_id** | [**list[str]**](str.md)| List of target organization ID to which access to _apiId_ will be granted (action is _orgs_) | 
 **grant_api_id** | [**list[str]**](str.md)| List of API ID to which access to to _apiId_ will be granted (action is _orgs\\_with\\_apis_). | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_id_delete**
> proxies_id_delete(id)

Deletes an API proxy.

Deletes an API proxy, removing all API access in the process.

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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The frontend API identifier.

try:
    # Deletes an API proxy.
    api_instance.proxies_id_delete(id)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The frontend API identifier. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_id_deprecate_post**
> VirtualizedAPI proxies_id_deprecate_post(id, retirement_date=retirement_date)

Deprecates the API.

Only an API Administrator may deprecate an API, and only _published_ API may be deprecated.  When an API is _deprecated_, the API can still be used, but users will be informed that the API has been deprecated.  Optionally, a **retirementDate** may be set which will schedule the API to be automatically retired and removed from use. If specified, the **retirementDate** should be in the ISO-8601 format of yyyy-MM-ddTHH:mm:ssZ (e.g. 2015-01-01T12:00:00Z).

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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The frontend API identifier.
retirement_date = 'retirement_date_example' # str | Optional API retirement date specified in supported ISO-8601 format.  Set to the past to retire immediately. (optional)

try:
    # Deprecates the API.
    api_response = api_instance.proxies_id_deprecate_post(id, retirement_date=retirement_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_id_deprecate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The frontend API identifier. | 
 **retirement_date** | **str**| Optional API retirement date specified in supported ISO-8601 format.  Set to the past to retire immediately. | [optional] 

### Return type

[**VirtualizedAPI**](VirtualizedAPI.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_id_get**
> VirtualizedAPI proxies_id_get(id)

Gets a frontend API by ID.



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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The frontend API identifier.

try:
    # Gets a frontend API by ID.
    api_response = api_instance.proxies_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The frontend API identifier. | 

### Return type

[**VirtualizedAPI**](VirtualizedAPI.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_id_image_get**
> proxies_id_image_get(id)

Gets the image for the API.

Returns the jpeg image associated with the API.

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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The frontend API identifier.

try:
    # Gets the image for the API.
    api_instance.proxies_id_image_get(id)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_id_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The frontend API identifier. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_id_image_post**
> proxies_id_image_post(id, file=file, type=type)

Set the image for the frontend API.

Set the jpeg image to be associated with the API.

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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The frontend API identifier.
file = '/path/to/file.txt' # file |  (optional)
type = 'type_example' # str |  (optional)

try:
    # Set the image for the frontend API.
    api_instance.proxies_id_image_post(id, file=file, type=type)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_id_image_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The frontend API identifier. | 
 **file** | **file**|  | [optional] 
 **type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_id_operations_get**
> list[VirtualizedAPIMethod] proxies_id_operations_get(id)

Gets a list of methods that are avilable to the API proxy.



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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The frontend API identifier.

try:
    # Gets a list of methods that are avilable to the API proxy.
    api_response = api_instance.proxies_id_operations_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_id_operations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The frontend API identifier. | 

### Return type

[**list[VirtualizedAPIMethod]**](VirtualizedAPIMethod.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_id_operations_operation_id_delete**
> proxies_id_operations_operation_id_delete(id, operation_id)

Deletes an API method by ID.



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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The frontend API identifier.
operation_id = 'operation_id_example' # str | The frontend API method identifier.

try:
    # Deletes an API method by ID.
    api_instance.proxies_id_operations_operation_id_delete(id, operation_id)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_id_operations_operation_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The frontend API identifier. | 
 **operation_id** | **str**| The frontend API method identifier. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_id_operations_operation_id_get**
> VirtualizedAPIMethod proxies_id_operations_operation_id_get(id, operation_id)

Gets an API method by ID.



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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The frontend API identifier.
operation_id = 'operation_id_example' # str | The frontend API method identifier.

try:
    # Gets an API method by ID.
    api_response = api_instance.proxies_id_operations_operation_id_get(id, operation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_id_operations_operation_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The frontend API identifier. | 
 **operation_id** | **str**| The frontend API method identifier. | 

### Return type

[**VirtualizedAPIMethod**](VirtualizedAPIMethod.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_id_operations_operation_id_put**
> VirtualizedAPIMethod proxies_id_operations_operation_id_put(id, operation_id, body)

Updates an API proxy operation.



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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The frontend API identifier.
operation_id = 'operation_id_example' # str | The frontend API method identifier.
body = swagger_client.VirtualizedAPIMethod() # VirtualizedAPIMethod | The method to update.

try:
    # Updates an API proxy operation.
    api_response = api_instance.proxies_id_operations_operation_id_put(id, operation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_id_operations_operation_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The frontend API identifier. | 
 **operation_id** | **str**| The frontend API method identifier. | 
 **body** | [**VirtualizedAPIMethod**](VirtualizedAPIMethod.md)| The method to update. | 

### Return type

[**VirtualizedAPIMethod**](VirtualizedAPIMethod.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_id_publish_post**
> VirtualizedAPI proxies_id_publish_post(id, name, vhost)

Publish the API.

If called by an API Administrator, then the API state will be _published_, otherwise the API state will be _pending_, and an email notification will be sent to the API Administrators, notifying them of the event. Optionally, on publishing, a new **name** for the API may be specified.  Similarly, an optional **vhost** may be specified.  The **vhost** is an externally resolvable virtual host from which the API will be accessed.

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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The frontend API identifier.
name = 'name_example' # str | The name on which to publish this API.
vhost = 'vhost_example' # str | The optional virtual host on which to publish this API.

try:
    # Publish the API.
    api_response = api_instance.proxies_id_publish_post(id, name, vhost)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_id_publish_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The frontend API identifier. | 
 **name** | **str**| The name on which to publish this API. | 
 **vhost** | **str**| The optional virtual host on which to publish this API. | 

### Return type

[**VirtualizedAPI**](VirtualizedAPI.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_id_put**
> VirtualizedAPI proxies_id_put(id, body)

Updates an API proxy.



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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The frontend API identifier.
body = swagger_client.VirtualizedAPI() # VirtualizedAPI | The virtualized API to update

try:
    # Updates an API proxy.
    api_response = api_instance.proxies_id_put(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The frontend API identifier. | 
 **body** | [**VirtualizedAPI**](VirtualizedAPI.md)| The virtualized API to update | 

### Return type

[**VirtualizedAPI**](VirtualizedAPI.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_id_undeprecate_post**
> VirtualizedAPI proxies_id_undeprecate_post(id)

Undeprecates the API.

Only an API Administrator may undeprecate an API, and only _published_ API, that are deprecated, may be undeprecated.

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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The frontend API identifier.

try:
    # Undeprecates the API.
    api_response = api_instance.proxies_id_undeprecate_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_id_undeprecate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The frontend API identifier. | 

### Return type

[**VirtualizedAPI**](VirtualizedAPI.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_id_unpublish_post**
> VirtualizedAPI proxies_id_unpublish_post(id)

Unpublish the API.

Only an API Administrator may unpublish an API.  When an API is _unpublished_, all access to the API is revoked from all applications, and all organizations, save the API development organization that owns the API.

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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The frontend API identifier.

try:
    # Unpublish the API.
    api_response = api_instance.proxies_id_unpublish_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_id_unpublish_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The frontend API identifier. | 

### Return type

[**VirtualizedAPI**](VirtualizedAPI.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_import_from_url_post**
> proxies_import_from_url_post(organization_id, url, password)

Imports a previously exported API.

Imports API, previously exported using [/exportApis](APIProxyRegistration.html#APIProxyRegistrationexportApis).  If the API was exported using a password, then the file is encrypted, and a **password** argument must be provided to decrypt.  The import will create  [VirtualizedAPI](VirtualizedAPI.html), their settings, and all backend [APIDefinition](APIDefinition.html) necessary to support the frontend API.  The **url** should be a [data URI scheme](http://en.wikipedia.org/wiki/Data_URI_scheme).

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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
organization_id = 'organization_id_example' # str | The organization identifier.
url = 'url_example' # str | The data URI.
password = 'password_example' # str | Optional password to decrypt the import file.

try:
    # Imports a previously exported API.
    api_instance.proxies_import_from_url_post(organization_id, url, password)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_import_from_url_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The organization identifier. | 
 **url** | **str**| The data URI. | 
 **password** | **str**| Optional password to decrypt the import file. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_import_post**
> proxies_import_post(organization_id, password, file)

Imports a previously exported API.

Imports API, previously exported using [/exportApis](APIProxyRegistration.html#APIProxyRegistrationexportApis).  If the API was exported using a password, then the file is encrypted, and a **password** argument must be provided to decrypt.  The import will create  [VirtualizedAPI](VirtualizedAPI.html), their settings, and all backend [APIDefinition](APIDefinition.html) necessary to support the frontend API.  This method is similar to [/importFromUrl](APIProxyRegistration.html#APIProxyRegistrationimportFromUrl), save that this method supports traditional form-based file upload, using `multipart/form-data`.

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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
organization_id = 'organization_id_example' # str | The organization identifier.
password = 'password_example' # str | Optional password to decrypt the import file.
file = '/path/to/file.txt' # file | The data file to import.

try:
    # Imports a previously exported API.
    api_instance.proxies_import_post(organization_id, password, file)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_import_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The organization identifier. | 
 **password** | **str**| Optional password to decrypt the import file. | 
 **file** | **file**| The data file to import. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_post**
> VirtualizedAPI proxies_post(body)

Creates a new API proxy from a backend API.

The [VirtualizedAPI apiId](VirtualizedAPI.html#apiId) is required.  If creating the APIas an API administrator, the [VirtualizedAPI organizationId](VirtualizedAPI.html#organizationId) must also be specified.

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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
body = swagger_client.VirtualizedAPI() # VirtualizedAPI | The frontend API to create.

try:
    # Creates a new API proxy from a backend API.
    api_response = api_instance.proxies_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VirtualizedAPI**](VirtualizedAPI.md)| The frontend API to create. | 

### Return type

[**VirtualizedAPI**](VirtualizedAPI.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_promote_post**
> proxies_promote_post(api_id)

Invokes the internal API promotion policy for the specified API.

In API Manager, API promotion must first be enabled in Settings. Also, in Policy Studio (Server Settings -> API Manager -> API Promotion) a promotion policy must be selected. By default a sample promotion policy is installed

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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
api_id = ['api_id_example'] # list[str] | The frontend API identifier(s) to promote

try:
    # Invokes the internal API promotion policy for the specified API.
    api_instance.proxies_promote_post(api_id)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_promote_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_id** | [**list[str]**](str.md)| The frontend API identifier(s) to promote | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_upgrade_id_post**
> proxies_upgrade_id_post(id, upgrade_api_id, deprecate, retire, retirement_date)

Upgrades an existing frontend API to a newer frontend API.

During an API lifecycle, it is necessary to upgrade users to use a newer frontend API.  The idea being that the old frontend API should be phased-out, and developers should move their applications to use the newer frontend API. This method assigns all organizations and applications the same access to the new frontend API (identified by **upgradeApiId**) that they have to the old API (identified by **id**). Optionally, the old frontend API may be deprecated or retired using **deprecate**, **retire**, or scheduled to be retired using **retirementDate**. If specified, the **retirementDate** should be in the ISO-8601 format of yyyy-MM-ddTHH:mm:ssZ (e.g. 2015-01-01T12:00:00Z).

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
api_instance = swagger_client.APIProxyRegistrationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
upgrade_api_id = 'upgrade_api_id_example' # str | The id of the frontend API which will be used to upgrade this virtualized API
deprecate = true # bool | Specifies whether or not the API being upgraded should be depreated
retire = true # bool | Specifies whether or not the API being upgraded should be retired
retirement_date = 'retirement_date_example' # str | Specifies the retirement date of the the API being upgraded if its being retired

try:
    # Upgrades an existing frontend API to a newer frontend API.
    api_instance.proxies_upgrade_id_post(id, upgrade_api_id, deprecate, retire, retirement_date)
except ApiException as e:
    print("Exception when calling APIProxyRegistrationApi->proxies_upgrade_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **upgrade_api_id** | **str**| The id of the frontend API which will be used to upgrade this virtualized API | 
 **deprecate** | **bool**| Specifies whether or not the API being upgraded should be depreated | 
 **retire** | **bool**| Specifies whether or not the API being upgraded should be retired | 
 **retirement_date** | **str**| Specifies the retirement date of the the API being upgraded if its being retired | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

