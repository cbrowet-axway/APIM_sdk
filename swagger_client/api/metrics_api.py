# coding: utf-8

"""
    API Manager API v1.3

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.3.0
    Contact: support@axway.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class MetricsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def metrics_fields_get(self, **kwargs):  # noqa: E501
        """Gets a list of metric field names available for summary and timeline queries.  # noqa: E501

        Retrieves a set of metric fields that may be used when querying or interpreting the summary and timeline reports.  The __metricType__ is the metric name.  The __aggreggateName__ is the metric name for the aggregated __metricType__.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.metrics_fields_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[MetricField]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.metrics_fields_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.metrics_fields_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def metrics_fields_get_with_http_info(self, **kwargs):  # noqa: E501
        """Gets a list of metric field names available for summary and timeline queries.  # noqa: E501

        Retrieves a set of metric fields that may be used when querying or interpreting the summary and timeline reports.  The __metricType__ is the metric name.  The __aggreggateName__ is the metric name for the aggregated __metricType__.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.metrics_fields_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[MetricField]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method metrics_fields_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/metrics/fields', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MetricField]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def metrics_reports_type_summary_level_get(self, type, level, _from, to, **kwargs):  # noqa: E501
        """Gets a summary report for application usage  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.metrics_reports_type_summary_level_get(type, level, _from, to, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: The report type, either 'app' or 'api' (required)
        :param int level: The report level (0 or 1 for drill-through) (required)
        :param str _from: The starting date/time for the report. (required)
        :param str to: The end date/time for the report. (required)
        :param list[str] client: Filter a specific client ID (multiple permitted).
        :param list[str] service: Filter a specific service name (multiple permitted).
        :param str method: Filter a specific method.
        :param str organization: Filter a specific organziation.
        :param str reportsubtype: Define the report subtype. Allowed values are : 'original', 'trafficAll' or 'trafficSubset'. Defaults to 'original' if absent
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.metrics_reports_type_summary_level_get_with_http_info(type, level, _from, to, **kwargs)  # noqa: E501
        else:
            (data) = self.metrics_reports_type_summary_level_get_with_http_info(type, level, _from, to, **kwargs)  # noqa: E501
            return data

    def metrics_reports_type_summary_level_get_with_http_info(self, type, level, _from, to, **kwargs):  # noqa: E501
        """Gets a summary report for application usage  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.metrics_reports_type_summary_level_get_with_http_info(type, level, _from, to, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: The report type, either 'app' or 'api' (required)
        :param int level: The report level (0 or 1 for drill-through) (required)
        :param str _from: The starting date/time for the report. (required)
        :param str to: The end date/time for the report. (required)
        :param list[str] client: Filter a specific client ID (multiple permitted).
        :param list[str] service: Filter a specific service name (multiple permitted).
        :param str method: Filter a specific method.
        :param str organization: Filter a specific organziation.
        :param str reportsubtype: Define the report subtype. Allowed values are : 'original', 'trafficAll' or 'trafficSubset'. Defaults to 'original' if absent
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type', 'level', '_from', 'to', 'client', 'service', 'method', 'organization', 'reportsubtype']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method metrics_reports_type_summary_level_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `metrics_reports_type_summary_level_get`")  # noqa: E501
        # verify the required parameter 'level' is set
        if ('level' not in params or
                params['level'] is None):
            raise ValueError("Missing the required parameter `level` when calling `metrics_reports_type_summary_level_get`")  # noqa: E501
        # verify the required parameter '_from' is set
        if ('_from' not in params or
                params['_from'] is None):
            raise ValueError("Missing the required parameter `_from` when calling `metrics_reports_type_summary_level_get`")  # noqa: E501
        # verify the required parameter 'to' is set
        if ('to' not in params or
                params['to'] is None):
            raise ValueError("Missing the required parameter `to` when calling `metrics_reports_type_summary_level_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'type' in params:
            path_params['type'] = params['type']  # noqa: E501
        if 'level' in params:
            path_params['level'] = params['level']  # noqa: E501

        query_params = []
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501
        if 'client' in params:
            query_params.append(('client', params['client']))  # noqa: E501
            collection_formats['client'] = 'multi'  # noqa: E501
        if 'service' in params:
            query_params.append(('service', params['service']))  # noqa: E501
            collection_formats['service'] = 'multi'  # noqa: E501
        if 'method' in params:
            query_params.append(('method', params['method']))  # noqa: E501
        if 'organization' in params:
            query_params.append(('organization', params['organization']))  # noqa: E501
        if 'reportsubtype' in params:
            query_params.append(('reportsubtype', params['reportsubtype']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/metrics/reports/{type}/summary/{level}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def metrics_reports_type_timeline_level_metric_type_get(self, type, level, _from, to, metric_type, **kwargs):  # noqa: E501
        """Gets a timeline report for application usage  # noqa: E501

        Produces a timeline report for a __metricType__ over a specified time range.  The __from__ and __two__ parameters should be a URL encoded ISO-8601 combined date and time format (e.g. 2013-03-13T00%3A00%3A00Z).  The __metricType__ name is one of the types returned from [fields](#APIMetricsgetMetricFields).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.metrics_reports_type_timeline_level_metric_type_get(type, level, _from, to, metric_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: The report type, either 'app' or 'api' (required)
        :param int level: The report level (0 or 1 for drill-through) (required)
        :param str _from: The starting date/time for the report. (required)
        :param str to: The end date/time for the report. (required)
        :param str metric_type: The metric type to query. (required)
        :param list[str] client: Filter a specific client ID (multiple permitted).
        :param list[str] service: Filter a specific service name (multiple permitted).
        :param str method: Filter a specific method.
        :param str organization: Filter a specific organziation.
        :param str reportsubtype: Define the report subtype. Allowed values are : 'original', 'trafficAll' or 'trafficSubset'. Defaults to 'original' if absent
        :return: MetricTimeline
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.metrics_reports_type_timeline_level_metric_type_get_with_http_info(type, level, _from, to, metric_type, **kwargs)  # noqa: E501
        else:
            (data) = self.metrics_reports_type_timeline_level_metric_type_get_with_http_info(type, level, _from, to, metric_type, **kwargs)  # noqa: E501
            return data

    def metrics_reports_type_timeline_level_metric_type_get_with_http_info(self, type, level, _from, to, metric_type, **kwargs):  # noqa: E501
        """Gets a timeline report for application usage  # noqa: E501

        Produces a timeline report for a __metricType__ over a specified time range.  The __from__ and __two__ parameters should be a URL encoded ISO-8601 combined date and time format (e.g. 2013-03-13T00%3A00%3A00Z).  The __metricType__ name is one of the types returned from [fields](#APIMetricsgetMetricFields).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.metrics_reports_type_timeline_level_metric_type_get_with_http_info(type, level, _from, to, metric_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: The report type, either 'app' or 'api' (required)
        :param int level: The report level (0 or 1 for drill-through) (required)
        :param str _from: The starting date/time for the report. (required)
        :param str to: The end date/time for the report. (required)
        :param str metric_type: The metric type to query. (required)
        :param list[str] client: Filter a specific client ID (multiple permitted).
        :param list[str] service: Filter a specific service name (multiple permitted).
        :param str method: Filter a specific method.
        :param str organization: Filter a specific organziation.
        :param str reportsubtype: Define the report subtype. Allowed values are : 'original', 'trafficAll' or 'trafficSubset'. Defaults to 'original' if absent
        :return: MetricTimeline
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type', 'level', '_from', 'to', 'metric_type', 'client', 'service', 'method', 'organization', 'reportsubtype']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method metrics_reports_type_timeline_level_metric_type_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `metrics_reports_type_timeline_level_metric_type_get`")  # noqa: E501
        # verify the required parameter 'level' is set
        if ('level' not in params or
                params['level'] is None):
            raise ValueError("Missing the required parameter `level` when calling `metrics_reports_type_timeline_level_metric_type_get`")  # noqa: E501
        # verify the required parameter '_from' is set
        if ('_from' not in params or
                params['_from'] is None):
            raise ValueError("Missing the required parameter `_from` when calling `metrics_reports_type_timeline_level_metric_type_get`")  # noqa: E501
        # verify the required parameter 'to' is set
        if ('to' not in params or
                params['to'] is None):
            raise ValueError("Missing the required parameter `to` when calling `metrics_reports_type_timeline_level_metric_type_get`")  # noqa: E501
        # verify the required parameter 'metric_type' is set
        if ('metric_type' not in params or
                params['metric_type'] is None):
            raise ValueError("Missing the required parameter `metric_type` when calling `metrics_reports_type_timeline_level_metric_type_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'type' in params:
            path_params['type'] = params['type']  # noqa: E501
        if 'level' in params:
            path_params['level'] = params['level']  # noqa: E501
        if 'metric_type' in params:
            path_params['metricType'] = params['metric_type']  # noqa: E501

        query_params = []
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501
        if 'client' in params:
            query_params.append(('client', params['client']))  # noqa: E501
            collection_formats['client'] = 'multi'  # noqa: E501
        if 'service' in params:
            query_params.append(('service', params['service']))  # noqa: E501
            collection_formats['service'] = 'multi'  # noqa: E501
        if 'method' in params:
            query_params.append(('method', params['method']))  # noqa: E501
        if 'organization' in params:
            query_params.append(('organization', params['organization']))  # noqa: E501
        if 'reportsubtype' in params:
            query_params.append(('reportsubtype', params['reportsubtype']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/metrics/reports/{type}/timeline/{level}/{metricType}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MetricTimeline',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
