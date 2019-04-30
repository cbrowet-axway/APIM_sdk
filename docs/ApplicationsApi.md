# swagger_client.ApplicationsApi

All URIs are relative to *https://localhost/api/portal/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applications_get**](ApplicationsApi.md#applications_get) | **GET** /applications | Get the list of applications
[**applications_id_apikeys_apikeyid_put**](ApplicationsApi.md#applications_id_apikeys_apikeyid_put) | **PUT** /applications/{id}/apikeys/{apikeyid} | Updates an API Key
[**applications_id_apikeys_get**](ApplicationsApi.md#applications_id_apikeys_get) | **GET** /applications/{id}/apikeys | Returns the API Keys associated with an application
[**applications_id_apikeys_key_id_delete**](ApplicationsApi.md#applications_id_apikeys_key_id_delete) | **DELETE** /applications/{id}/apikeys/{keyId} | Delete an API Key
[**applications_id_apikeys_post**](ApplicationsApi.md#applications_id_apikeys_post) | **POST** /applications/{id}/apikeys | Creates a new API Key and secret for the application
[**applications_id_apis_api_access_id_approve_post**](ApplicationsApi.md#applications_id_apis_api_access_id_approve_post) | **POST** /applications/{id}/apis/{apiAccessId}/approve | Creates an API access request to an API for an application.
[**applications_id_apis_api_access_id_delete**](ApplicationsApi.md#applications_id_apis_api_access_id_delete) | **DELETE** /applications/{id}/apis/{apiAccessId} | Deletes access to an API for an application
[**applications_id_apis_api_access_id_put**](ApplicationsApi.md#applications_id_apis_api_access_id_put) | **PUT** /applications/{id}/apis/{apiAccessId} | Updates access to an API for an application
[**applications_id_apis_get**](ApplicationsApi.md#applications_id_apis_get) | **GET** /applications/{id}/apis | Get the list of APIs that the application can access
[**applications_id_apis_post**](ApplicationsApi.md#applications_id_apis_post) | **POST** /applications/{id}/apis | Create a request for an application to access an API.
[**applications_id_approve_post**](ApplicationsApi.md#applications_id_approve_post) | **POST** /applications/{id}/approve | Approves a pending application request
[**applications_id_availablescopes_get**](ApplicationsApi.md#applications_id_availablescopes_get) | **GET** /applications/{id}/availablescopes | Returns the scopes available to an application
[**applications_id_delete**](ApplicationsApi.md#applications_id_delete) | **DELETE** /applications/{id} | Delete an application
[**applications_id_extclients_get**](ApplicationsApi.md#applications_id_extclients_get) | **GET** /applications/{id}/extclients | Returns the external clients associated with an application
[**applications_id_extclients_object_id_delete**](ApplicationsApi.md#applications_id_extclients_object_id_delete) | **DELETE** /applications/{id}/extclients/{objectId} | Delete an external client
[**applications_id_extclients_object_id_put**](ApplicationsApi.md#applications_id_extclients_object_id_put) | **PUT** /applications/{id}/extclients/{objectId} | Updates an external client for the application
[**applications_id_extclients_post**](ApplicationsApi.md#applications_id_extclients_post) | **POST** /applications/{id}/extclients | Maps a new external client to the application
[**applications_id_get**](ApplicationsApi.md#applications_id_get) | **GET** /applications/{id} | Get an application
[**applications_id_image_get**](ApplicationsApi.md#applications_id_image_get) | **GET** /applications/{id}/image | Get the image for an application
[**applications_id_image_post**](ApplicationsApi.md#applications_id_image_post) | **POST** /applications/{id}/image | Adds a JPEG image to an application
[**applications_id_oauth_client_id_put**](ApplicationsApi.md#applications_id_oauth_client_id_put) | **PUT** /applications/{id}/oauth/{clientId} | Updates an OAuth Credential for the application
[**applications_id_oauth_clientid_newsecret_put**](ApplicationsApi.md#applications_id_oauth_clientid_newsecret_put) | **PUT** /applications/{id}/oauth/{clientid}/newsecret | Updates an OAuth Credential for an application by generating a new secret
[**applications_id_oauth_get**](ApplicationsApi.md#applications_id_oauth_get) | **GET** /applications/{id}/oauth | Returns the OAuth Credentials associated with an application
[**applications_id_oauth_oauth_id_delete**](ApplicationsApi.md#applications_id_oauth_oauth_id_delete) | **DELETE** /applications/{id}/oauth/{oauthId} | Delete an OAuth client ID and secret
[**applications_id_oauth_post**](ApplicationsApi.md#applications_id_oauth_post) | **POST** /applications/{id}/oauth | Creates a new OAuth client ID and secret for the application
[**applications_id_oauthresource_get**](ApplicationsApi.md#applications_id_oauthresource_get) | **GET** /applications/{id}/oauthresource | Returns the OAuth protected resources (scopes) associated with an application
[**applications_id_oauthresource_post**](ApplicationsApi.md#applications_id_oauthresource_post) | **POST** /applications/{id}/oauthresource | Adds an OAuth protected resource to an application
[**applications_id_oauthresource_resource_id_delete**](ApplicationsApi.md#applications_id_oauthresource_resource_id_delete) | **DELETE** /applications/{id}/oauthresource/{resourceId} | Remove an OAuth protected resource from an application
[**applications_id_oauthresource_resource_id_put**](ApplicationsApi.md#applications_id_oauthresource_resource_id_put) | **PUT** /applications/{id}/oauthresource/{resourceId} | Updates a protected resource associate with an application, sets enabled to true/false
[**applications_id_permissions_get**](ApplicationsApi.md#applications_id_permissions_get) | **GET** /applications/{id}/permissions | Get the list of permissions.
[**applications_id_permissions_perm_id_delete**](ApplicationsApi.md#applications_id_permissions_perm_id_delete) | **DELETE** /applications/{id}/permissions/{permId} | Remove a permission
[**applications_id_permissions_perm_id_put**](ApplicationsApi.md#applications_id_permissions_perm_id_put) | **PUT** /applications/{id}/permissions/{permId} | Modify a permission
[**applications_id_permissions_post**](ApplicationsApi.md#applications_id_permissions_post) | **POST** /applications/{id}/permissions | Create a new permission.
[**applications_id_put**](ApplicationsApi.md#applications_id_put) | **PUT** /applications/{id} | Update an application
[**applications_id_quota_delete**](ApplicationsApi.md#applications_id_quota_delete) | **DELETE** /applications/{id}/quota | Deletes a quota from an application
[**applications_id_quota_get**](ApplicationsApi.md#applications_id_quota_get) | **GET** /applications/{id}/quota | Returns the quota associated with an application.
[**applications_id_quota_post**](ApplicationsApi.md#applications_id_quota_post) | **POST** /applications/{id}/quota | Creates a new quota constraint for the application
[**applications_id_quota_put**](ApplicationsApi.md#applications_id_quota_put) | **PUT** /applications/{id}/quota | Updates a quota contraint for an application
[**applications_id_scope_get**](ApplicationsApi.md#applications_id_scope_get) | **GET** /applications/{id}/scope | Returns the scopes associated with an application
[**applications_id_scope_post**](ApplicationsApi.md#applications_id_scope_post) | **POST** /applications/{id}/scope | Adds an OAuth protected resource to an application
[**applications_id_scope_scope_id_delete**](ApplicationsApi.md#applications_id_scope_scope_id_delete) | **DELETE** /applications/{id}/scope/{scopeId} | Remove an OAuth protected resource from an application
[**applications_id_scope_scope_id_put**](ApplicationsApi.md#applications_id_scope_scope_id_put) | **PUT** /applications/{id}/scope/{scopeId} | Updates a scope associated with an application, sets default to true/false
[**applications_oauthclient_client_id_get**](ApplicationsApi.md#applications_oauthclient_client_id_get) | **GET** /applications/oauthclient/{clientId} | Get an application associated with an OAuth Client ID
[**applications_post**](ApplicationsApi.md#applications_post) | **POST** /applications | Creates a new application.


# **applications_get**
> list[Application] applications_get(field=field, op=op, value=value)

Get the list of applications

Get the list of applications that are visible to the authenticated user.  The list of applications can be filtered using the expression: field=__field__&op=__op__&value=__value__.  Optionally, you can add a logical operation for all expressions, using the form: &lop=AND|OR.  By default, the logical operation is AND.  Multiple expression filters can be used, specifying field, op, and value for each filter. The __field__ is one of:  apiid : Matches the application if the application is using the API, specified by ID  userid : Matches the application if the user has explicit access to the application, specified by ID  description : The application's description  email : The application's contact email address  enabled :  The enabled state of the application, one of: enabled, disabled  createdOn : The date the application was created on, time in ms, e.g.: 1372755998542  name : The name of the application  orgid : Matches the application if the application is part of the organization, specified by ID  phone : The application's contact phone  state : The application's current state, one of: approved, pending  The __op__ is an operation and is one of:  eq : Equal  ne : Not equal  gt :  Greater than  lt :  Less than  ge :  Greater than or equal  le :  Less than or equal  like : Like  gete :  Greater than or equal to, and less than or equal to; the __value__ should be a lower-minimum and upper-maximum separated by comma, e.g: value=5,10  The __value__ will be compared against the __field__, according to the supplied __op__. 

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
field = ['field_example'] # list[str] | Filter field name. (optional)
op = ['op_example'] # list[str] | Filter operation. (optional)
value = ['value_example'] # list[str] | Filter value (optional)

try:
    # Get the list of applications
    api_response = api_instance.applications_get(field=field, op=op, value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | [**list[str]**](str.md)| Filter field name. | [optional] 
 **op** | [**list[str]**](str.md)| Filter operation. | [optional] 
 **value** | [**list[str]**](str.md)| Filter value | [optional] 

### Return type

[**list[Application]**](Application.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_apikeys_apikeyid_put**
> APIKey applications_id_apikeys_apikeyid_put(id, apikeyid, body=body)

Updates an API Key

Updates the secret, enabled and Cors origin field.  The fields __id__, __createdBy__, __createdOn__ are read only.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application whose API Key is to be updated.
apikeyid = 'apikeyid_example' # str | The ID of the API Key to be updated.
body = swagger_client.APIKey() # APIKey |  (optional)

try:
    # Updates an API Key
    api_response = api_instance.applications_id_apikeys_apikeyid_put(id, apikeyid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_apikeys_apikeyid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application whose API Key is to be updated. | 
 **apikeyid** | **str**| The ID of the API Key to be updated. | 
 **body** | [**APIKey**](APIKey.md)|  | [optional] 

### Return type

[**APIKey**](APIKey.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_apikeys_get**
> list[APIKey] applications_id_apikeys_get(id)

Returns the API Keys associated with an application

Returns the API Keys associated with an application.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application whose API Keys are to be returned.

try:
    # Returns the API Keys associated with an application
    api_response = api_instance.applications_id_apikeys_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_apikeys_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application whose API Keys are to be returned. | 

### Return type

[**list[APIKey]**](APIKey.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_apikeys_key_id_delete**
> applications_id_apikeys_key_id_delete(id, key_id)

Delete an API Key

Deletes an API Key. Deleting an API key means that it will no longer be accepted for application authentication.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The API Key ID to be deleted.
key_id = 'key_id_example' # str | 

try:
    # Delete an API Key
    api_instance.applications_id_apikeys_key_id_delete(id, key_id)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_apikeys_key_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The API Key ID to be deleted. | 
 **key_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_apikeys_post**
> APIKey applications_id_apikeys_post(id, api_key=api_key)

Creates a new API Key and secret for the application

Creates a new API Key and secret for the application.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application requiring an API Key.
api_key = swagger_client.APIKey() # APIKey | The APIKey to create (optional)

try:
    # Creates a new API Key and secret for the application
    api_response = api_instance.applications_id_apikeys_post(id, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_apikeys_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application requiring an API Key. | 
 **api_key** | [**APIKey**](APIKey.md)| The APIKey to create | [optional] 

### Return type

[**APIKey**](APIKey.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_apis_api_access_id_approve_post**
> applications_id_apis_api_access_id_approve_post(id, api_access_id)

Creates an API access request to an API for an application.

Approving user must be API Manager Administrator or an Organization Administrator of the application's organization with the correct privileges to approve API access requests.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The application ID.
api_access_id = 'api_access_id_example' # str | The API access ID.

try:
    # Creates an API access request to an API for an application.
    api_instance.applications_id_apis_api_access_id_approve_post(id, api_access_id)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_apis_api_access_id_approve_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The application ID. | 
 **api_access_id** | **str**| The API access ID. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_apis_api_access_id_delete**
> APIAccess applications_id_apis_api_access_id_delete(id, api_access_id)

Deletes access to an API for an application

Permanently deletes access to an API for an application.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The application ID.
api_access_id = 'api_access_id_example' # str | The API access ID.

try:
    # Deletes access to an API for an application
    api_response = api_instance.applications_id_apis_api_access_id_delete(id, api_access_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_apis_api_access_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The application ID. | 
 **api_access_id** | **str**| The API access ID. | 

### Return type

[**APIAccess**](APIAccess.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_apis_api_access_id_put**
> APIAccess applications_id_apis_api_access_id_put(id, api_access_id, body=body)

Updates access to an API for an application

Updates access to an API for an application.  Only __enabled__ may be modified.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The application ID.
api_access_id = 'api_access_id_example' # str | The API access ID.
body = swagger_client.APIAccess() # APIAccess |  (optional)

try:
    # Updates access to an API for an application
    api_response = api_instance.applications_id_apis_api_access_id_put(id, api_access_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_apis_api_access_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The application ID. | 
 **api_access_id** | **str**| The API access ID. | 
 **body** | [**APIAccess**](APIAccess.md)|  | [optional] 

### Return type

[**APIAccess**](APIAccess.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_apis_get**
> list[APIAccess] applications_id_apis_get(id)

Get the list of APIs that the application can access

Get the list of APIs that the application can access.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The application ID.

try:
    # Get the list of APIs that the application can access
    api_response = api_instance.applications_id_apis_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_apis_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The application ID. | 

### Return type

[**list[APIAccess]**](APIAccess.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_apis_post**
> APIAccess applications_id_apis_post(id, body=body)

Create a request for an application to access an API.

Only API Manager Administrator, or an Organization Administrator of the application's organization with the correct privileges, or the application manager may create API access requests.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The application ID.
body = swagger_client.APIAccess() # APIAccess |  (optional)

try:
    # Create a request for an application to access an API.
    api_response = api_instance.applications_id_apis_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_apis_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The application ID. | 
 **body** | [**APIAccess**](APIAccess.md)|  | [optional] 

### Return type

[**APIAccess**](APIAccess.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_approve_post**
> applications_id_approve_post(id)

Approves a pending application request

Approving user must be API Manager Administrator or an Organization Administrator of the application's organization with the correct privileges to approve new application requests.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The application request ID.

try:
    # Approves a pending application request
    api_instance.applications_id_approve_post(id)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_approve_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The application request ID. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_availablescopes_get**
> list[list[object]] applications_id_availablescopes_get(id, api_scope=api_scope)

Returns the scopes available to an application

Returns the OAuth scopes available to  an application.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application whose OAuth scopes are to be returned.
api_scope = false # bool |  (optional) (default to false)

try:
    # Returns the scopes available to an application
    api_response = api_instance.applications_id_availablescopes_get(id, api_scope=api_scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_availablescopes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application whose OAuth scopes are to be returned. | 
 **api_scope** | **bool**|  | [optional] [default to false]

### Return type

**list[list[object]]**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_delete**
> applications_id_delete(id)

Delete an application

Only managers of the application, API Manager Administrators, or Organization Administrators with enabled delegated application management privileges, may delete applications.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application to delete.

try:
    # Delete an application
    api_instance.applications_id_delete(id)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application to delete. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_extclients_get**
> list[ExternalClient] applications_id_extclients_get(id)

Returns the external clients associated with an application

Returns the external clients associated with an application. External clients are used when authenticating the application through a 3rd party OAuth service

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application whose external clients are to be returned.

try:
    # Returns the external clients associated with an application
    api_response = api_instance.applications_id_extclients_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_extclients_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application whose external clients are to be returned. | 

### Return type

[**list[ExternalClient]**](ExternalClient.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_extclients_object_id_delete**
> applications_id_extclients_object_id_delete(id, object_id)

Delete an external client

Deletes an external client. Deleting a mapping means that it will no longer be accepted for application authentication.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application whose external client is to be deleted.
object_id = 'object_id_example' # str | The ID of the external client entry to be deleted.

try:
    # Delete an external client
    api_instance.applications_id_extclients_object_id_delete(id, object_id)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_extclients_object_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application whose external client is to be deleted. | 
 **object_id** | **str**| The ID of the external client entry to be deleted. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_extclients_object_id_put**
> ExternalClient applications_id_extclients_object_id_put(id, object_id, body=body)

Updates an external client for the application

Updates an external client for the application. External clients are used when authenticating the application through a 3rd party OAuth service

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application whose external client is to be updated.
object_id = 'object_id_example' # str | The external client entry to be updated.
body = swagger_client.ExternalClient() # ExternalClient |  (optional)

try:
    # Updates an external client for the application
    api_response = api_instance.applications_id_extclients_object_id_put(id, object_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_extclients_object_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application whose external client is to be updated. | 
 **object_id** | **str**| The external client entry to be updated. | 
 **body** | [**ExternalClient**](ExternalClient.md)|  | [optional] 

### Return type

[**ExternalClient**](ExternalClient.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_extclients_post**
> ExternalClient applications_id_extclients_post(id, body=body)

Maps a new external client to the application

Maps a new external client to the application. External clients are used when authenticating the application through a 3rd party OAuth service

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application to map to an external client.
body = swagger_client.ExternalClient() # ExternalClient |  (optional)

try:
    # Maps a new external client to the application
    api_response = api_instance.applications_id_extclients_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_extclients_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application to map to an external client. | 
 **body** | [**ExternalClient**](ExternalClient.md)|  | [optional] 

### Return type

[**ExternalClient**](ExternalClient.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_get**
> Application applications_id_get(id)

Get an application

Retrieves the details of an application.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the application to be returned.

try:
    # Get an application
    api_response = api_instance.applications_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the application to be returned. | 

### Return type

[**Application**](Application.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_image_get**
> applications_id_image_get(id)

Get the image for an application

Get the JPEG image associated with an application.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the application whose image is to be return

try:
    # Get the image for an application
    api_instance.applications_id_image_get(id)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the application whose image is to be return | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_image_post**
> applications_id_image_post(id, file, type=type)

Adds a JPEG image to an application

Adds a JPEG image to an application with a MultiPart POST

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the application whose image is being added
file = '/path/to/file.txt' # file | The file uploaded in the POST body as an element in a multipart post
type = 'type_example' # str |  (optional)

try:
    # Adds a JPEG image to an application
    api_instance.applications_id_image_post(id, file, type=type)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_image_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the application whose image is being added | 
 **file** | **file**| The file uploaded in the POST body as an element in a multipart post | 
 **type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_oauth_client_id_put**
> OAuthClient applications_id_oauth_client_id_put(id, client_id, body=body)

Updates an OAuth Credential for the application

Updates an OAuth Credential for the application.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application whose OAuth credential is to be updated.
client_id = 'client_id_example' # str | The OAuth Credential ID to be updated.
body = swagger_client.OAuthClient() # OAuthClient |  (optional)

try:
    # Updates an OAuth Credential for the application
    api_response = api_instance.applications_id_oauth_client_id_put(id, client_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_oauth_client_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application whose OAuth credential is to be updated. | 
 **client_id** | **str**| The OAuth Credential ID to be updated. | 
 **body** | [**OAuthClient**](OAuthClient.md)|  | [optional] 

### Return type

[**OAuthClient**](OAuthClient.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_oauth_clientid_newsecret_put**
> OAuthClient applications_id_oauth_clientid_newsecret_put(id, clientid)

Updates an OAuth Credential for an application by generating a new secret

Updates an OAuth Credential for an application by generating a new client secret.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application whose OAuth credential is to be updated with a new secret
clientid = 'clientid_example' # str | The OAuth Credential ID to be updated with a new secret

try:
    # Updates an OAuth Credential for an application by generating a new secret
    api_response = api_instance.applications_id_oauth_clientid_newsecret_put(id, clientid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_oauth_clientid_newsecret_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application whose OAuth credential is to be updated with a new secret | 
 **clientid** | **str**| The OAuth Credential ID to be updated with a new secret | 

### Return type

[**OAuthClient**](OAuthClient.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_oauth_get**
> list[OAuthClient] applications_id_oauth_get(id)

Returns the OAuth Credentials associated with an application

Returns the OAuth Credentials associated with an application.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application whose OAuth Credentials are to be returned.

try:
    # Returns the OAuth Credentials associated with an application
    api_response = api_instance.applications_id_oauth_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_oauth_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application whose OAuth Credentials are to be returned. | 

### Return type

[**list[OAuthClient]**](OAuthClient.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_oauth_oauth_id_delete**
> applications_id_oauth_oauth_id_delete(id, oauth_id)

Delete an OAuth client ID and secret

Deletes an OAuth client ID and secret. Deleting an OAuth client ID and secret means that it will no longer be accepted for OAuth application authentication.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application whose OAuth Credential is to be deleted.
oauth_id = 'oauth_id_example' # str | The OAuth Client ID to be deleted.

try:
    # Delete an OAuth client ID and secret
    api_instance.applications_id_oauth_oauth_id_delete(id, oauth_id)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_oauth_oauth_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application whose OAuth Credential is to be deleted. | 
 **oauth_id** | **str**| The OAuth Client ID to be deleted. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_oauth_post**
> OAuthClient applications_id_oauth_post(id, body)

Creates a new OAuth client ID and secret for the application

Creates a new OAuth client ID and secret for the application.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application requiring an OAuth client ID and secret.
body = swagger_client.OAuthClient() # OAuthClient | The OAuth credential to create

try:
    # Creates a new OAuth client ID and secret for the application
    api_response = api_instance.applications_id_oauth_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_oauth_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application requiring an OAuth client ID and secret. | 
 **body** | [**OAuthClient**](OAuthClient.md)| The OAuth credential to create | 

### Return type

[**OAuthClient**](OAuthClient.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_oauthresource_get**
> list[OAuthResource] applications_id_oauthresource_get(id)

Returns the OAuth protected resources (scopes) associated with an application

Returns the OAuth protected resources (scopes) associated with an application.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application whose OAuth protected resources (Scopes) are to be returned.

try:
    # Returns the OAuth protected resources (scopes) associated with an application
    api_response = api_instance.applications_id_oauthresource_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_oauthresource_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application whose OAuth protected resources (Scopes) are to be returned. | 

### Return type

[**list[OAuthResource]**](OAuthResource.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_oauthresource_post**
> OAuthResource applications_id_oauthresource_post(id, body)

Adds an OAuth protected resource to an application

An application must define which OAuth Protected resources it wants to access. These resources will define the scope of the application.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application requiring an OAuth protected resource.
body = swagger_client.OAuthResource() # OAuthResource | The OAuth protected resource to add to the application

try:
    # Adds an OAuth protected resource to an application
    api_response = api_instance.applications_id_oauthresource_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_oauthresource_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application requiring an OAuth protected resource. | 
 **body** | [**OAuthResource**](OAuthResource.md)| The OAuth protected resource to add to the application | 

### Return type

[**OAuthResource**](OAuthResource.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_oauthresource_resource_id_delete**
> applications_id_oauthresource_resource_id_delete(id, resource_id)

Remove an OAuth protected resource from an application

Removes the association between an application and an OAuth protected resource on the API Server. The application will no longer have the scope associated with the resource. Tokens issued prior to the removal will still be scoped for the resource.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application whose protected resource is to be removed.
resource_id = 'resource_id_example' # str | The uri of the OAuth protected resource to be disassociated from the application.

try:
    # Remove an OAuth protected resource from an application
    api_instance.applications_id_oauthresource_resource_id_delete(id, resource_id)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_oauthresource_resource_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application whose protected resource is to be removed. | 
 **resource_id** | **str**| The uri of the OAuth protected resource to be disassociated from the application. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_oauthresource_resource_id_put**
> OAuthResource applications_id_oauthresource_resource_id_put(id, resource_id, body)

Updates a protected resource associate with an application, sets enabled to true/false

An OAuth Protected resource associated with an application can be enabled or disabled with this method.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application requiring an updated OAuth protected resource.
resource_id = 'resource_id_example' # str | The ID of the OAuth protected resource to update
body = swagger_client.OAuthResource() # OAuthResource | The updated OAuth protected resource

try:
    # Updates a protected resource associate with an application, sets enabled to true/false
    api_response = api_instance.applications_id_oauthresource_resource_id_put(id, resource_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_oauthresource_resource_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application requiring an updated OAuth protected resource. | 
 **resource_id** | **str**| The ID of the OAuth protected resource to update | 
 **body** | [**OAuthResource**](OAuthResource.md)| The updated OAuth protected resource | 

### Return type

[**OAuthResource**](OAuthResource.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_permissions_get**
> list[PermissionDTO] applications_id_permissions_get(id)

Get the list of permissions.

Get the access-control list (ACL) for the application. Callers with view-only privilege can only access their own permission.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The application ID.

try:
    # Get the list of permissions.
    api_response = api_instance.applications_id_permissions_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_permissions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The application ID. | 

### Return type

[**list[PermissionDTO]**](PermissionDTO.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_permissions_perm_id_delete**
> applications_id_permissions_perm_id_delete(id, perm_id)

Remove a permission

Remove an existing access-control entry from the application's ACL. Management privilege required.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The application ID.
perm_id = 'perm_id_example' # str | The permission ID.

try:
    # Remove a permission
    api_instance.applications_id_permissions_perm_id_delete(id, perm_id)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_permissions_perm_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The application ID. | 
 **perm_id** | **str**| The permission ID. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_permissions_perm_id_put**
> PermissionDTO applications_id_permissions_perm_id_put(id, perm_id, body=body)

Modify a permission

Modify an existing access-control entry from the application's ACL. Management privilege required.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The application ID.
perm_id = 'perm_id_example' # str | The permission ID.
body = swagger_client.PermissionDTO() # PermissionDTO |  (optional)

try:
    # Modify a permission
    api_response = api_instance.applications_id_permissions_perm_id_put(id, perm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_permissions_perm_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The application ID. | 
 **perm_id** | **str**| The permission ID. | 
 **body** | [**PermissionDTO**](PermissionDTO.md)|  | [optional] 

### Return type

[**PermissionDTO**](PermissionDTO.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_permissions_post**
> PermissionDTO applications_id_permissions_post(id, body=body)

Create a new permission.

Add a new access-control entry to the application's ACL. Management privilege required.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The application ID.
body = swagger_client.PermissionDTO() # PermissionDTO |  (optional)

try:
    # Create a new permission.
    api_response = api_instance.applications_id_permissions_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_permissions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The application ID. | 
 **body** | [**PermissionDTO**](PermissionDTO.md)|  | [optional] 

### Return type

[**PermissionDTO**](PermissionDTO.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_put**
> Application applications_id_put(id, body=body)

Update an application

Only managers of the application, API Manager Administrators, or Organization Administrators with enabled delegated application management privileges, may update an application. Note, if a field is omitted from the payload, or its value is set to null, the existing value for this field will be retained.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the application to be updated
body = swagger_client.Application() # Application |  (optional)

try:
    # Update an application
    api_response = api_instance.applications_id_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the application to be updated | 
 **body** | [**Application**](Application.md)|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_quota_delete**
> applications_id_quota_delete(id)

Deletes a quota from an application

Deletes a quota from an application

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application who's quota constraint is to be deleted.

try:
    # Deletes a quota from an application
    api_instance.applications_id_quota_delete(id)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_quota_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application who&#39;s quota constraint is to be deleted. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_quota_get**
> list[QuotaDTO] applications_id_quota_get(id)

Returns the quota associated with an application.

Returns the quota associated with an application.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application who's quota constraints are to be returned.

try:
    # Returns the quota associated with an application.
    api_response = api_instance.applications_id_quota_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_quota_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application who&#39;s quota constraints are to be returned. | 

### Return type

[**list[QuotaDTO]**](QuotaDTO.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_quota_post**
> QuotaDTO applications_id_quota_post(id, body=body)

Creates a new quota constraint for the application

Creates a new quota constraint for the application.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application for the quota contraint.
body = swagger_client.QuotaDTO() # QuotaDTO |  (optional)

try:
    # Creates a new quota constraint for the application
    api_response = api_instance.applications_id_quota_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_quota_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application for the quota contraint. | 
 **body** | [**QuotaDTO**](QuotaDTO.md)|  | [optional] 

### Return type

[**QuotaDTO**](QuotaDTO.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_quota_put**
> QuotaDTO applications_id_quota_put(id, body=body)

Updates a quota contraint for an application

Updates a quota contraint for the given application.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application who's quota is to be updated.
body = swagger_client.QuotaDTO() # QuotaDTO |  (optional)

try:
    # Updates a quota contraint for an application
    api_response = api_instance.applications_id_quota_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_quota_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application who&#39;s quota is to be updated. | 
 **body** | [**QuotaDTO**](QuotaDTO.md)|  | [optional] 

### Return type

[**QuotaDTO**](QuotaDTO.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_scope_get**
> list[list[object]] applications_id_scope_get(id)

Returns the scopes associated with an application

Returns the OAuth scopes associated with an application.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application whose OAuth protected resources (Scopes) are to be returned.

try:
    # Returns the scopes associated with an application
    api_response = api_instance.applications_id_scope_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_scope_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application whose OAuth protected resources (Scopes) are to be returned. | 

### Return type

**list[list[object]]**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_scope_post**
> OAuthAppScope applications_id_scope_post(id, body)

Adds an OAuth protected resource to an application

An application must define which scopes it wants to access. These define the scope of the application.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application requiring an OAuth scope.
body = swagger_client.OAuthAppScope() # OAuthAppScope | The OAuth Scope to add to the application

try:
    # Adds an OAuth protected resource to an application
    api_response = api_instance.applications_id_scope_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_scope_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application requiring an OAuth scope. | 
 **body** | [**OAuthAppScope**](OAuthAppScope.md)| The OAuth Scope to add to the application | 

### Return type

[**OAuthAppScope**](OAuthAppScope.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_scope_scope_id_delete**
> applications_id_scope_scope_id_delete(id, scope_id)

Remove an OAuth protected resource from an application

Removes the association between an application and an OAuth protected resource on the API Server. The application will no longer have the scope associated with the resource. Tokens issued prior to the removal will still be scoped for the resource.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application whose protected resource is to be removed.
scope_id = 'scope_id_example' # str | The id of the Scope to be disassociated from the application.

try:
    # Remove an OAuth protected resource from an application
    api_instance.applications_id_scope_scope_id_delete(id, scope_id)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_scope_scope_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application whose protected resource is to be removed. | 
 **scope_id** | **str**| The id of the Scope to be disassociated from the application. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_scope_scope_id_put**
> OAuthAppScope applications_id_scope_scope_id_put(id, scope_id, body)

Updates a scope associated with an application, sets default to true/false

An OAuth Scope associated with an application can be set or unset as a default scope with this method.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of application requiring an updated OAuth protected resource.
scope_id = 'scope_id_example' # str | The ID of the Application Scope to update
body = swagger_client.OAuthAppScope() # OAuthAppScope | The updated OAuth protected resource

try:
    # Updates a scope associated with an application, sets default to true/false
    api_response = api_instance.applications_id_scope_scope_id_put(id, scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_id_scope_scope_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of application requiring an updated OAuth protected resource. | 
 **scope_id** | **str**| The ID of the Application Scope to update | 
 **body** | [**OAuthAppScope**](OAuthAppScope.md)| The updated OAuth protected resource | 

### Return type

[**OAuthAppScope**](OAuthAppScope.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_oauthclient_client_id_get**
> Application applications_oauthclient_client_id_get(client_id)

Get an application associated with an OAuth Client ID

Retrieves the application associated with an OAuth Client ID

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
client_id = 'client_id_example' # str | The OAuth Client ID associated with the Application.

try:
    # Get an application associated with an OAuth Client ID
    api_response = api_instance.applications_oauthclient_client_id_get(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_oauthclient_client_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The OAuth Client ID associated with the Application. | 

### Return type

[**Application**](Application.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_post**
> Application applications_post(body=body)

Creates a new application.

Creates a new application.  New applications may need to be approved using [/approve](#APIApplicationsapproveApp).

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApplicationRequest() # ApplicationRequest |  (optional)

try:
    # Creates a new application.
    api_response = api_instance.applications_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationRequest**](ApplicationRequest.md)|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

