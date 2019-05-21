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
from swagger_client.api.api_proxy_registration_api import APIProxyRegistrationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAPIProxyRegistrationApi(unittest.TestCase):
    """APIProxyRegistrationApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.api_proxy_registration_api.APIProxyRegistrationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_proxies_export_id_get(self):
        """Test case for proxies_export_id_get

        Downloads an API export.  # noqa: E501
        """
        pass

    def test_proxies_export_post(self):
        """Test case for proxies_export_post

        Creates an API export.  # noqa: E501
        """
        pass

    def test_proxies_get(self):
        """Test case for proxies_get

        Queries a list of frontend API.  # noqa: E501
        """
        pass

    def test_proxies_grantaccess_post(self):
        """Test case for proxies_grantaccess_post

        Macro function to grant API access.  # noqa: E501
        """
        pass

    def test_proxies_id_applications_get(self):
        """Test case for proxies_id_applications_get

        Gets a list of Applications that have been granted access to the specified frontend API.  # noqa: E501
        """
        pass

    def test_proxies_id_delete(self):
        """Test case for proxies_id_delete

        Deletes an API proxy.  # noqa: E501
        """
        pass

    def test_proxies_id_deprecate_post(self):
        """Test case for proxies_id_deprecate_post

        Deprecates the API.  # noqa: E501
        """
        pass

    def test_proxies_id_get(self):
        """Test case for proxies_id_get

        Gets a frontend API by ID.  # noqa: E501
        """
        pass

    def test_proxies_id_image_get(self):
        """Test case for proxies_id_image_get

        Gets the image for the API.  # noqa: E501
        """
        pass

    def test_proxies_id_image_post(self):
        """Test case for proxies_id_image_post

        Set the image for the frontend API.  # noqa: E501
        """
        pass

    def test_proxies_id_operations_get(self):
        """Test case for proxies_id_operations_get

        Gets a list of methods that are avilable to the API proxy.  # noqa: E501
        """
        pass

    def test_proxies_id_operations_operation_id_delete(self):
        """Test case for proxies_id_operations_operation_id_delete

        Deletes an API method by ID.  # noqa: E501
        """
        pass

    def test_proxies_id_operations_operation_id_get(self):
        """Test case for proxies_id_operations_operation_id_get

        Gets an API method by ID.  # noqa: E501
        """
        pass

    def test_proxies_id_operations_operation_id_put(self):
        """Test case for proxies_id_operations_operation_id_put

        Updates an API proxy operation.  # noqa: E501
        """
        pass

    def test_proxies_id_publish_post(self):
        """Test case for proxies_id_publish_post

        Publish the API.  # noqa: E501
        """
        pass

    def test_proxies_id_put(self):
        """Test case for proxies_id_put

        Updates an API proxy.  # noqa: E501
        """
        pass

    def test_proxies_id_undeprecate_post(self):
        """Test case for proxies_id_undeprecate_post

        Undeprecates the API.  # noqa: E501
        """
        pass

    def test_proxies_id_unpublish_post(self):
        """Test case for proxies_id_unpublish_post

        Unpublish the API.  # noqa: E501
        """
        pass

    def test_proxies_import_from_url_post(self):
        """Test case for proxies_import_from_url_post

        Imports a previously exported API.  # noqa: E501
        """
        pass

    def test_proxies_import_post(self):
        """Test case for proxies_import_post

        Imports a previously exported API.  # noqa: E501
        """
        pass

    def test_proxies_post(self):
        """Test case for proxies_post

        Creates a new API proxy from a backend API.  # noqa: E501
        """
        pass

    def test_proxies_promote_post(self):
        """Test case for proxies_promote_post

        Invokes the internal API promotion policy for the specified API.  # noqa: E501
        """
        pass

    def test_proxies_upgrade_id_post(self):
        """Test case for proxies_upgrade_id_post

        Upgrades an existing frontend API to a newer frontend API.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
