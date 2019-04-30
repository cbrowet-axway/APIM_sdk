# swagger_client.MetricsApi

All URIs are relative to *https://localhost/api/portal/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metrics_fields_get**](MetricsApi.md#metrics_fields_get) | **GET** /metrics/fields | Gets a list of metric field names available for summary and timeline queries.
[**metrics_reports_type_summary_level_get**](MetricsApi.md#metrics_reports_type_summary_level_get) | **GET** /metrics/reports/{type}/summary/{level} | Gets a summary report for application usage
[**metrics_reports_type_timeline_level_metric_type_get**](MetricsApi.md#metrics_reports_type_timeline_level_metric_type_get) | **GET** /metrics/reports/{type}/timeline/{level}/{metricType} | Gets a timeline report for application usage


# **metrics_fields_get**
> list[MetricField] metrics_fields_get()

Gets a list of metric field names available for summary and timeline queries.

Retrieves a set of metric fields that may be used when querying or interpreting the summary and timeline reports.  The __metricType__ is the metric name.  The __aggreggateName__ is the metric name for the aggregated __metricType__.

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
api_instance = swagger_client.MetricsApi(swagger_client.ApiClient(configuration))

try:
    # Gets a list of metric field names available for summary and timeline queries.
    api_response = api_instance.metrics_fields_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->metrics_fields_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MetricField]**](MetricField.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_reports_type_summary_level_get**
> metrics_reports_type_summary_level_get(type, level, _from, to, client=client, service=service, method=method, organization=organization, reportsubtype=reportsubtype)

Gets a summary report for application usage



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
api_instance = swagger_client.MetricsApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | The report type, either 'app' or 'api'
level = 56 # int | The report level (0 or 1 for drill-through)
_from = '_from_example' # str | The starting date/time for the report.
to = 'to_example' # str | The end date/time for the report.
client = ['client_example'] # list[str] | Filter a specific client ID (multiple permitted). (optional)
service = ['service_example'] # list[str] | Filter a specific service name (multiple permitted). (optional)
method = 'method_example' # str | Filter a specific method. (optional)
organization = 'organization_example' # str | Filter a specific organziation. (optional)
reportsubtype = 'reportsubtype_example' # str | Define the report subtype. Allowed values are : 'original', 'trafficAll' or 'trafficSubset'. Defaults to 'original' if absent (optional)

try:
    # Gets a summary report for application usage
    api_instance.metrics_reports_type_summary_level_get(type, level, _from, to, client=client, service=service, method=method, organization=organization, reportsubtype=reportsubtype)
except ApiException as e:
    print("Exception when calling MetricsApi->metrics_reports_type_summary_level_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The report type, either &#39;app&#39; or &#39;api&#39; | 
 **level** | **int**| The report level (0 or 1 for drill-through) | 
 **_from** | **str**| The starting date/time for the report. | 
 **to** | **str**| The end date/time for the report. | 
 **client** | [**list[str]**](str.md)| Filter a specific client ID (multiple permitted). | [optional] 
 **service** | [**list[str]**](str.md)| Filter a specific service name (multiple permitted). | [optional] 
 **method** | **str**| Filter a specific method. | [optional] 
 **organization** | **str**| Filter a specific organziation. | [optional] 
 **reportsubtype** | **str**| Define the report subtype. Allowed values are : &#39;original&#39;, &#39;trafficAll&#39; or &#39;trafficSubset&#39;. Defaults to &#39;original&#39; if absent | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_reports_type_timeline_level_metric_type_get**
> MetricTimeline metrics_reports_type_timeline_level_metric_type_get(type, level, _from, to, metric_type, client=client, service=service, method=method, organization=organization, reportsubtype=reportsubtype)

Gets a timeline report for application usage

Produces a timeline report for a __metricType__ over a specified time range.  The __from__ and __two__ parameters should be a URL encoded ISO-8601 combined date and time format (e.g. 2013-03-13T00%3A00%3A00Z).  The __metricType__ name is one of the types returned from [fields](#APIMetricsgetMetricFields).

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
api_instance = swagger_client.MetricsApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | The report type, either 'app' or 'api'
level = 56 # int | The report level (0 or 1 for drill-through)
_from = '_from_example' # str | The starting date/time for the report.
to = 'to_example' # str | The end date/time for the report.
metric_type = 'metric_type_example' # str | The metric type to query.
client = ['client_example'] # list[str] | Filter a specific client ID (multiple permitted). (optional)
service = ['service_example'] # list[str] | Filter a specific service name (multiple permitted). (optional)
method = 'method_example' # str | Filter a specific method. (optional)
organization = 'organization_example' # str | Filter a specific organziation. (optional)
reportsubtype = 'reportsubtype_example' # str | Define the report subtype. Allowed values are : 'original', 'trafficAll' or 'trafficSubset'. Defaults to 'original' if absent (optional)

try:
    # Gets a timeline report for application usage
    api_response = api_instance.metrics_reports_type_timeline_level_metric_type_get(type, level, _from, to, metric_type, client=client, service=service, method=method, organization=organization, reportsubtype=reportsubtype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->metrics_reports_type_timeline_level_metric_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The report type, either &#39;app&#39; or &#39;api&#39; | 
 **level** | **int**| The report level (0 or 1 for drill-through) | 
 **_from** | **str**| The starting date/time for the report. | 
 **to** | **str**| The end date/time for the report. | 
 **metric_type** | **str**| The metric type to query. | 
 **client** | [**list[str]**](str.md)| Filter a specific client ID (multiple permitted). | [optional] 
 **service** | [**list[str]**](str.md)| Filter a specific service name (multiple permitted). | [optional] 
 **method** | **str**| Filter a specific method. | [optional] 
 **organization** | **str**| Filter a specific organziation. | [optional] 
 **reportsubtype** | **str**| Define the report subtype. Allowed values are : &#39;original&#39;, &#39;trafficAll&#39; or &#39;trafficSubset&#39;. Defaults to &#39;original&#39; if absent | [optional] 

### Return type

[**MetricTimeline**](MetricTimeline.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

