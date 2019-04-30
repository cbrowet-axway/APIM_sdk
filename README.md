# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.3.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = swagger_client.APIDiscoveryApi(swagger_client.ApiClient(configuration))

try:
    # Lists all APIs/services virtualised in the API Server.
    api_response = api_instance.discovery_apis_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIDiscoveryApi->discovery_apis_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost/api/portal/v1.3*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APIDiscoveryApi* | [**discovery_apis_get**](docs/APIDiscoveryApi.md#discovery_apis_get) | **GET** /discovery/apis | Lists all APIs/services virtualised in the API Server.
*APIDiscoveryApi* | [**discovery_oauthresources_get**](docs/APIDiscoveryApi.md#discovery_oauthresources_get) | **GET** /discovery/oauthresources | Gets a list OAuth protected resources and their associated scopes.
*APIDiscoveryApi* | [**discovery_scopes_get**](docs/APIDiscoveryApi.md#discovery_scopes_get) | **GET** /discovery/scopes | Retrieves every resource on the API Server that is protected by OAuth, and the scopes that cover those resources
*APIDiscoveryApi* | [**discovery_sdk_id_platform_get**](docs/APIDiscoveryApi.md#discovery_sdk_id_platform_get) | **GET** /discovery/sdk/{id}/{platform} | Generates an SDK package for the specified API based on the type of the client requested
*APIDiscoveryApi* | [**discovery_swagger_api_id_id_get**](docs/APIDiscoveryApi.md#discovery_swagger_api_id_id_get) | **GET** /discovery/swagger/api/id/{id} | Retrieves an extended Swagger feed for the specified API.
*APIDiscoveryApi* | [**discovery_swagger_api_name_get**](docs/APIDiscoveryApi.md#discovery_swagger_api_name_get) | **GET** /discovery/swagger/api/{name} | Retrieves an extended Swagger feed for the specified API.
*APIDiscoveryApi* | [**discovery_swagger_apis_get**](docs/APIDiscoveryApi.md#discovery_swagger_apis_get) | **GET** /discovery/swagger/apis | Convenience method for retrieving all Swagger feeds for all virtualised services.
*APIDiscoveryApi* | [**discovery_swagger_apis_id_image_get**](docs/APIDiscoveryApi.md#discovery_swagger_apis_id_image_get) | **GET** /discovery/swagger/apis/{id}/image | Retrieves the API image
*APIDiscoveryApi* | [**discovery_swagger_apis_id_service_definition_get**](docs/APIDiscoveryApi.md#discovery_swagger_apis_id_service_definition_get) | **GET** /discovery/swagger/apis/{id}/service-definition | Retrieves the service definition of the API. 
*APIManagerServicesApi* | [**alerts_get**](docs/APIManagerServicesApi.md#alerts_get) | **GET** /alerts | Gets the alerts configured for the API Manager
*APIManagerServicesApi* | [**alerts_post**](docs/APIManagerServicesApi.md#alerts_post) | **POST** /alerts | Updates the API Manager alerts configuration
*APIManagerServicesApi* | [**appinfo_get**](docs/APIManagerServicesApi.md#appinfo_get) | **GET** /appinfo | Gets API Manager feature information.
*APIManagerServicesApi* | [**certinfo_post**](docs/APIManagerServicesApi.md#certinfo_post) | **POST** /certinfo | Extracts certificate information from the supplied data
*APIManagerServicesApi* | [**config_get**](docs/APIManagerServicesApi.md#config_get) | **GET** /config | Gets API Manager configuration
*APIManagerServicesApi* | [**config_put**](docs/APIManagerServicesApi.md#config_put) | **PUT** /config | Updates the API Manager configuration
*APIManagerServicesApi* | [**connectors_connector_id_get**](docs/APIManagerServicesApi.md#connectors_connector_id_get) | **GET** /connectors/{connectorId} | Return a list of APIs for the specified connector
*APIManagerServicesApi* | [**connectors_connector_id_login_post**](docs/APIManagerServicesApi.md#connectors_connector_id_login_post) | **POST** /connectors/{connectorId}/login | Login to an external service from which APIs will be imported
*APIManagerServicesApi* | [**connectors_get**](docs/APIManagerServicesApi.md#connectors_get) | **GET** /connectors | Return a list of API connectors
*APIManagerServicesApi* | [**filedata_post**](docs/APIManagerServicesApi.md#filedata_post) | **POST** /filedata | Returns the DataURI representation of the uploaded file
*APIManagerServicesApi* | [**license_get**](docs/APIManagerServicesApi.md#license_get) | **GET** /license | Checks that the API Manager has a valid license
*APIManagerServicesApi* | [**listeners_get**](docs/APIManagerServicesApi.md#listeners_get) | **GET** /listeners | Gets the API Manager listeners
*APIManagerServicesApi* | [**oauthclientprofiles_get**](docs/APIManagerServicesApi.md#oauthclientprofiles_get) | **GET** /oauthclientprofiles | Get a list of OAuth profiles for use in backend API authorisation
*APIManagerServicesApi* | [**policies_get**](docs/APIManagerServicesApi.md#policies_get) | **GET** /policies | Gets a list of the specified policies
*APIManagerServicesApi* | [**remotehosts_get**](docs/APIManagerServicesApi.md#remotehosts_get) | **GET** /remotehosts | Returns a list of remote hosts
*APIManagerServicesApi* | [**remotehosts_id_delete**](docs/APIManagerServicesApi.md#remotehosts_id_delete) | **DELETE** /remotehosts/{id} | Deletes a remote host.
*APIManagerServicesApi* | [**remotehosts_id_put**](docs/APIManagerServicesApi.md#remotehosts_id_put) | **PUT** /remotehosts/{id} | Updates a remote host
*APIManagerServicesApi* | [**remotehosts_post**](docs/APIManagerServicesApi.md#remotehosts_post) | **POST** /remotehosts | Creates a new remote host
*APIManagerServicesApi* | [**service_discovery_instance_type_post**](docs/APIManagerServicesApi.md#service_discovery_instance_type_post) | **POST** /service-discovery/{instance}/{type} | Returns a list of services hosted on the specified Gateway instance
*APIManagerServicesApi* | [**sysconfig_get**](docs/APIManagerServicesApi.md#sysconfig_get) | **GET** /sysconfig | Gets API Manager system configuration
*APIManagerServicesApi* | [**sysconfig_put**](docs/APIManagerServicesApi.md#sysconfig_put) | **PUT** /sysconfig | Update API Manager system configuration
*APIManagerServicesApi* | [**title_get**](docs/APIManagerServicesApi.md#title_get) | **GET** /title | Gets the API Manager&#39;s title
*APIManagerServicesApi* | [**tokenstores_get**](docs/APIManagerServicesApi.md#tokenstores_get) | **GET** /tokenstores | Gets a list of Token Stores
*APIManagerServicesApi* | [**topology_post**](docs/APIManagerServicesApi.md#topology_post) | **POST** /topology | Retrieves the Topology from the specified Admin Node Manager
*APIProxyRegistrationApi* | [**proxies_export_id_get**](docs/APIProxyRegistrationApi.md#proxies_export_id_get) | **GET** /proxies/export/{id} | Downloads an API export.
*APIProxyRegistrationApi* | [**proxies_export_post**](docs/APIProxyRegistrationApi.md#proxies_export_post) | **POST** /proxies/export | Creates an API export.
*APIProxyRegistrationApi* | [**proxies_get**](docs/APIProxyRegistrationApi.md#proxies_get) | **GET** /proxies | Queries a list of frontend API.
*APIProxyRegistrationApi* | [**proxies_grantaccess_post**](docs/APIProxyRegistrationApi.md#proxies_grantaccess_post) | **POST** /proxies/grantaccess | Macro function to grant API access.
*APIProxyRegistrationApi* | [**proxies_id_delete**](docs/APIProxyRegistrationApi.md#proxies_id_delete) | **DELETE** /proxies/{id} | Deletes an API proxy.
*APIProxyRegistrationApi* | [**proxies_id_deprecate_post**](docs/APIProxyRegistrationApi.md#proxies_id_deprecate_post) | **POST** /proxies/{id}/deprecate | Deprecates the API.
*APIProxyRegistrationApi* | [**proxies_id_get**](docs/APIProxyRegistrationApi.md#proxies_id_get) | **GET** /proxies/{id} | Gets a frontend API by ID.
*APIProxyRegistrationApi* | [**proxies_id_image_get**](docs/APIProxyRegistrationApi.md#proxies_id_image_get) | **GET** /proxies/{id}/image | Gets the image for the API.
*APIProxyRegistrationApi* | [**proxies_id_image_post**](docs/APIProxyRegistrationApi.md#proxies_id_image_post) | **POST** /proxies/{id}/image | Set the image for the frontend API.
*APIProxyRegistrationApi* | [**proxies_id_operations_get**](docs/APIProxyRegistrationApi.md#proxies_id_operations_get) | **GET** /proxies/{id}/operations | Gets a list of methods that are avilable to the API proxy.
*APIProxyRegistrationApi* | [**proxies_id_operations_operation_id_delete**](docs/APIProxyRegistrationApi.md#proxies_id_operations_operation_id_delete) | **DELETE** /proxies/{id}/operations/{operationId} | Deletes an API method by ID.
*APIProxyRegistrationApi* | [**proxies_id_operations_operation_id_get**](docs/APIProxyRegistrationApi.md#proxies_id_operations_operation_id_get) | **GET** /proxies/{id}/operations/{operationId} | Gets an API method by ID.
*APIProxyRegistrationApi* | [**proxies_id_operations_operation_id_put**](docs/APIProxyRegistrationApi.md#proxies_id_operations_operation_id_put) | **PUT** /proxies/{id}/operations/{operationId} | Updates an API proxy operation.
*APIProxyRegistrationApi* | [**proxies_id_publish_post**](docs/APIProxyRegistrationApi.md#proxies_id_publish_post) | **POST** /proxies/{id}/publish | Publish the API.
*APIProxyRegistrationApi* | [**proxies_id_put**](docs/APIProxyRegistrationApi.md#proxies_id_put) | **PUT** /proxies/{id} | Updates an API proxy.
*APIProxyRegistrationApi* | [**proxies_id_undeprecate_post**](docs/APIProxyRegistrationApi.md#proxies_id_undeprecate_post) | **POST** /proxies/{id}/undeprecate | Undeprecates the API.
*APIProxyRegistrationApi* | [**proxies_id_unpublish_post**](docs/APIProxyRegistrationApi.md#proxies_id_unpublish_post) | **POST** /proxies/{id}/unpublish | Unpublish the API.
*APIProxyRegistrationApi* | [**proxies_import_from_url_post**](docs/APIProxyRegistrationApi.md#proxies_import_from_url_post) | **POST** /proxies/importFromUrl | Imports a previously exported API.
*APIProxyRegistrationApi* | [**proxies_import_post**](docs/APIProxyRegistrationApi.md#proxies_import_post) | **POST** /proxies/import | Imports a previously exported API.
*APIProxyRegistrationApi* | [**proxies_post**](docs/APIProxyRegistrationApi.md#proxies_post) | **POST** /proxies | Creates a new API proxy from a backend API.
*APIProxyRegistrationApi* | [**proxies_promote_post**](docs/APIProxyRegistrationApi.md#proxies_promote_post) | **POST** /proxies/promote | Invokes the internal API promotion policy for the specified API.
*APIProxyRegistrationApi* | [**proxies_upgrade_id_post**](docs/APIProxyRegistrationApi.md#proxies_upgrade_id_post) | **POST** /proxies/upgrade/{id} | Upgrades an existing frontend API to a newer frontend API.
*APIRepositoryApi* | [**apirepo_get**](docs/APIRepositoryApi.md#apirepo_get) | **GET** /apirepo | Get the list of API
*APIRepositoryApi* | [**apirepo_id_delete**](docs/APIRepositoryApi.md#apirepo_id_delete) | **DELETE** /apirepo/{id} | Deletes an API.
*APIRepositoryApi* | [**apirepo_id_download_get**](docs/APIRepositoryApi.md#apirepo_id_download_get) | **GET** /apirepo/{id}/download | Downloads an API by ID.
*APIRepositoryApi* | [**apirepo_id_get**](docs/APIRepositoryApi.md#apirepo_id_get) | **GET** /apirepo/{id} | Get an API by ID
*APIRepositoryApi* | [**apirepo_id_methods_get**](docs/APIRepositoryApi.md#apirepo_id_methods_get) | **GET** /apirepo/{id}/methods | Queries the list of API methods
*APIRepositoryApi* | [**apirepo_id_methods_method_id_delete**](docs/APIRepositoryApi.md#apirepo_id_methods_method_id_delete) | **DELETE** /apirepo/{id}/methods/{methodId} | Delete an API method
*APIRepositoryApi* | [**apirepo_id_methods_method_id_get**](docs/APIRepositoryApi.md#apirepo_id_methods_method_id_get) | **GET** /apirepo/{id}/methods/{methodId} | Get API method by ID.
*APIRepositoryApi* | [**apirepo_id_methods_method_id_put**](docs/APIRepositoryApi.md#apirepo_id_methods_method_id_put) | **PUT** /apirepo/{id}/methods/{methodId} | Update an API method
*APIRepositoryApi* | [**apirepo_id_methods_post**](docs/APIRepositoryApi.md#apirepo_id_methods_post) | **POST** /apirepo/{id}/methods | Create an API method
*APIRepositoryApi* | [**apirepo_id_put**](docs/APIRepositoryApi.md#apirepo_id_put) | **PUT** /apirepo/{id} | Updates an API
*APIRepositoryApi* | [**apirepo_import_from_external_post**](docs/APIRepositoryApi.md#apirepo_import_from_external_post) | **POST** /apirepo/importFromExternal | Create one or more backend APIs for an external service
*APIRepositoryApi* | [**apirepo_import_from_gw_post**](docs/APIRepositoryApi.md#apirepo_import_from_gw_post) | **POST** /apirepo/importFromGw | Create an API definition by importing a PolicyStudio-registered web service (REST or WSDL) hosted on the the API Gateway
*APIRepositoryApi* | [**apirepo_import_from_url_post**](docs/APIRepositoryApi.md#apirepo_import_from_url_post) | **POST** /apirepo/importFromUrl | Create an API by loading a file from URL.
*APIRepositoryApi* | [**apirepo_import_post**](docs/APIRepositoryApi.md#apirepo_import_post) | **POST** /apirepo/import | Create an API by uploading a file
*APIRepositoryApi* | [**apirepo_post**](docs/APIRepositoryApi.md#apirepo_post) | **POST** /apirepo | Create an API definition
*ApplicationsApi* | [**applications_get**](docs/ApplicationsApi.md#applications_get) | **GET** /applications | Get the list of applications
*ApplicationsApi* | [**applications_id_apikeys_apikeyid_put**](docs/ApplicationsApi.md#applications_id_apikeys_apikeyid_put) | **PUT** /applications/{id}/apikeys/{apikeyid} | Updates an API Key
*ApplicationsApi* | [**applications_id_apikeys_get**](docs/ApplicationsApi.md#applications_id_apikeys_get) | **GET** /applications/{id}/apikeys | Returns the API Keys associated with an application
*ApplicationsApi* | [**applications_id_apikeys_key_id_delete**](docs/ApplicationsApi.md#applications_id_apikeys_key_id_delete) | **DELETE** /applications/{id}/apikeys/{keyId} | Delete an API Key
*ApplicationsApi* | [**applications_id_apikeys_post**](docs/ApplicationsApi.md#applications_id_apikeys_post) | **POST** /applications/{id}/apikeys | Creates a new API Key and secret for the application
*ApplicationsApi* | [**applications_id_apis_api_access_id_approve_post**](docs/ApplicationsApi.md#applications_id_apis_api_access_id_approve_post) | **POST** /applications/{id}/apis/{apiAccessId}/approve | Creates an API access request to an API for an application.
*ApplicationsApi* | [**applications_id_apis_api_access_id_delete**](docs/ApplicationsApi.md#applications_id_apis_api_access_id_delete) | **DELETE** /applications/{id}/apis/{apiAccessId} | Deletes access to an API for an application
*ApplicationsApi* | [**applications_id_apis_api_access_id_put**](docs/ApplicationsApi.md#applications_id_apis_api_access_id_put) | **PUT** /applications/{id}/apis/{apiAccessId} | Updates access to an API for an application
*ApplicationsApi* | [**applications_id_apis_get**](docs/ApplicationsApi.md#applications_id_apis_get) | **GET** /applications/{id}/apis | Get the list of APIs that the application can access
*ApplicationsApi* | [**applications_id_apis_post**](docs/ApplicationsApi.md#applications_id_apis_post) | **POST** /applications/{id}/apis | Create a request for an application to access an API.
*ApplicationsApi* | [**applications_id_approve_post**](docs/ApplicationsApi.md#applications_id_approve_post) | **POST** /applications/{id}/approve | Approves a pending application request
*ApplicationsApi* | [**applications_id_availablescopes_get**](docs/ApplicationsApi.md#applications_id_availablescopes_get) | **GET** /applications/{id}/availablescopes | Returns the scopes available to an application
*ApplicationsApi* | [**applications_id_delete**](docs/ApplicationsApi.md#applications_id_delete) | **DELETE** /applications/{id} | Delete an application
*ApplicationsApi* | [**applications_id_extclients_get**](docs/ApplicationsApi.md#applications_id_extclients_get) | **GET** /applications/{id}/extclients | Returns the external clients associated with an application
*ApplicationsApi* | [**applications_id_extclients_object_id_delete**](docs/ApplicationsApi.md#applications_id_extclients_object_id_delete) | **DELETE** /applications/{id}/extclients/{objectId} | Delete an external client
*ApplicationsApi* | [**applications_id_extclients_object_id_put**](docs/ApplicationsApi.md#applications_id_extclients_object_id_put) | **PUT** /applications/{id}/extclients/{objectId} | Updates an external client for the application
*ApplicationsApi* | [**applications_id_extclients_post**](docs/ApplicationsApi.md#applications_id_extclients_post) | **POST** /applications/{id}/extclients | Maps a new external client to the application
*ApplicationsApi* | [**applications_id_get**](docs/ApplicationsApi.md#applications_id_get) | **GET** /applications/{id} | Get an application
*ApplicationsApi* | [**applications_id_image_get**](docs/ApplicationsApi.md#applications_id_image_get) | **GET** /applications/{id}/image | Get the image for an application
*ApplicationsApi* | [**applications_id_image_post**](docs/ApplicationsApi.md#applications_id_image_post) | **POST** /applications/{id}/image | Adds a JPEG image to an application
*ApplicationsApi* | [**applications_id_oauth_client_id_put**](docs/ApplicationsApi.md#applications_id_oauth_client_id_put) | **PUT** /applications/{id}/oauth/{clientId} | Updates an OAuth Credential for the application
*ApplicationsApi* | [**applications_id_oauth_clientid_newsecret_put**](docs/ApplicationsApi.md#applications_id_oauth_clientid_newsecret_put) | **PUT** /applications/{id}/oauth/{clientid}/newsecret | Updates an OAuth Credential for an application by generating a new secret
*ApplicationsApi* | [**applications_id_oauth_get**](docs/ApplicationsApi.md#applications_id_oauth_get) | **GET** /applications/{id}/oauth | Returns the OAuth Credentials associated with an application
*ApplicationsApi* | [**applications_id_oauth_oauth_id_delete**](docs/ApplicationsApi.md#applications_id_oauth_oauth_id_delete) | **DELETE** /applications/{id}/oauth/{oauthId} | Delete an OAuth client ID and secret
*ApplicationsApi* | [**applications_id_oauth_post**](docs/ApplicationsApi.md#applications_id_oauth_post) | **POST** /applications/{id}/oauth | Creates a new OAuth client ID and secret for the application
*ApplicationsApi* | [**applications_id_oauthresource_get**](docs/ApplicationsApi.md#applications_id_oauthresource_get) | **GET** /applications/{id}/oauthresource | Returns the OAuth protected resources (scopes) associated with an application
*ApplicationsApi* | [**applications_id_oauthresource_post**](docs/ApplicationsApi.md#applications_id_oauthresource_post) | **POST** /applications/{id}/oauthresource | Adds an OAuth protected resource to an application
*ApplicationsApi* | [**applications_id_oauthresource_resource_id_delete**](docs/ApplicationsApi.md#applications_id_oauthresource_resource_id_delete) | **DELETE** /applications/{id}/oauthresource/{resourceId} | Remove an OAuth protected resource from an application
*ApplicationsApi* | [**applications_id_oauthresource_resource_id_put**](docs/ApplicationsApi.md#applications_id_oauthresource_resource_id_put) | **PUT** /applications/{id}/oauthresource/{resourceId} | Updates a protected resource associate with an application, sets enabled to true/false
*ApplicationsApi* | [**applications_id_permissions_get**](docs/ApplicationsApi.md#applications_id_permissions_get) | **GET** /applications/{id}/permissions | Get the list of permissions.
*ApplicationsApi* | [**applications_id_permissions_perm_id_delete**](docs/ApplicationsApi.md#applications_id_permissions_perm_id_delete) | **DELETE** /applications/{id}/permissions/{permId} | Remove a permission
*ApplicationsApi* | [**applications_id_permissions_perm_id_put**](docs/ApplicationsApi.md#applications_id_permissions_perm_id_put) | **PUT** /applications/{id}/permissions/{permId} | Modify a permission
*ApplicationsApi* | [**applications_id_permissions_post**](docs/ApplicationsApi.md#applications_id_permissions_post) | **POST** /applications/{id}/permissions | Create a new permission.
*ApplicationsApi* | [**applications_id_put**](docs/ApplicationsApi.md#applications_id_put) | **PUT** /applications/{id} | Update an application
*ApplicationsApi* | [**applications_id_quota_delete**](docs/ApplicationsApi.md#applications_id_quota_delete) | **DELETE** /applications/{id}/quota | Deletes a quota from an application
*ApplicationsApi* | [**applications_id_quota_get**](docs/ApplicationsApi.md#applications_id_quota_get) | **GET** /applications/{id}/quota | Returns the quota associated with an application.
*ApplicationsApi* | [**applications_id_quota_post**](docs/ApplicationsApi.md#applications_id_quota_post) | **POST** /applications/{id}/quota | Creates a new quota constraint for the application
*ApplicationsApi* | [**applications_id_quota_put**](docs/ApplicationsApi.md#applications_id_quota_put) | **PUT** /applications/{id}/quota | Updates a quota contraint for an application
*ApplicationsApi* | [**applications_id_scope_get**](docs/ApplicationsApi.md#applications_id_scope_get) | **GET** /applications/{id}/scope | Returns the scopes associated with an application
*ApplicationsApi* | [**applications_id_scope_post**](docs/ApplicationsApi.md#applications_id_scope_post) | **POST** /applications/{id}/scope | Adds an OAuth protected resource to an application
*ApplicationsApi* | [**applications_id_scope_scope_id_delete**](docs/ApplicationsApi.md#applications_id_scope_scope_id_delete) | **DELETE** /applications/{id}/scope/{scopeId} | Remove an OAuth protected resource from an application
*ApplicationsApi* | [**applications_id_scope_scope_id_put**](docs/ApplicationsApi.md#applications_id_scope_scope_id_put) | **PUT** /applications/{id}/scope/{scopeId} | Updates a scope associated with an application, sets default to true/false
*ApplicationsApi* | [**applications_oauthclient_client_id_get**](docs/ApplicationsApi.md#applications_oauthclient_client_id_get) | **GET** /applications/oauthclient/{clientId} | Get an application associated with an OAuth Client ID
*ApplicationsApi* | [**applications_post**](docs/ApplicationsApi.md#applications_post) | **POST** /applications | Creates a new application.
*CurrentUserApi* | [**currentuser_changepassword_post**](docs/CurrentUserApi.md#currentuser_changepassword_post) | **POST** /currentuser/changepassword | Modify the current user&#39;s password
*CurrentUserApi* | [**currentuser_get**](docs/CurrentUserApi.md#currentuser_get) | **GET** /currentuser | Get the current user
*CurrentUserApi* | [**currentuser_put**](docs/CurrentUserApi.md#currentuser_put) | **PUT** /currentuser | Modify the current user
*LoginApi* | [**login_delete**](docs/LoginApi.md#login_delete) | **DELETE** /login | Logout from API Manager
*LoginApi* | [**login_post**](docs/LoginApi.md#login_post) | **POST** /login | Login to API Manager
*MetricsApi* | [**metrics_fields_get**](docs/MetricsApi.md#metrics_fields_get) | **GET** /metrics/fields | Gets a list of metric field names available for summary and timeline queries.
*MetricsApi* | [**metrics_reports_type_summary_level_get**](docs/MetricsApi.md#metrics_reports_type_summary_level_get) | **GET** /metrics/reports/{type}/summary/{level} | Gets a summary report for application usage
*MetricsApi* | [**metrics_reports_type_timeline_level_metric_type_get**](docs/MetricsApi.md#metrics_reports_type_timeline_level_metric_type_get) | **GET** /metrics/reports/{type}/timeline/{level}/{metricType} | Gets a timeline report for application usage
*MigrateApi* | [**migrate_applications_export_create_post**](docs/MigrateApi.md#migrate_applications_export_create_post) | **POST** /migrate/applications/export/create | Creates a set of export options associated with the current http session
*MigrateApi* | [**migrate_applications_export_download_get**](docs/MigrateApi.md#migrate_applications_export_download_get) | **GET** /migrate/applications/export/download | Exports Application data for migration to other API Gateways
*MigrateApi* | [**migrate_applications_export_json_post**](docs/MigrateApi.md#migrate_applications_export_json_post) | **POST** /migrate/applications/export/json | Creates an export of applications based on the export options posted as a JSON object
*MigrateApi* | [**migrate_applications_export_post**](docs/MigrateApi.md#migrate_applications_export_post) | **POST** /migrate/applications/export | Creates an export of applications based on the export options posted in a form data
*MigrateApi* | [**migrate_applications_import_post**](docs/MigrateApi.md#migrate_applications_import_post) | **POST** /migrate/applications/import | Imports applications to the API Gateway
*OAuthAuthorizationsApi* | [**authorizations_authzid_delete**](docs/OAuthAuthorizationsApi.md#authorizations_authzid_delete) | **DELETE** /authorizations/{authzid} | Delete the OAuth Authorization for the given authorization id.
*OAuthAuthorizationsApi* | [**authorizations_get**](docs/OAuthAuthorizationsApi.md#authorizations_get) | **GET** /authorizations | Retrieve all stored OAuth Authorizations for the logged in user.
*OAuthAuthorizationsApi* | [**authorizations_owner_subjectid_application_appid_delete**](docs/OAuthAuthorizationsApi.md#authorizations_owner_subjectid_application_appid_delete) | **DELETE** /authorizations/owner/{subjectid}/application/{appid} | 
*OrganizationsApi* | [**organizations_get**](docs/OrganizationsApi.md#organizations_get) | **GET** /organizations | List all organizations
*OrganizationsApi* | [**organizations_id_apis_api_access_id_delete**](docs/OrganizationsApi.md#organizations_id_apis_api_access_id_delete) | **DELETE** /organizations/{id}/apis/{apiAccessId} | Deletes access to an API for an organization
*OrganizationsApi* | [**organizations_id_apis_api_access_id_put**](docs/OrganizationsApi.md#organizations_id_apis_api_access_id_put) | **PUT** /organizations/{id}/apis/{apiAccessId} | Updates access to an API for an organization
*OrganizationsApi* | [**organizations_id_apis_get**](docs/OrganizationsApi.md#organizations_id_apis_get) | **GET** /organizations/{id}/apis | Get the list of approved APIs for the organization
*OrganizationsApi* | [**organizations_id_apis_post**](docs/OrganizationsApi.md#organizations_id_apis_post) | **POST** /organizations/{id}/apis | Grants access to an API for an organization.
*OrganizationsApi* | [**organizations_id_delete**](docs/OrganizationsApi.md#organizations_id_delete) | **DELETE** /organizations/{id} | Delete an organization
*OrganizationsApi* | [**organizations_id_get**](docs/OrganizationsApi.md#organizations_id_get) | **GET** /organizations/{id} | Get an organization
*OrganizationsApi* | [**organizations_id_image_get**](docs/OrganizationsApi.md#organizations_id_image_get) | **GET** /organizations/{id}/image | Get the image for an organization
*OrganizationsApi* | [**organizations_id_image_post**](docs/OrganizationsApi.md#organizations_id_image_post) | **POST** /organizations/{id}/image | Set the image for an organization
*OrganizationsApi* | [**organizations_id_put**](docs/OrganizationsApi.md#organizations_id_put) | **PUT** /organizations/{id} | Update the details of an organization
*OrganizationsApi* | [**organizations_id_tokens_get**](docs/OrganizationsApi.md#organizations_id_tokens_get) | **GET** /organizations/{id}/tokens | Get registration codes for an organization
*OrganizationsApi* | [**organizations_id_tokens_post**](docs/OrganizationsApi.md#organizations_id_tokens_post) | **POST** /organizations/{id}/tokens | Create a registration code
*OrganizationsApi* | [**organizations_id_tokens_token_delete**](docs/OrganizationsApi.md#organizations_id_tokens_token_delete) | **DELETE** /organizations/{id}/tokens/{token} | Delete the registration code
*OrganizationsApi* | [**organizations_id_tokens_token_get**](docs/OrganizationsApi.md#organizations_id_tokens_token_get) | **GET** /organizations/{id}/tokens/{token} | Get registration code
*OrganizationsApi* | [**organizations_id_tokens_token_put**](docs/OrganizationsApi.md#organizations_id_tokens_token_put) | **PUT** /organizations/{id}/tokens/{token} | Update a registration code
*OrganizationsApi* | [**organizations_post**](docs/OrganizationsApi.md#organizations_post) | **POST** /organizations | Creates a new organization
*QuotasApi* | [**quotas_get**](docs/QuotasApi.md#quotas_get) | **GET** /quotas | Returns all quotas
*QuotasApi* | [**quotas_id_delete**](docs/QuotasApi.md#quotas_id_delete) | **DELETE** /quotas/{id} | Deletes a quota
*QuotasApi* | [**quotas_id_get**](docs/QuotasApi.md#quotas_id_get) | **GET** /quotas/{id} | Returns the quota with the given ID
*QuotasApi* | [**quotas_id_put**](docs/QuotasApi.md#quotas_id_put) | **PUT** /quotas/{id} | Updates a quota
*QuotasApi* | [**quotas_post**](docs/QuotasApi.md#quotas_post) | **POST** /quotas | Creates a new quota
*UsersApi* | [**users_forgotpassword_post**](docs/UsersApi.md#users_forgotpassword_post) | **POST** /users/forgotpassword | Allows a user to reset their password.
*UsersApi* | [**users_get**](docs/UsersApi.md#users_get) | **GET** /users | Obtains a list of users
*UsersApi* | [**users_id_approve_post**](docs/UsersApi.md#users_id_approve_post) | **POST** /users/{id}/approve | Grants approval to a request to create a new user on the system.
*UsersApi* | [**users_id_changepassword_post**](docs/UsersApi.md#users_id_changepassword_post) | **POST** /users/{id}/changepassword | Updates the password for a given user.
*UsersApi* | [**users_id_delete**](docs/UsersApi.md#users_id_delete) | **DELETE** /users/{id} | Deletes a user.
*UsersApi* | [**users_id_get**](docs/UsersApi.md#users_id_get) | **GET** /users/{id} | Retrieves the details for a given user.
*UsersApi* | [**users_id_image_get**](docs/UsersApi.md#users_id_image_get) | **GET** /users/{id}/image | Get the image for a user
*UsersApi* | [**users_id_image_post**](docs/UsersApi.md#users_id_image_post) | **POST** /users/{id}/image | Set the image for a user
*UsersApi* | [**users_id_put**](docs/UsersApi.md#users_id_put) | **PUT** /users/{id} | Updates the details for a given user.
*UsersApi* | [**users_id_resetpassword_put**](docs/UsersApi.md#users_id_resetpassword_put) | **PUT** /users/{id}/resetpassword | Admin level function to reset the password for a given user.
*UsersApi* | [**users_post**](docs/UsersApi.md#users_post) | **POST** /users | Admin function to create a new user on the system
*UsersApi* | [**users_register_post**](docs/UsersApi.md#users_register_post) | **POST** /users/register | Register a new user.
*UsersApi* | [**users_resetpassword_get**](docs/UsersApi.md#users_resetpassword_get) | **GET** /users/resetpassword | Validates the user [/forgotpassword](#APIUsersforgotUserPassword) password request.
*UsersApi* | [**users_validateuser_get**](docs/UsersApi.md#users_validateuser_get) | **GET** /users/validateuser | Validates the user [/register](#APIUsersregisterUser) request.


## Documentation For Models

 - [API](docs/API.md)
 - [APIAccess](docs/APIAccess.md)
 - [APIDefinition](docs/APIDefinition.md)
 - [APIKey](docs/APIKey.md)
 - [APIPromotion](docs/APIPromotion.md)
 - [AlertConfig](docs/AlertConfig.md)
 - [Application](docs/Application.md)
 - [ApplicationRequest](docs/ApplicationRequest.md)
 - [AuthenticatedUserAttributes](docs/AuthenticatedUserAttributes.md)
 - [AuthenticationProfile](docs/AuthenticationProfile.md)
 - [Authorization](docs/Authorization.md)
 - [AuthorizationCode](docs/AuthorizationCode.md)
 - [BackendBlob](docs/BackendBlob.md)
 - [BackendExport](docs/BackendExport.md)
 - [BackendMethodExport](docs/BackendMethodExport.md)
 - [CACert](docs/CACert.md)
 - [CORSProfile](docs/CORSProfile.md)
 - [Config](docs/Config.md)
 - [DiscoveryAPI](docs/DiscoveryAPI.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ExportOptions](docs/ExportOptions.md)
 - [ExternalClient](docs/ExternalClient.md)
 - [FrontendExport](docs/FrontendExport.md)
 - [GrantTypes](docs/GrantTypes.md)
 - [Group](docs/Group.md)
 - [Host](docs/Host.md)
 - [Implicit](docs/Implicit.md)
 - [InboundProfiles](docs/InboundProfiles.md)
 - [Lock](docs/Lock.md)
 - [LoginEndpoint](docs/LoginEndpoint.md)
 - [Method](docs/Method.md)
 - [MetricField](docs/MetricField.md)
 - [MetricTimeline](docs/MetricTimeline.md)
 - [OAuthAppScope](docs/OAuthAppScope.md)
 - [OAuthClient](docs/OAuthClient.md)
 - [OAuthProtectedResource](docs/OAuthProtectedResource.md)
 - [OAuthResource](docs/OAuthResource.md)
 - [Operation](docs/Operation.md)
 - [Organization](docs/Organization.md)
 - [OutboundProfiles](docs/OutboundProfiles.md)
 - [ParamValue](docs/ParamValue.md)
 - [Parameter](docs/Parameter.md)
 - [PermissionDTO](docs/PermissionDTO.md)
 - [PortalTrafficListener](docs/PortalTrafficListener.md)
 - [QuotaApiConstraintDTO](docs/QuotaApiConstraintDTO.md)
 - [QuotaDTO](docs/QuotaDTO.md)
 - [ReferencedEntity](docs/ReferencedEntity.md)
 - [RegistrationToken](docs/RegistrationToken.md)
 - [RemoteHost](docs/RemoteHost.md)
 - [ResponseCode](docs/ResponseCode.md)
 - [SchemaObject](docs/SchemaObject.md)
 - [Scope](docs/Scope.md)
 - [SecurityDevice](docs/SecurityDevice.md)
 - [SecurityProfile](docs/SecurityProfile.md)
 - [Series](docs/Series.md)
 - [Service](docs/Service.md)
 - [ServiceProfiles](docs/ServiceProfiles.md)
 - [Swagger](docs/Swagger.md)
 - [SwaggerSecurityDevice](docs/SwaggerSecurityDevice.md)
 - [SwaggerSecurityProfile](docs/SwaggerSecurityProfile.md)
 - [SystemConfig](docs/SystemConfig.md)
 - [TokenEndpoint](docs/TokenEndpoint.md)
 - [TokenRequestEndpoint](docs/TokenRequestEndpoint.md)
 - [Topology](docs/Topology.md)
 - [User](docs/User.md)
 - [VirtualizedAPI](docs/VirtualizedAPI.md)
 - [VirtualizedAPIMethod](docs/VirtualizedAPIMethod.md)
 - [VirtualizedMethodExport](docs/VirtualizedMethodExport.md)


## Documentation For Authorization


## basic

- **Type**: HTTP basic authentication


## Author

support@axway.com

