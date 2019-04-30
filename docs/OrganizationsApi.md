# swagger_client.OrganizationsApi

All URIs are relative to *https://localhost/api/portal/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_get**](OrganizationsApi.md#organizations_get) | **GET** /organizations | List all organizations
[**organizations_id_apis_api_access_id_delete**](OrganizationsApi.md#organizations_id_apis_api_access_id_delete) | **DELETE** /organizations/{id}/apis/{apiAccessId} | Deletes access to an API for an organization
[**organizations_id_apis_api_access_id_put**](OrganizationsApi.md#organizations_id_apis_api_access_id_put) | **PUT** /organizations/{id}/apis/{apiAccessId} | Updates access to an API for an organization
[**organizations_id_apis_get**](OrganizationsApi.md#organizations_id_apis_get) | **GET** /organizations/{id}/apis | Get the list of approved APIs for the organization
[**organizations_id_apis_post**](OrganizationsApi.md#organizations_id_apis_post) | **POST** /organizations/{id}/apis | Grants access to an API for an organization.
[**organizations_id_delete**](OrganizationsApi.md#organizations_id_delete) | **DELETE** /organizations/{id} | Delete an organization
[**organizations_id_get**](OrganizationsApi.md#organizations_id_get) | **GET** /organizations/{id} | Get an organization
[**organizations_id_image_get**](OrganizationsApi.md#organizations_id_image_get) | **GET** /organizations/{id}/image | Get the image for an organization
[**organizations_id_image_post**](OrganizationsApi.md#organizations_id_image_post) | **POST** /organizations/{id}/image | Set the image for an organization
[**organizations_id_put**](OrganizationsApi.md#organizations_id_put) | **PUT** /organizations/{id} | Update the details of an organization
[**organizations_id_tokens_get**](OrganizationsApi.md#organizations_id_tokens_get) | **GET** /organizations/{id}/tokens | Get registration codes for an organization
[**organizations_id_tokens_post**](OrganizationsApi.md#organizations_id_tokens_post) | **POST** /organizations/{id}/tokens | Create a registration code
[**organizations_id_tokens_token_delete**](OrganizationsApi.md#organizations_id_tokens_token_delete) | **DELETE** /organizations/{id}/tokens/{token} | Delete the registration code
[**organizations_id_tokens_token_get**](OrganizationsApi.md#organizations_id_tokens_token_get) | **GET** /organizations/{id}/tokens/{token} | Get registration code
[**organizations_id_tokens_token_put**](OrganizationsApi.md#organizations_id_tokens_token_put) | **PUT** /organizations/{id}/tokens/{token} | Update a registration code
[**organizations_post**](OrganizationsApi.md#organizations_post) | **POST** /organizations | Creates a new organization


# **organizations_get**
> list[Organization] organizations_get(field=field, op=op, value=value)

List all organizations

Get the list of organizations that are visible to the authenticated user.  Only API Administrators may list all organizations, all other users will see their organization.  The list of organizations can be filtered using the expression: field=__field__&op=__op__&value=__value__.  Optionally, you can add a logical operation for all expressions, using the form: &lop=AND|OR.  By default, the logical operation is AND.  Multiple expression filters can be used, specifying field, op, and value for each filter. The __field__ is one of:  apiid : Matches the organization if the organization is using the API, specified by ID  description : The organization's description  email : The organization's contact email address  enabled :  The enabled state of the organization, one of: enabled, disabled  createdOn : The date the organization was created on, time in ms, e.g.: 1372755998542  name : The name of the organization  phone : The organization's contact phone  The __op__ is an operation and is one of:  eq : Equal  ne : Not equal  gt :  Greater than  lt :  Less than  ge :  Greater than or equal  le :  Less than or equal  like : Like  gete :  Greater than or equal to, and less than or equal to; the __value__ should be a lower-minimum and upper-maximum separated by comma, e.g: value=5,10  The __value__ will be compared against the __field__, according to the supplied __op__. 

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
field = ['field_example'] # list[str] | Filter field name. (optional)
op = ['op_example'] # list[str] | Filter operation. (optional)
value = ['value_example'] # list[str] | Filter value (optional)

try:
    # List all organizations
    api_response = api_instance.organizations_get(field=field, op=op, value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | [**list[str]**](str.md)| Filter field name. | [optional] 
 **op** | [**list[str]**](str.md)| Filter operation. | [optional] 
 **value** | [**list[str]**](str.md)| Filter value | [optional] 

### Return type

[**list[Organization]**](Organization.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_apis_api_access_id_delete**
> APIAccess organizations_id_apis_api_access_id_delete(id, api_access_id)

Deletes access to an API for an organization

Permanently deletes access to an API for an organization.  Deleting API access will also delete API access to any application.

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The organization ID.
api_access_id = 'api_access_id_example' # str | The API access ID.

try:
    # Deletes access to an API for an organization
    api_response = api_instance.organizations_id_apis_api_access_id_delete(id, api_access_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_id_apis_api_access_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The organization ID. | 
 **api_access_id** | **str**| The API access ID. | 

### Return type

[**APIAccess**](APIAccess.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_apis_api_access_id_put**
> APIAccess organizations_id_apis_api_access_id_put(id, api_access_id, body=body)

Updates access to an API for an organization

Updates access to an API for an organization.  Only __enabled__ may be modified, and disabling access will also disable access to all applications that may be using it.

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The organization ID.
api_access_id = 'api_access_id_example' # str | The API access ID.
body = swagger_client.APIAccess() # APIAccess |  (optional)

try:
    # Updates access to an API for an organization
    api_response = api_instance.organizations_id_apis_api_access_id_put(id, api_access_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_id_apis_api_access_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The organization ID. | 
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

# **organizations_id_apis_get**
> APIAccess organizations_id_apis_get(id)

Get the list of approved APIs for the organization

Get the list of aproved APIs for the organization

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The organization ID who's approved APIs are required.

try:
    # Get the list of approved APIs for the organization
    api_response = api_instance.organizations_id_apis_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_id_apis_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The organization ID who&#39;s approved APIs are required. | 

### Return type

[**APIAccess**](APIAccess.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_apis_post**
> APIAccess organizations_id_apis_post(id, body=body)

Grants access to an API for an organization.

Grants access to an API for an organization.  Only the API Admin may call this method.

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The organization ID requesting access to an API.
body = swagger_client.APIAccess() # APIAccess |  (optional)

try:
    # Grants access to an API for an organization.
    api_response = api_instance.organizations_id_apis_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_id_apis_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The organization ID requesting access to an API. | 
 **body** | [**APIAccess**](APIAccess.md)|  | [optional] 

### Return type

[**APIAccess**](APIAccess.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_delete**
> organizations_id_delete(id)

Delete an organization

Deletes an organization. Deleting an organization will result in all users and associated applications being deleted

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The organization ID to delete.

try:
    # Delete an organization
    api_instance.organizations_id_delete(id)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The organization ID to delete. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_get**
> Organization organizations_id_get(id)

Get an organization

Retrieves the details of an organization.

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The organization ID to be returned.

try:
    # Get an organization
    api_response = api_instance.organizations_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The organization ID to be returned. | 

### Return type

[**Organization**](Organization.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_image_get**
> organizations_id_image_get(id)

Get the image for an organization

Returns the jpeg image associated with an organization.

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The organization ID whos image is to be returned

try:
    # Get the image for an organization
    api_instance.organizations_id_image_get(id)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_id_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The organization ID whos image is to be returned | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_image_post**
> organizations_id_image_post(id, file=file, type=type)

Set the image for an organization

Set the jpeg image to be associated with an organization.

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The organization ID whos image is to be set
file = '/path/to/file.txt' # file |  (optional)
type = 'type_example' # str |  (optional)

try:
    # Set the image for an organization
    api_instance.organizations_id_image_post(id, file=file, type=type)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_id_image_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The organization ID whos image is to be set | 
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

# **organizations_id_put**
> Organization organizations_id_put(id, body=body)

Update the details of an organization

Updates an organization.

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The organization ID to update.
body = swagger_client.Organization() # Organization |  (optional)

try:
    # Update the details of an organization
    api_response = api_instance.organizations_id_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The organization ID to update. | 
 **body** | [**Organization**](Organization.md)|  | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_tokens_get**
> list[RegistrationToken] organizations_id_tokens_get(id)

Get registration codes for an organization

Retrieves the registration codes for an organization.

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The organization ID whos tokens are to be returned.

try:
    # Get registration codes for an organization
    api_response = api_instance.organizations_id_tokens_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_id_tokens_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The organization ID whos tokens are to be returned. | 

### Return type

[**list[RegistrationToken]**](RegistrationToken.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_tokens_post**
> RegistrationToken organizations_id_tokens_post(id, body=body)

Create a registration code

Create a registration code for self service onboarding of users to the organization

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The organization ID to be associated with the registration code.
body = swagger_client.RegistrationToken() # RegistrationToken |  (optional)

try:
    # Create a registration code
    api_response = api_instance.organizations_id_tokens_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_id_tokens_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The organization ID to be associated with the registration code. | 
 **body** | [**RegistrationToken**](RegistrationToken.md)|  | [optional] 

### Return type

[**RegistrationToken**](RegistrationToken.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_tokens_token_delete**
> organizations_id_tokens_token_delete(id, token)

Delete the registration code

Delete the registration code.

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The organization ID associated with the registration code.
token = 'token_example' # str | The registration code to be deleted.

try:
    # Delete the registration code
    api_instance.organizations_id_tokens_token_delete(id, token)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_id_tokens_token_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The organization ID associated with the registration code. | 
 **token** | **str**| The registration code to be deleted. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_tokens_token_get**
> list[RegistrationToken] organizations_id_tokens_token_get(id, token)

Get registration code

Retrieves the registration code.

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The organization ID associated with the registration code.
token = 'token_example' # str | The registration code to be returned.

try:
    # Get registration code
    api_response = api_instance.organizations_id_tokens_token_get(id, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_id_tokens_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The organization ID associated with the registration code. | 
 **token** | **str**| The registration code to be returned. | 

### Return type

[**list[RegistrationToken]**](RegistrationToken.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_tokens_token_put**
> RegistrationToken organizations_id_tokens_token_put(id, token, body=body)

Update a registration code

Update a registration code for self service onboarding of users to the organization

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The organization ID to be associated with the registration code.
token = 'token_example' # str | 
body = swagger_client.RegistrationToken() # RegistrationToken |  (optional)

try:
    # Update a registration code
    api_response = api_instance.organizations_id_tokens_token_put(id, token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_id_tokens_token_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The organization ID to be associated with the registration code. | 
 **token** | **str**|  | 
 **body** | [**RegistrationToken**](RegistrationToken.md)|  | [optional] 

### Return type

[**RegistrationToken**](RegistrationToken.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_post**
> Organization organizations_post(body=body)

Creates a new organization

Creates a new organization.  Only API Administrators may create organizations.

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
api_instance = swagger_client.OrganizationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Organization() # Organization |  (optional)

try:
    # Creates a new organization
    api_response = api_instance.organizations_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Organization**](Organization.md)|  | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

