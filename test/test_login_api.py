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
from swagger_client.api.login_api import LoginApi  # noqa: E501
from swagger_client.rest import ApiException


class TestLoginApi(unittest.TestCase):
    """LoginApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.login_api.LoginApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_login_delete(self):
        """Test case for login_delete

        Logout from API Manager  # noqa: E501
        """
        pass

    def test_login_post(self):
        """Test case for login_post

        Login to API Manager  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
