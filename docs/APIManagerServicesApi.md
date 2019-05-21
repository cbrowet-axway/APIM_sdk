# swagger_client.APIManagerServicesApi

All URIs are relative to *https://localhost/api/portal/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alerts_get**](APIManagerServicesApi.md#alerts_get) | **GET** /alerts | Gets the alerts configured for the API Manager
[**alerts_post**](APIManagerServicesApi.md#alerts_post) | **POST** /alerts | Updates the API Manager alerts configuration
[**appinfo_get**](APIManagerServicesApi.md#appinfo_get) | **GET** /appinfo | Gets API Manager feature information.
[**certinfo_post**](APIManagerServicesApi.md#certinfo_post) | **POST** /certinfo | Extracts certificate information from the supplied data
[**config_customproperties_get**](APIManagerServicesApi.md#config_customproperties_get) | **GET** /config/customproperties | Gets API Manager custom property metadata
[**config_get**](APIManagerServicesApi.md#config_get) | **GET** /config | Gets API Manager configuration
[**config_put**](APIManagerServicesApi.md#config_put) | **PUT** /config | Updates the API Manager configuration
[**connectors_connector_id_get**](APIManagerServicesApi.md#connectors_connector_id_get) | **GET** /connectors/{connectorId} | Return a list of APIs for the specified connector
[**connectors_connector_id_login_post**](APIManagerServicesApi.md#connectors_connector_id_login_post) | **POST** /connectors/{connectorId}/login | Login to an external service from which APIs will be imported
[**connectors_get**](APIManagerServicesApi.md#connectors_get) | **GET** /connectors | Return a list of API connectors
[**filedata_post**](APIManagerServicesApi.md#filedata_post) | **POST** /filedata | Returns the DataURI representation of the uploaded file
[**license_get**](APIManagerServicesApi.md#license_get) | **GET** /license | Checks that the API Manager has a valid license
[**listeners_get**](APIManagerServicesApi.md#listeners_get) | **GET** /listeners | Gets the API Manager listeners
[**oauthclientprofiles_get**](APIManagerServicesApi.md#oauthclientprofiles_get) | **GET** /oauthclientprofiles | Get a list of OAuth profiles for use in backend API authorisation
[**policies_get**](APIManagerServicesApi.md#policies_get) | **GET** /policies | Gets a list of the specified policies
[**remotehosts_get**](APIManagerServicesApi.md#remotehosts_get) | **GET** /remotehosts | Returns a list of remote hosts
[**remotehosts_id_delete**](APIManagerServicesApi.md#remotehosts_id_delete) | **DELETE** /remotehosts/{id} | Deletes a remote host.
[**remotehosts_id_put**](APIManagerServicesApi.md#remotehosts_id_put) | **PUT** /remotehosts/{id} | Updates a remote host
[**remotehosts_post**](APIManagerServicesApi.md#remotehosts_post) | **POST** /remotehosts | Creates a new remote host
[**service_discovery_instance_type_post**](APIManagerServicesApi.md#service_discovery_instance_type_post) | **POST** /service-discovery/{instance}/{type} | Returns a list of services hosted on the specified Gateway instance
[**sysconfig_get**](APIManagerServicesApi.md#sysconfig_get) | **GET** /sysconfig | Gets API Manager system configuration
[**sysconfig_put**](APIManagerServicesApi.md#sysconfig_put) | **PUT** /sysconfig | Update API Manager system configuration
[**title_get**](APIManagerServicesApi.md#title_get) | **GET** /title | Gets the API Manager&#39;s title
[**tokenstores_get**](APIManagerServicesApi.md#tokenstores_get) | **GET** /tokenstores | Gets a list of Token Stores
[**topology_post**](APIManagerServicesApi.md#topology_post) | **POST** /topology | Retrieves the Topology from the specified Admin Node Manager


# **alerts_get**
> AlertConfig alerts_get()

Gets the alerts configured for the API Manager

Gets the alerts configured for the API Manager that shows which alerts are enabled/disabled for the application.  Only the API Administrator may call this method.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))

try:
    # Gets the alerts configured for the API Manager
    api_response = api_instance.alerts_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->alerts_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AlertConfig**](AlertConfig.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_post**
> AlertConfig alerts_post(body=body)

Updates the API Manager alerts configuration

Updates the API Manager alerts configuration.  Only the API Administrator may call this method.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.AlertConfig() # AlertConfig |  (optional)

try:
    # Updates the API Manager alerts configuration
    api_response = api_instance.alerts_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->alerts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertConfig**](AlertConfig.md)|  | [optional] 

### Return type

[**AlertConfig**](AlertConfig.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appinfo_get**
> Config appinfo_get()

Gets API Manager feature information.

Returns an API Manager configuration object describing the application.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIManagerServicesApi()

try:
    # Gets API Manager feature information.
    api_response = api_instance.appinfo_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->appinfo_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Config**](Config.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **certinfo_post**
> certinfo_post(username=username, file=file, passphrase=passphrase, inbound=inbound, outbound=outbound)

Extracts certificate information from the supplied data

Extracts certificate information from the supplied data.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))
username = 'username_example' # str |  (optional)
file = '/path/to/file.txt' # file |  (optional)
passphrase = 'passphrase_example' # str |  (optional)
inbound = true # bool |  (optional)
outbound = true # bool |  (optional)

try:
    # Extracts certificate information from the supplied data
    api_instance.certinfo_post(username=username, file=file, passphrase=passphrase, inbound=inbound, outbound=outbound)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->certinfo_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] 
 **file** | **file**|  | [optional] 
 **passphrase** | **str**|  | [optional] 
 **inbound** | **bool**|  | [optional] 
 **outbound** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_customproperties_get**
> CustomPropertiesConfig config_customproperties_get()

Gets API Manager custom property metadata

Returns an API Manager configuration object containing the metadata for the custom properties defined in the API Manager app.config.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))

try:
    # Gets API Manager custom property metadata
    api_response = api_instance.config_customproperties_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->config_customproperties_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomPropertiesConfig**](CustomPropertiesConfig.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_get**
> Config config_get()

Gets API Manager configuration

Returns an API Manager configuration object.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))

try:
    # Gets API Manager configuration
    api_response = api_instance.config_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->config_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Config**](Config.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_put**
> Config config_put(body=body)

Updates the API Manager configuration

Updates the API Manager configuration.  Only the API Administrator may call this method.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Config() # Config |  (optional)

try:
    # Updates the API Manager configuration
    api_response = api_instance.config_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->config_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Config**](Config.md)|  | [optional] 

### Return type

[**Config**](Config.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_connector_id_get**
> list[dict(str, object)] connectors_connector_id_get(connector_id)

Return a list of APIs for the specified connector

Return a list of APIs for the specified connector.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))
connector_id = 'connector_id_example' # str | ID of the connector for which APIs should be returned. Connector IDs can be retrieved by calling /connectors.

try:
    # Return a list of APIs for the specified connector
    api_response = api_instance.connectors_connector_id_get(connector_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->connectors_connector_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| ID of the connector for which APIs should be returned. Connector IDs can be retrieved by calling /connectors. | 

### Return type

**list[dict(str, object)]**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_connector_id_login_post**
> str connectors_connector_id_login_post(connector_id, username, password)

Login to an external service from which APIs will be imported

Login to an external service from which APIs will be imported.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))
connector_id = 'connector_id_example' # str | ID of the API connector. Connector IDs can be retrieved by calling /connectors.
username = 'username_example' # str | External service username
password = 'password_example' # str | External service password

try:
    # Login to an external service from which APIs will be imported
    api_response = api_instance.connectors_connector_id_login_post(connector_id, username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->connectors_connector_id_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| ID of the API connector. Connector IDs can be retrieved by calling /connectors. | 
 **username** | **str**| External service username | 
 **password** | **str**| External service password | 

### Return type

**str**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_get**
> list[dict(str, object)] connectors_get()

Return a list of API connectors

Return a list of API connectors.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of API connectors
    api_response = api_instance.connectors_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->connectors_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[dict(str, object)]**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filedata_post**
> filedata_post(file=file)

Returns the DataURI representation of the uploaded file

Returns the DataURI representation of the uploaded file.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))
file = '/path/to/file.txt' # file |  (optional)

try:
    # Returns the DataURI representation of the uploaded file
    api_instance.filedata_post(file=file)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->filedata_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_get**
> str license_get()

Checks that the API Manager has a valid license

Returns an API Manager license configuration object.  Does not require authentication.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIManagerServicesApi()

try:
    # Checks that the API Manager has a valid license
    api_response = api_instance.license_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->license_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listeners_get**
> list[PortalTrafficListener] listeners_get()

Gets the API Manager listeners

Returns a list of API Manager listeners.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))

try:
    # Gets the API Manager listeners
    api_response = api_instance.listeners_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->listeners_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PortalTrafficListener]**](PortalTrafficListener.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauthclientprofiles_get**
> list[ReferencedEntity] oauthclientprofiles_get()

Get a list of OAuth profiles for use in backend API authorisation

Return a list of OAuth Client Profiles for use in authorising API access to backend APIs.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))

try:
    # Get a list of OAuth profiles for use in backend API authorisation
    api_response = api_instance.oauthclientprofiles_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->oauthclientprofiles_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ReferencedEntity]**](ReferencedEntity.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_get**
> list[ReferencedEntity] policies_get(type)

Gets a list of the specified policies

Returns the list of policies (of the specified type) that are available to Portal-registered APIs.  __type__ is one of: faulthandler, globalrequest, globalresponse, request, routing, response, promotion, authentication or token-info.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | The type of policy to return. Possible values are: 'faulthandler', 'globalrequest', 'globalresponse', 'request', 'routing', 'response', 'authentication', 'oauthtokeninfo', 'promotion'

try:
    # Gets a list of the specified policies
    api_response = api_instance.policies_get(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->policies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of policy to return. Possible values are: &#39;faulthandler&#39;, &#39;globalrequest&#39;, &#39;globalresponse&#39;, &#39;request&#39;, &#39;routing&#39;, &#39;response&#39;, &#39;authentication&#39;, &#39;oauthtokeninfo&#39;, &#39;promotion&#39; | 

### Return type

[**list[ReferencedEntity]**](ReferencedEntity.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotehosts_get**
> list[RemoteHost] remotehosts_get()

Returns a list of remote hosts

Returns a list of API Manager-registered remote hosts.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))

try:
    # Returns a list of remote hosts
    api_response = api_instance.remotehosts_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->remotehosts_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RemoteHost]**](RemoteHost.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotehosts_id_delete**
> remotehosts_id_delete(id)

Deletes a remote host.

Deletes an API Manager-registered remote host. Dynamically removes the remote host from the API Gateway runtime.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The remote host identifier.

try:
    # Deletes a remote host.
    api_instance.remotehosts_id_delete(id)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->remotehosts_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The remote host identifier. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotehosts_id_put**
> RemoteHost remotehosts_id_put(id, body=body)

Updates a remote host

Updates an API Manager-registered remote host. Dynamically updates the API Gateway runtime so that the new remote host settings are available.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The remote host identifier.
body = swagger_client.RemoteHost() # RemoteHost |  (optional)

try:
    # Updates a remote host
    api_response = api_instance.remotehosts_id_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->remotehosts_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The remote host identifier. | 
 **body** | [**RemoteHost**](RemoteHost.md)|  | [optional] 

### Return type

[**RemoteHost**](RemoteHost.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotehosts_post**
> RemoteHost remotehosts_post(body=body)

Creates a new remote host

Creates a new API Manager-regsitered remote host. Dynamically updates the API Gateway runtime so that the remote host is available.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.RemoteHost() # RemoteHost |  (optional)

try:
    # Creates a new remote host
    api_response = api_instance.remotehosts_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->remotehosts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoteHost**](RemoteHost.md)|  | [optional] 

### Return type

[**RemoteHost**](RemoteHost.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_discovery_instance_type_post**
> list[Swagger] service_discovery_instance_type_post(instance, type, host=host, port=port, username=username, password=password)

Returns a list of services hosted on the specified Gateway instance

Returns a list of services hosted on the specified Gateway instance.  __type__ is one of: rest, wsdl.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))
instance = 'instance_example' # str | 
type = 'type_example' # str | The type of service to return. Possible values are: 'rest', 'wsdl'
host = 'host_example' # str |  (optional)
port = 'port_example' # str |  (optional)
username = 'username_example' # str |  (optional)
password = 'password_example' # str |  (optional)

try:
    # Returns a list of services hosted on the specified Gateway instance
    api_response = api_instance.service_discovery_instance_type_post(instance, type, host=host, port=port, username=username, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->service_discovery_instance_type_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**|  | 
 **type** | **str**| The type of service to return. Possible values are: &#39;rest&#39;, &#39;wsdl&#39; | 
 **host** | **str**|  | [optional] 
 **port** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 
 **password** | **str**|  | [optional] 

### Return type

[**list[Swagger]**](Swagger.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sysconfig_get**
> SystemConfig sysconfig_get()

Gets API Manager system configuration

Returns an API Manager system configuration object.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))

try:
    # Gets API Manager system configuration
    api_response = api_instance.sysconfig_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->sysconfig_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemConfig**](SystemConfig.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sysconfig_put**
> SystemConfig sysconfig_put(body=body)

Update API Manager system configuration

Returns an API Manager system configuration object.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.SystemConfig() # SystemConfig |  (optional)

try:
    # Update API Manager system configuration
    api_response = api_instance.sysconfig_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->sysconfig_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SystemConfig**](SystemConfig.md)|  | [optional] 

### Return type

[**SystemConfig**](SystemConfig.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **title_get**
> str title_get()

Gets the API Manager's title

Returns the API Manager title.  Does not require authentication.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIManagerServicesApi()

try:
    # Gets the API Manager's title
    api_response = api_instance.title_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->title_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokenstores_get**
> list[ReferencedEntity] tokenstores_get()

Gets a list of Token Stores

Returns a list of Token Stores to be used by OAuth Security Devices for inbound security on portal-registered APIs.

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))

try:
    # Gets a list of Token Stores
    api_response = api_instance.tokenstores_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->tokenstores_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ReferencedEntity]**](ReferencedEntity.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topology_post**
> Topology topology_post(host, port, username, password)

Retrieves the Topology from the specified Admin Node Manager

Retrieves the Topology from the specified Admin Node Manager

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
api_instance = swagger_client.APIManagerServicesApi(swagger_client.ApiClient(configuration))
host = 'host_example' # str | The host on which the Admin Node Manager is running
port = 'port_example' # str | The Admin Node Manager management port.
username = 'username_example' # str | Username to use for Admin Node Manager authentication .
password = 'password_example' # str | Password to use for Admin Node Manager authentication.

try:
    # Retrieves the Topology from the specified Admin Node Manager
    api_response = api_instance.topology_post(host, port, username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIManagerServicesApi->topology_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| The host on which the Admin Node Manager is running | 
 **port** | **str**| The Admin Node Manager management port. | 
 **username** | **str**| Username to use for Admin Node Manager authentication . | 
 **password** | **str**| Password to use for Admin Node Manager authentication. | 

### Return type

[**Topology**](Topology.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

