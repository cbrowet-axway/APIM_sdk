# swagger_client.UsersApi

All URIs are relative to *https://localhost/api/portal/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_forgotpassword_post**](UsersApi.md#users_forgotpassword_post) | **POST** /users/forgotpassword | Allows a user to reset their password.
[**users_get**](UsersApi.md#users_get) | **GET** /users | Obtains a list of users
[**users_id_approve_post**](UsersApi.md#users_id_approve_post) | **POST** /users/{id}/approve | Grants approval to a request to create a new user on the system.
[**users_id_changepassword_post**](UsersApi.md#users_id_changepassword_post) | **POST** /users/{id}/changepassword | Updates the password for a given user.
[**users_id_delete**](UsersApi.md#users_id_delete) | **DELETE** /users/{id} | Deletes a user.
[**users_id_get**](UsersApi.md#users_id_get) | **GET** /users/{id} | Retrieves the details for a given user.
[**users_id_image_get**](UsersApi.md#users_id_image_get) | **GET** /users/{id}/image | Get the image for a user
[**users_id_image_post**](UsersApi.md#users_id_image_post) | **POST** /users/{id}/image | Set the image for a user
[**users_id_put**](UsersApi.md#users_id_put) | **PUT** /users/{id} | Updates the details for a given user.
[**users_id_resetpassword_put**](UsersApi.md#users_id_resetpassword_put) | **PUT** /users/{id}/resetpassword | Admin level function to reset the password for a given user.
[**users_post**](UsersApi.md#users_post) | **POST** /users | Admin function to create a new user on the system
[**users_register_post**](UsersApi.md#users_register_post) | **POST** /users/register | Register a new user.
[**users_resetpassword_get**](UsersApi.md#users_resetpassword_get) | **GET** /users/resetpassword | Validates the user [/forgotpassword](#APIUsersforgotUserPassword) password request.
[**users_validateuser_get**](UsersApi.md#users_validateuser_get) | **GET** /users/validateuser | Validates the user [/register](#APIUsersregisterUser) request.


# **users_forgotpassword_post**
> users_forgotpassword_post(email, success=success, failure=failure)

Allows a user to reset their password.

When this method is invoked, an email is sent to the owner of _email_ to verify that they wish for their password to be reset. The owner of _email_ must click on a link to reset the password. The link should direct the user to [/resetpassword](#APIUsersresetForgottenPassword) with appropriate query paremeters. Redirect URLs may be specified for success and failure conditions. If redirect URLs are specified, they must be a known Static File listener configured in the gateway or the request will be rejected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
email = 'email_example' # str | The email address of the user.
success = 'success_example' # str | The redirect success location (e.g. /request-forgotten-pw-success) (optional)
failure = 'failure_example' # str | The redirect failure location (e.g. /request-forgotten-pw-failed) (optional)

try:
    # Allows a user to reset their password.
    api_instance.users_forgotpassword_post(email, success=success, failure=failure)
except ApiException as e:
    print("Exception when calling UsersApi->users_forgotpassword_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email address of the user. | 
 **success** | **str**| The redirect success location (e.g. /request-forgotten-pw-success) | [optional] 
 **failure** | **str**| The redirect failure location (e.g. /request-forgotten-pw-failed) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get**
> list[User] users_get(field=field, op=op, value=value)

Obtains a list of users

Returns a list of users that are visible to the authenticated user.  The list of users can be filtered using the expression: field=__field__&op=__op__&value=__value__.  Optionally, you can add a logical operation for all expressions, using the form: &lop=AND|OR.  By default, the logical operation is AND.  Multiple expression filters can be used, specifying field, op, and value for each filter. The __field__ is one of:  apiid :      Matches the user if the user has explicit access to application(s) that are using the API, specified by ID  appid :      Matches the user if the user has explicit access to the application, specified by ID  description :      The user's description  email :      The user's email address  enabled :      The enabled state of the user, one of: enabled, disabled  createdOn :      The date the user was created on, time in ms, e.g.: 1372755998542  mobile :      The user's mobile phone  name :      The name of the user  loginName :  The login name of the user  orgid :      Matches the user if the user is a member of the organization, specified by ID  phone :      The user's phone  role :      The user's role, one of: user or oadmin  state :      The user's current state, one of: approved, pending  surname :      The surname of the user  The __op__ is an operation and is one of:  eq :      Equal  ne :      Not equal  gt :      Greater than  lt :      Less than  ge :      Greater than or equal  le :      Less than or equal  like :      Like  gete :      Greater than or equal to, and less than or equal to; the __value__ should be a lower-minimum and upper-maximum separated by comma, e.g: value=5,10  The __value__ will be compared against the __field__, according to the supplied __op__. 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
field = ['field_example'] # list[str] | Filter field name. (optional)
op = ['op_example'] # list[str] | Filter operation. (optional)
value = ['value_example'] # list[str] | Filter value (optional)

try:
    # Obtains a list of users
    api_response = api_instance.users_get(field=field, op=op, value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | [**list[str]**](str.md)| Filter field name. | [optional] 
 **op** | [**list[str]**](str.md)| Filter operation. | [optional] 
 **value** | [**list[str]**](str.md)| Filter value | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_approve_post**
> User users_id_approve_post(id)

Grants approval to a request to create a new user on the system.

Approving user must be API Manager Administrator or an Organization Administrator of the user's organization with the correct privileges to approve new user requests.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the user to be approved.

try:
    # Grants approval to a request to create a new user on the system.
    api_response = api_instance.users_id_approve_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_id_approve_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the user to be approved. | 

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_changepassword_post**
> users_id_changepassword_post(id, new_password)

Updates the password for a given user.

The authenticated user must be API Manager Administrator or an Organization Administrator of the user's organization with the correct privileges to invoke this method.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the user being updated.
new_password = 'new_password_example' # str | The new password of the user being updated.

try:
    # Updates the password for a given user.
    api_instance.users_id_changepassword_post(id, new_password)
except ApiException as e:
    print("Exception when calling UsersApi->users_id_changepassword_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the user being updated. | 
 **new_password** | **str**| The new password of the user being updated. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_delete**
> users_id_delete(id)

Deletes a user.

Deletes a user with the given user ID.  All the applications and keys associated with the deleted user remain in the organization and can be managed by the Organization Administrator or the API Administrator.  The API Administrator can delete any user.  The Organization Administrators can only delete users belonging to their organizations..

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The user ID to delete

try:
    # Deletes a user.
    api_instance.users_id_delete(id)
except ApiException as e:
    print("Exception when calling UsersApi->users_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user ID to delete | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_get**
> User users_id_get(id)

Retrieves the details for a given user.

Retrieves user details, given a user ID.  The API Manager Administrator may access all users, otherwise, the user ID must be a member of the authenticated user's own organization.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the user to be retreived.

try:
    # Retrieves the details for a given user.
    api_response = api_instance.users_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the user to be retreived. | 

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_image_get**
> users_id_image_get(id)

Get the image for a user

Returns the jpeg image associated with an user.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The user ID whos image is to be returned

try:
    # Get the image for a user
    api_instance.users_id_image_get(id)
except ApiException as e:
    print("Exception when calling UsersApi->users_id_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user ID whos image is to be returned | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_image_post**
> users_id_image_post(id, file, type)

Set the image for a user

Set the jpeg image to be associated with a user.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The user ID for which an image is to be updated
file = '/path/to/file.txt' # file | The file input data
type = 'type_example' # str | This value should be unset

try:
    # Set the image for a user
    api_instance.users_id_image_post(id, file, type)
except ApiException as e:
    print("Exception when calling UsersApi->users_id_image_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user ID for which an image is to be updated | 
 **file** | **file**| The file input data | 
 **type** | **str**| This value should be unset | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_put**
> User users_id_put(id, body=body)

Updates the details for a given user.

Updates user details, given a user ID.  The API Manager Administrator may update all users, otherwise, the user ID must be a member of the authenticated user's own organization and the authenticated user must be an Organization Administrator.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the user being updated.
body = swagger_client.User() # User |  (optional)

try:
    # Updates the details for a given user.
    api_response = api_instance.users_id_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the user being updated. | 
 **body** | [**User**](User.md)|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_resetpassword_put**
> User users_id_resetpassword_put(id)

Admin level function to reset the password for a given user.

The authenticated user must be API Manager Administrator or an Organization Administrator of the user's organization with the correct privileges to invoke this method.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the user having password reset administratively.

try:
    # Admin level function to reset the password for a given user.
    api_response = api_instance.users_id_resetpassword_put(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_id_resetpassword_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the user having password reset administratively. | 

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> User users_post(body=body)

Admin function to create a new user on the system

Creates a new user on the system.  Only Organization Administrators and API Manager Administrators may create users. Custom properties can be included on create.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.User() # User |  (optional)

try:
    # Admin function to create a new user on the system
    api_response = api_instance.users_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_register_post**
> users_register_post(name, email, password, token=token, success=success, failure=failure)

Register a new user.

Allows a user to register for an account on the system. A validation email request is sent to the provided email address to confirm ownership. The email should contain a link to [/validateuser](#APIUsersvalidateUser) with appropriate parameters. User properties (including custom properties) may be supplied as form parameters. The method will return JSON, but optionally, redirect URLs may be specified for success and failure conditions. If redirect URLs are specified, they must be a known Static File listener configured in the gateway or the request will be rejected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
name = 'name_example' # str | The name of the user to register.
email = 'email_example' # str | The unique email address of the user to register.
password = 'password_example' # str | The password of the user to register.
token = 'token_example' # str | The registration token to use. (optional)
success = 'success_example' # str | The redirect success location (e.g. '/registration-success') (optional)
failure = 'failure_example' # str | The redirect failure location (e.g. '/registration-failed') (optional)

try:
    # Register a new user.
    api_instance.users_register_post(name, email, password, token=token, success=success, failure=failure)
except ApiException as e:
    print("Exception when calling UsersApi->users_register_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the user to register. | 
 **email** | **str**| The unique email address of the user to register. | 
 **password** | **str**| The password of the user to register. | 
 **token** | **str**| The registration token to use. | [optional] 
 **success** | **str**| The redirect success location (e.g. &#39;/registration-success&#39;) | [optional] 
 **failure** | **str**| The redirect failure location (e.g. &#39;/registration-failed&#39;) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_resetpassword_get**
> users_resetpassword_get(email, validator)

Validates the user [/forgotpassword](#APIUsersforgotUserPassword) password request.

User validation code and email address are expected as query string parameters.  When invoked, an email will be sent to the user with their new password.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
email = 'email_example' # str | The email address of the user being validated.
validator = 'validator_example' # str | Validation string for the user entry.

try:
    # Validates the user [/forgotpassword](#APIUsersforgotUserPassword) password request.
    api_instance.users_resetpassword_get(email, validator)
except ApiException as e:
    print("Exception when calling UsersApi->users_resetpassword_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email address of the user being validated. | 
 **validator** | **str**| Validation string for the user entry. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_validateuser_get**
> users_validateuser_get(email, validator)

Validates the user [/register](#APIUsersregisterUser) request.

User validation code and email address are expected as query parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
email = 'email_example' # str | The email address of the user being validated.
validator = 'validator_example' # str | Validation string for the user entry.

try:
    # Validates the user [/register](#APIUsersregisterUser) request.
    api_instance.users_validateuser_get(email, validator)
except ApiException as e:
    print("Exception when calling UsersApi->users_validateuser_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email address of the user being validated. | 
 **validator** | **str**| Validation string for the user entry. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

