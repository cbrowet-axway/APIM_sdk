# swagger_client.LoginApi

All URIs are relative to *https://localhost/api/portal/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_delete**](LoginApi.md#login_delete) | **DELETE** /login | Logout from API Manager
[**login_post**](LoginApi.md#login_post) | **POST** /login | Login to API Manager


# **login_delete**
> login_delete()

Logout from API Manager

Destroys the caller session with the API Manager.

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
api_instance = swagger_client.LoginApi(swagger_client.ApiClient(configuration))

try:
    # Logout from API Manager
    api_instance.login_delete()
except ApiException as e:
    print("Exception when calling LoginApi->login_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_post**
> login_post(username, password, success=success, failure=failure)

Login to API Manager

Logs a user, identified by _username_ and _password_, into the API Manager by creating unique a session cookie.  The _success_ parameter defaults to a named URL identified by \"/home\" and will return a redirect to the portal after login.  The _failure_ parameter is optional.  If _failure_ is not specified, and the login attempt fails, this method returns a JSON error response.  If _failure_ is specified, and the login attempt fails, then this method will redirect to a named URL, identified by \"/login-failed\".

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoginApi()
username = 'username_example' # str | The login name of the authenticating user
password = 'password_example' # str | The password of the authenticating user
success = 'success_example' # str | The redirect success location (defaults to: /home) (optional)
failure = 'failure_example' # str | Optional redirect failure location (e.g. /login-failed (optional)

try:
    # Login to API Manager
    api_instance.login_post(username, password, success=success, failure=failure)
except ApiException as e:
    print("Exception when calling LoginApi->login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The login name of the authenticating user | 
 **password** | **str**| The password of the authenticating user | 
 **success** | **str**| The redirect success location (defaults to: /home) | [optional] 
 **failure** | **str**| Optional redirect failure location (e.g. /login-failed | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

