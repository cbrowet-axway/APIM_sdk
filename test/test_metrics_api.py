# coding: utf-8

"""
    API Manager API v1.3

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.3.0
    Contact: support@axway.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.metrics_api import MetricsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMetricsApi(unittest.TestCase):
    """MetricsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.metrics_api.MetricsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_metrics_fields_get(self):
        """Test case for metrics_fields_get

        Gets a list of metric field names available for summary and timeline queries.  # noqa: E501
        """
        pass

    def test_metrics_reports_type_summary_level_get(self):
        """Test case for metrics_reports_type_summary_level_get

        Gets a summary report for application usage  # noqa: E501
        """
        pass

    def test_metrics_reports_type_timeline_level_metric_type_get(self):
        """Test case for metrics_reports_type_timeline_level_metric_type_get

        Gets a timeline report for application usage  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
