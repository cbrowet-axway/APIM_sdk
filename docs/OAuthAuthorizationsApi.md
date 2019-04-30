# swagger_client.OAuthAuthorizationsApi

All URIs are relative to *https://localhost/api/portal/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorizations_authzid_delete**](OAuthAuthorizationsApi.md#authorizations_authzid_delete) | **DELETE** /authorizations/{authzid} | Delete the OAuth Authorization for the given authorization id.
[**authorizations_get**](OAuthAuthorizationsApi.md#authorizations_get) | **GET** /authorizations | Retrieve all stored OAuth Authorizations for the logged in user.
[**authorizations_owner_subjectid_application_appid_delete**](OAuthAuthorizationsApi.md#authorizations_owner_subjectid_application_appid_delete) | **DELETE** /authorizations/owner/{subjectid}/application/{appid} | 


# **authorizations_authzid_delete**
> authorizations_authzid_delete(authzid)

Delete the OAuth Authorization for the given authorization id.

Admin or Resource Owner task to delete the given authorization id.

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
api_instance = swagger_client.OAuthAuthorizationsApi(swagger_client.ApiClient(configuration))
authzid = 'authzid_example' # str | 

try:
    # Delete the OAuth Authorization for the given authorization id.
    api_instance.authorizations_authzid_delete(authzid)
except ApiException as e:
    print("Exception when calling OAuthAuthorizationsApi->authorizations_authzid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authzid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorizations_get**
> list[Authorization] authorizations_get()

Retrieve all stored OAuth Authorizations for the logged in user.

If user is a member of the admin group then all authorizations are returned. If not, then the logged in user's authorizations are returned.

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
api_instance = swagger_client.OAuthAuthorizationsApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve all stored OAuth Authorizations for the logged in user.
    api_response = api_instance.authorizations_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthAuthorizationsApi->authorizations_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Authorization]**](Authorization.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorizations_owner_subjectid_application_appid_delete**
> authorizations_owner_subjectid_application_appid_delete(subjectid, appid)





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
api_instance = swagger_client.OAuthAuthorizationsApi(swagger_client.ApiClient(configuration))
subjectid = 'subjectid_example' # str | 
appid = 'appid_example' # str | 

try:
    # 
    api_instance.authorizations_owner_subjectid_application_appid_delete(subjectid, appid)
except ApiException as e:
    print("Exception when calling OAuthAuthorizationsApi->authorizations_owner_subjectid_application_appid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subjectid** | **str**|  | 
 **appid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

