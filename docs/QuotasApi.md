# swagger_client.QuotasApi

All URIs are relative to *https://localhost/api/portal/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotas_get**](QuotasApi.md#quotas_get) | **GET** /quotas | Returns all quotas
[**quotas_id_delete**](QuotasApi.md#quotas_id_delete) | **DELETE** /quotas/{id} | Deletes a quota
[**quotas_id_get**](QuotasApi.md#quotas_id_get) | **GET** /quotas/{id} | Returns the quota with the given ID
[**quotas_id_put**](QuotasApi.md#quotas_id_put) | **PUT** /quotas/{id} | Updates a quota
[**quotas_post**](QuotasApi.md#quotas_post) | **POST** /quotas | Creates a new quota


# **quotas_get**
> list[QuotaDTO] quotas_get()

Returns all quotas

This method may be called by any member of the Portal, however only the API Administrator may retrieve the system quota.

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
api_instance = swagger_client.QuotasApi(swagger_client.ApiClient(configuration))

try:
    # Returns all quotas
    api_response = api_instance.quotas_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotasApi->quotas_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[QuotaDTO]**](QuotaDTO.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotas_id_delete**
> quotas_id_delete(id)

Deletes a quota

Deletes a quota.  Only API Administrators may update quotas.  Default system and application quotas may not be deleted.

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
api_instance = swagger_client.QuotasApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The quota ID to delete.

try:
    # Deletes a quota
    api_instance.quotas_id_delete(id)
except ApiException as e:
    print("Exception when calling QuotasApi->quotas_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The quota ID to delete. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotas_id_get**
> QuotaDTO quotas_id_get(id)

Returns the quota with the given ID

Returns a quota.  This method may be called by any member of the Portal, however, only API Administrators may retrieve the system quota.

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
api_instance = swagger_client.QuotasApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The quota ID to retrieve.

try:
    # Returns the quota with the given ID
    api_response = api_instance.quotas_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotasApi->quotas_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The quota ID to retrieve. | 

### Return type

[**QuotaDTO**](QuotaDTO.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotas_id_put**
> QuotaDTO quotas_id_put(id, body=body)

Updates a quota

Updates an existing quota. Only API Administrators may update quotas.

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
api_instance = swagger_client.QuotasApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
body = swagger_client.QuotaDTO() # QuotaDTO |  (optional)

try:
    # Updates a quota
    api_response = api_instance.quotas_id_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotasApi->quotas_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**QuotaDTO**](QuotaDTO.md)|  | [optional] 

### Return type

[**QuotaDTO**](QuotaDTO.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotas_post**
> QuotaDTO quotas_post(body=body)

Creates a new quota

Creates a new quota.  Only API Administrators may create quotas.

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
api_instance = swagger_client.QuotasApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuotaDTO() # QuotaDTO |  (optional)

try:
    # Creates a new quota
    api_response = api_instance.quotas_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotasApi->quotas_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuotaDTO**](QuotaDTO.md)|  | [optional] 

### Return type

[**QuotaDTO**](QuotaDTO.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

