# swagger_client.MigrateApi

All URIs are relative to *https://localhost/api/portal/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**migrate_applications_export_create_post**](MigrateApi.md#migrate_applications_export_create_post) | **POST** /migrate/applications/export/create | Creates a set of export options associated with the current http session
[**migrate_applications_export_download_get**](MigrateApi.md#migrate_applications_export_download_get) | **GET** /migrate/applications/export/download | Exports Application data for migration to other API Gateways
[**migrate_applications_export_json_post**](MigrateApi.md#migrate_applications_export_json_post) | **POST** /migrate/applications/export/json | Creates an export of applications based on the export options posted as a JSON object
[**migrate_applications_export_post**](MigrateApi.md#migrate_applications_export_post) | **POST** /migrate/applications/export | Creates an export of applications based on the export options posted in a form data
[**migrate_applications_import_post**](MigrateApi.md#migrate_applications_import_post) | **POST** /migrate/applications/import | Imports applications to the API Gateway


# **migrate_applications_export_create_post**
> migrate_applications_export_create_post(body)

Creates a set of export options associated with the current http session

Creates a set of export options associated with the current http session. Options include the password used to encrypt the resulting export, export elements: apikeys, oauth & quotas, the filename of the export, and the list of application ids for inclusion in the export. The exported data can be retrieved subsequently with a GET request

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
api_instance = swagger_client.MigrateApi(swagger_client.ApiClient(configuration))
body = swagger_client.ExportOptions() # ExportOptions | The options for creating an application export file

try:
    # Creates a set of export options associated with the current http session
    api_instance.migrate_applications_export_create_post(body)
except ApiException as e:
    print("Exception when calling MigrateApi->migrate_applications_export_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportOptions**](ExportOptions.md)| The options for creating an application export file | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_applications_export_download_get**
> migrate_applications_export_download_get(filename=filename)

Exports Application data for migration to other API Gateways

Retrieves the export options associated with the current user HTTP session and creates a stream or returns the exported data in response body.

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
api_instance = swagger_client.MigrateApi(swagger_client.ApiClient(configuration))
filename = 'filename_example' # str | Optional. If present this method will return an octet stream with an file attachment of the same name (optional)

try:
    # Exports Application data for migration to other API Gateways
    api_instance.migrate_applications_export_download_get(filename=filename)
except ApiException as e:
    print("Exception when calling MigrateApi->migrate_applications_export_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Optional. If present this method will return an octet stream with an file attachment of the same name | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_applications_export_json_post**
> migrate_applications_export_json_post(body)

Creates an export of applications based on the export options posted as a JSON object

Creates an export file based on options including the password used to encrypt the resulting export, export elements: apikeys, oauth & quotas, the filename of the export, and the list of application ids for inclusion in the export. The exported data is returned as part of the response body

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
api_instance = swagger_client.MigrateApi(swagger_client.ApiClient(configuration))
body = swagger_client.ExportOptions() # ExportOptions | Export options

try:
    # Creates an export of applications based on the export options posted as a JSON object
    api_instance.migrate_applications_export_json_post(body)
except ApiException as e:
    print("Exception when calling MigrateApi->migrate_applications_export_json_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportOptions**](ExportOptions.md)| Export options | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_applications_export_post**
> migrate_applications_export_post(apikeys, oauth, quota, filename=filename, password=password, app_ids=app_ids)

Creates an export of applications based on the export options posted in a form data

Creates an export file based on options including the password used to encrypt the resulting export, export elements: apikeys, oauth & quotas, the filename of the export, and the list of application ids for inclusion in the export. The exported data is returned as part of the response body

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
api_instance = swagger_client.MigrateApi(swagger_client.ApiClient(configuration))
apikeys = 'apikeys_example' # str | True/False. Include/Exclude api keys
oauth = 'oauth_example' # str | True/False. Include/Exclude oauth credentials
quota = 'quota_example' # str | True/False. Include/Exclude quotas, if available
filename = 'filename_example' # str | The name of the export file (optional)
password = 'password_example' # str | The password used to encrypt the exported file (optional)
app_ids = ['app_ids_example'] # list[str] | The list of identifiers for the applications to be exported (optional)

try:
    # Creates an export of applications based on the export options posted in a form data
    api_instance.migrate_applications_export_post(apikeys, oauth, quota, filename=filename, password=password, app_ids=app_ids)
except ApiException as e:
    print("Exception when calling MigrateApi->migrate_applications_export_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikeys** | **str**| True/False. Include/Exclude api keys | 
 **oauth** | **str**| True/False. Include/Exclude oauth credentials | 
 **quota** | **str**| True/False. Include/Exclude quotas, if available | 
 **filename** | **str**| The name of the export file | [optional] 
 **password** | **str**| The password used to encrypt the exported file | [optional] 
 **app_ids** | [**list[str]**](str.md)| The list of identifiers for the applications to be exported | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_applications_import_post**
> migrate_applications_import_post(file, organization_id, user_id, type, password=password)

Imports applications to the API Gateway

Imports a set of applications and assocated API Keys and OAuth credentials, encrypted files require a decryption password

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
api_instance = swagger_client.MigrateApi(swagger_client.ApiClient(configuration))
file = '/path/to/file.txt' # file | The file containing application data to be imported
organization_id = 'organization_id_example' # str | The Organization to associate the imported applications with. If applicable, for Core OAuth this parameter will be ignored
user_id = 'user_id_example' # str | The user to associate the applications with. Default is the API Admin
type = 'type_example' # str | This value should be unset
password = 'password_example' # str | Password to be used for decryption (optional)

try:
    # Imports applications to the API Gateway
    api_instance.migrate_applications_import_post(file, organization_id, user_id, type, password=password)
except ApiException as e:
    print("Exception when calling MigrateApi->migrate_applications_import_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| The file containing application data to be imported | 
 **organization_id** | **str**| The Organization to associate the imported applications with. If applicable, for Core OAuth this parameter will be ignored | 
 **user_id** | **str**| The user to associate the applications with. Default is the API Admin | 
 **type** | **str**| This value should be unset | 
 **password** | **str**| Password to be used for decryption | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

