# Config

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portal_name** | **str** | The name of the API Manager. | [optional] 
**portal_hostname** | **str** | The network hostname or IP Address of the API Manager which will be used in email links. | [optional] 
**api_portal_name** | **str** | The name of the API Portal | [optional] 
**api_portal_hostname** | **str** | The network hostname or IP Address of the API Portal which will be used in email links. | [optional] 
**is_api_portal_configured** | **bool** | Indicates if the API Portal is configured. | [optional] [default to False]
**registration_enabled** | **bool** | Enables/disables user registration for the API Manager | [optional] [default to False]
**reset_password_enabled** | **bool** | Enables/disables spport for resetting user passwords for the API Manager | [optional] [default to False]
**minimum_password_length** | **int** | The minimum password length. | [optional] 
**auto_approve_user_registration** | **bool** | Enables/disables auto-approve for user registration whereby API Administrator or Organization Administrator approval is not required. | [optional] [default to False]
**system_o_auth_scopes_enabled** | **bool** | Enables/disables the ability to add System scopes to an Application. These scopes represent Gateway OAuth resources that are not covered by APIs. | [optional] [default to False]
**auto_approve_applications** | **bool** | Enables/disables auto-application approval whereby users do not need API Administrator or Organization Administrator approval. | [optional] [default to False]
**delegate_user_administration** | **bool** | Enables/disables user administration to the Organization Administrators. | [optional] [default to False]
**delegate_application_administration** | **bool** | Enables/disables application administration to the Organization Administrators. | [optional] [default to False]
**api_default_virtual_host** | **str** | The network host and port that serves as the default virtual host from which API Manager registered API will be accessible through. | [optional] 
**api_routing_key_enabled** | **bool** | Enable routing to APIs on the same base path. | [optional] [default to False]
**api_routing_key_location** | **str** | An additional routing key is required to support multiple APIs registered on the same base path. This indicates where to look for the value. | [optional] 
**email_from** | **str** | The &#39;from&#39; address used in emails. | [optional] 
**email_bounce_address** | **str** | An email address where undeliverable emails will be bounced to. | [optional] 
**promote_api_via_policy** | **bool** | Enables/disables API promotion via policy. | [optional] [default to False]
**global_policies_enabled** | **bool** | Enables/disables Global policies. | [optional] [default to False]
**global_request_policy** | **str** | The Global Request Policy to be executed for all Frontend API calls. Must be a valid policy ID. Can be null to indicate no policy | [optional] 
**global_response_policy** | **str** | The Global Response Policy to be executed for all Frontend API calls. Must be a valid policy ID. Can be null to indicate no policy | [optional] 
**fault_handlers_enabled** | **bool** | Enables/disables API Manager fault handlers. | [optional] [default to False]
**global_fault_handler_policy** | **str** | The Global Fault Handler Policy to be used by all Frontend APIs in the event of an error. Must be a valid policy ID. Can be null to indicate no policy | [optional] 
**base_o_auth** | **bool** |  | [optional] [default to False]
**external_user_name** | **str** | External user name | [optional] 
**external_user_description** | **str** | External user description | [optional] 
**external_user_phone** | **str** | External user phone | [optional] 
**external_user_email** | **str** | External user email | [optional] 
**external_user_organization** | **str** | External user organization name | [optional] 
**external_user_role** | **str** | External user role | [optional] 
**external_user_enabled** | **str** | External user enabled | [optional] 
**session_idle_timeout** | **int** | Idle session timeout in milliseconds | 
**is_trial** | **bool** | Is trial enabled | [optional] [default to False]
**default_trial_duration** | **int** | Default trial duration in days | [optional] 
**login_name_regex** | **str** | Login name validation regex | [optional] 
**product_version** | **str** | The Version information of API Manager. | [optional] 
**os** | **str** | The operating system on which API Manager server is running. | [optional] 
**architecture** | **str** | The architecture of the operating system on which the API Manager server is running. Supported values: [ win-x86-32, linux-x86-64 ] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


