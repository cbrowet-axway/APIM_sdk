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
from swagger_client.api.applications_api import ApplicationsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestApplicationsApi(unittest.TestCase):
    """ApplicationsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.applications_api.ApplicationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_applications_get(self):
        """Test case for applications_get

        Get the list of applications  # noqa: E501
        """
        pass

    def test_applications_id_apikeys_apikeyid_put(self):
        """Test case for applications_id_apikeys_apikeyid_put

        Updates an API Key  # noqa: E501
        """
        pass

    def test_applications_id_apikeys_get(self):
        """Test case for applications_id_apikeys_get

        Returns the API Keys associated with an application  # noqa: E501
        """
        pass

    def test_applications_id_apikeys_key_id_delete(self):
        """Test case for applications_id_apikeys_key_id_delete

        Delete an API Key  # noqa: E501
        """
        pass

    def test_applications_id_apikeys_post(self):
        """Test case for applications_id_apikeys_post

        Creates a new API Key and secret for the application  # noqa: E501
        """
        pass

    def test_applications_id_apis_api_access_id_approve_post(self):
        """Test case for applications_id_apis_api_access_id_approve_post

        Creates an API access request to an API for an application.  # noqa: E501
        """
        pass

    def test_applications_id_apis_api_access_id_delete(self):
        """Test case for applications_id_apis_api_access_id_delete

        Deletes access to an API for an application  # noqa: E501
        """
        pass

    def test_applications_id_apis_api_access_id_put(self):
        """Test case for applications_id_apis_api_access_id_put

        Updates access to an API for an application  # noqa: E501
        """
        pass

    def test_applications_id_apis_get(self):
        """Test case for applications_id_apis_get

        Get the list of APIs that the application can access  # noqa: E501
        """
        pass

    def test_applications_id_apis_post(self):
        """Test case for applications_id_apis_post

        Create a request for an application to access an API.  # noqa: E501
        """
        pass

    def test_applications_id_approve_post(self):
        """Test case for applications_id_approve_post

        Approves a pending application request  # noqa: E501
        """
        pass

    def test_applications_id_availablescopes_get(self):
        """Test case for applications_id_availablescopes_get

        Returns the scopes available to an application  # noqa: E501
        """
        pass

    def test_applications_id_delete(self):
        """Test case for applications_id_delete

        Delete an application  # noqa: E501
        """
        pass

    def test_applications_id_extclients_get(self):
        """Test case for applications_id_extclients_get

        Returns the external clients associated with an application  # noqa: E501
        """
        pass

    def test_applications_id_extclients_object_id_delete(self):
        """Test case for applications_id_extclients_object_id_delete

        Delete an external client  # noqa: E501
        """
        pass

    def test_applications_id_extclients_object_id_put(self):
        """Test case for applications_id_extclients_object_id_put

        Updates an external client for the application  # noqa: E501
        """
        pass

    def test_applications_id_extclients_post(self):
        """Test case for applications_id_extclients_post

        Maps a new external client to the application  # noqa: E501
        """
        pass

    def test_applications_id_get(self):
        """Test case for applications_id_get

        Get an application  # noqa: E501
        """
        pass

    def test_applications_id_image_get(self):
        """Test case for applications_id_image_get

        Get the image for an application  # noqa: E501
        """
        pass

    def test_applications_id_image_post(self):
        """Test case for applications_id_image_post

        Adds a JPEG image to an application  # noqa: E501
        """
        pass

    def test_applications_id_oauth_client_id_put(self):
        """Test case for applications_id_oauth_client_id_put

        Updates an OAuth Credential for the application  # noqa: E501
        """
        pass

    def test_applications_id_oauth_clientid_newsecret_put(self):
        """Test case for applications_id_oauth_clientid_newsecret_put

        Updates an OAuth Credential for an application by generating a new secret  # noqa: E501
        """
        pass

    def test_applications_id_oauth_get(self):
        """Test case for applications_id_oauth_get

        Returns the OAuth Credentials associated with an application  # noqa: E501
        """
        pass

    def test_applications_id_oauth_oauth_id_delete(self):
        """Test case for applications_id_oauth_oauth_id_delete

        Delete an OAuth client ID and secret  # noqa: E501
        """
        pass

    def test_applications_id_oauth_post(self):
        """Test case for applications_id_oauth_post

        Creates a new OAuth client ID and secret for the application  # noqa: E501
        """
        pass

    def test_applications_id_oauthresource_get(self):
        """Test case for applications_id_oauthresource_get

        Returns the OAuth protected resources (scopes) associated with an application  # noqa: E501
        """
        pass

    def test_applications_id_oauthresource_post(self):
        """Test case for applications_id_oauthresource_post

        Adds an OAuth protected resource to an application  # noqa: E501
        """
        pass

    def test_applications_id_oauthresource_resource_id_delete(self):
        """Test case for applications_id_oauthresource_resource_id_delete

        Remove an OAuth protected resource from an application  # noqa: E501
        """
        pass

    def test_applications_id_oauthresource_resource_id_put(self):
        """Test case for applications_id_oauthresource_resource_id_put

        Updates a protected resource associate with an application, sets enabled to true/false  # noqa: E501
        """
        pass

    def test_applications_id_permissions_get(self):
        """Test case for applications_id_permissions_get

        Get the list of permissions.  # noqa: E501
        """
        pass

    def test_applications_id_permissions_perm_id_delete(self):
        """Test case for applications_id_permissions_perm_id_delete

        Remove a permission  # noqa: E501
        """
        pass

    def test_applications_id_permissions_perm_id_put(self):
        """Test case for applications_id_permissions_perm_id_put

        Modify a permission  # noqa: E501
        """
        pass

    def test_applications_id_permissions_post(self):
        """Test case for applications_id_permissions_post

        Create a new permission.  # noqa: E501
        """
        pass

    def test_applications_id_put(self):
        """Test case for applications_id_put

        Update an application  # noqa: E501
        """
        pass

    def test_applications_id_quota_delete(self):
        """Test case for applications_id_quota_delete

        Deletes a quota from an application  # noqa: E501
        """
        pass

    def test_applications_id_quota_get(self):
        """Test case for applications_id_quota_get

        Returns the quota associated with an application.  # noqa: E501
        """
        pass

    def test_applications_id_quota_post(self):
        """Test case for applications_id_quota_post

        Creates a new quota constraint for the application  # noqa: E501
        """
        pass

    def test_applications_id_quota_put(self):
        """Test case for applications_id_quota_put

        Updates a quota contraint for an application  # noqa: E501
        """
        pass

    def test_applications_id_scope_get(self):
        """Test case for applications_id_scope_get

        Returns the scopes associated with an application  # noqa: E501
        """
        pass

    def test_applications_id_scope_post(self):
        """Test case for applications_id_scope_post

        Adds an OAuth protected resource to an application  # noqa: E501
        """
        pass

    def test_applications_id_scope_scope_id_delete(self):
        """Test case for applications_id_scope_scope_id_delete

        Remove an OAuth protected resource from an application  # noqa: E501
        """
        pass

    def test_applications_id_scope_scope_id_put(self):
        """Test case for applications_id_scope_scope_id_put

        Updates a scope associated with an application, sets default to true/false  # noqa: E501
        """
        pass

    def test_applications_oauthclient_client_id_get(self):
        """Test case for applications_oauthclient_client_id_get

        Get an application associated with an OAuth Client ID  # noqa: E501
        """
        pass

    def test_applications_post(self):
        """Test case for applications_post

        Creates a new application.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
