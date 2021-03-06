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
from swagger_client.api.quotas_api import QuotasApi  # noqa: E501
from swagger_client.rest import ApiException


class TestQuotasApi(unittest.TestCase):
    """QuotasApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.quotas_api.QuotasApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_quotas_get(self):
        """Test case for quotas_get

        Returns all quotas  # noqa: E501
        """
        pass

    def test_quotas_id_delete(self):
        """Test case for quotas_id_delete

        Deletes a quota  # noqa: E501
        """
        pass

    def test_quotas_id_get(self):
        """Test case for quotas_id_get

        Returns the quota with the given ID  # noqa: E501
        """
        pass

    def test_quotas_id_put(self):
        """Test case for quotas_id_put

        Updates a quota  # noqa: E501
        """
        pass

    def test_quotas_post(self):
        """Test case for quotas_post

        Creates a new quota  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
