# swagger_client.CurrentUserApi

All URIs are relative to *https://localhost/api/portal/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currentuser_changepassword_post**](CurrentUserApi.md#currentuser_changepassword_post) | **POST** /currentuser/changepassword | Modify the current user&#39;s password
[**currentuser_get**](CurrentUserApi.md#currentuser_get) | **GET** /currentuser | Get the current user
[**currentuser_put**](CurrentUserApi.md#currentuser_put) | **PUT** /currentuser | Modify the current user


# **currentuser_changepassword_post**
> currentuser_changepassword_post(old_password, new_password)

Modify the current user's password

Modify the password of the authenticated user

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
api_instance = swagger_client.CurrentUserApi(swagger_client.ApiClient(configuration))
old_password = 'old_password_example' # str | The user's old password
new_password = 'new_password_example' # str | The user's new password

try:
    # Modify the current user's password
    api_instance.currentuser_changepassword_post(old_password, new_password)
except ApiException as e:
    print("Exception when calling CurrentUserApi->currentuser_changepassword_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **old_password** | **str**| The user&#39;s old password | 
 **new_password** | **str**| The user&#39;s new password | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currentuser_get**
> User currentuser_get()

Get the current user

Get the account details of the authenticated user

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
api_instance = swagger_client.CurrentUserApi(swagger_client.ApiClient(configuration))

try:
    # Get the current user
    api_response = api_instance.currentuser_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrentUserApi->currentuser_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currentuser_put**
> User currentuser_put(body=body)

Modify the current user

Modify the account details of the authenticated user

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
api_instance = swagger_client.CurrentUserApi(swagger_client.ApiClient(configuration))
body = swagger_client.User() # User |  (optional)

try:
    # Modify the current user
    api_response = api_instance.currentuser_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrentUserApi->currentuser_put: %s\n" % e)
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

