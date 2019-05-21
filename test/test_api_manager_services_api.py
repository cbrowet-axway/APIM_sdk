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
from swagger_client.api.api_manager_services_api import APIManagerServicesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAPIManagerServicesApi(unittest.TestCase):
    """APIManagerServicesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.api_manager_services_api.APIManagerServicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_alerts_get(self):
        """Test case for alerts_get

        Gets the alerts configured for the API Manager  # noqa: E501
        """
        pass

    def test_alerts_post(self):
        """Test case for alerts_post

        Updates the API Manager alerts configuration  # noqa: E501
        """
        pass

    def test_appinfo_get(self):
        """Test case for appinfo_get

        Gets API Manager feature information.  # noqa: E501
        """
        pass

    def test_certinfo_post(self):
        """Test case for certinfo_post

        Extracts certificate information from the supplied data  # noqa: E501
        """
        pass

    def test_config_customproperties_get(self):
        """Test case for config_customproperties_get

        Gets API Manager custom property metadata  # noqa: E501
        """
        pass

    def test_config_get(self):
        """Test case for config_get

        Gets API Manager configuration  # noqa: E501
        """
        pass

    def test_config_put(self):
        """Test case for config_put

        Updates the API Manager configuration  # noqa: E501
        """
        pass

    def test_connectors_connector_id_get(self):
        """Test case for connectors_connector_id_get

        Return a list of APIs for the specified connector  # noqa: E501
        """
        pass

    def test_connectors_connector_id_login_post(self):
        """Test case for connectors_connector_id_login_post

        Login to an external service from which APIs will be imported  # noqa: E501
        """
        pass

    def test_connectors_get(self):
        """Test case for connectors_get

        Return a list of API connectors  # noqa: E501
        """
        pass

    def test_filedata_post(self):
        """Test case for filedata_post

        Returns the DataURI representation of the uploaded file  # noqa: E501
        """
        pass

    def test_license_get(self):
        """Test case for license_get

        Checks that the API Manager has a valid license  # noqa: E501
        """
        pass

    def test_listeners_get(self):
        """Test case for listeners_get

        Gets the API Manager listeners  # noqa: E501
        """
        pass

    def test_oauthclientprofiles_get(self):
        """Test case for oauthclientprofiles_get

        Get a list of OAuth profiles for use in backend API authorisation  # noqa: E501
        """
        pass

    def test_policies_get(self):
        """Test case for policies_get

        Gets a list of the specified policies  # noqa: E501
        """
        pass

    def test_remotehosts_get(self):
        """Test case for remotehosts_get

        Returns a list of remote hosts  # noqa: E501
        """
        pass

    def test_remotehosts_id_delete(self):
        """Test case for remotehosts_id_delete

        Deletes a remote host.  # noqa: E501
        """
        pass

    def test_remotehosts_id_put(self):
        """Test case for remotehosts_id_put

        Updates a remote host  # noqa: E501
        """
        pass

    def test_remotehosts_post(self):
        """Test case for remotehosts_post

        Creates a new remote host  # noqa: E501
        """
        pass

    def test_service_discovery_instance_type_post(self):
        """Test case for service_discovery_instance_type_post

        Returns a list of services hosted on the specified Gateway instance  # noqa: E501
        """
        pass

    def test_sysconfig_get(self):
        """Test case for sysconfig_get

        Gets API Manager system configuration  # noqa: E501
        """
        pass

    def test_sysconfig_put(self):
        """Test case for sysconfig_put

        Update API Manager system configuration  # noqa: E501
        """
        pass

    def test_title_get(self):
        """Test case for title_get

        Gets the API Manager's title  # noqa: E501
        """
        pass

    def test_tokenstores_get(self):
        """Test case for tokenstores_get

        Gets a list of Token Stores  # noqa: E501
        """
        pass

    def test_topology_post(self):
        """Test case for topology_post

        Retrieves the Topology from the specified Admin Node Manager  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
