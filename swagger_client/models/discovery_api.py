# coding: utf-8

"""
    API Manager API v1.3

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.3.0
    Contact: support@axway.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DiscoveryAPI(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'summary': 'str',
        'id': 'str',
        'uri': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'summary': 'summary',
        'id': 'id',
        'uri': 'uri',
        'type': 'type'
    }

    def __init__(self, name=None, summary=None, id=None, uri=None, type=None):  # noqa: E501
        """DiscoveryAPI - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._summary = None
        self._id = None
        self._uri = None
        self._type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if summary is not None:
            self.summary = summary
        if id is not None:
            self.id = id
        if uri is not None:
            self.uri = uri
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this DiscoveryAPI.  # noqa: E501

        The name of the API  # noqa: E501

        :return: The name of this DiscoveryAPI.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DiscoveryAPI.

        The name of the API  # noqa: E501

        :param name: The name of this DiscoveryAPI.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def summary(self):
        """Gets the summary of this DiscoveryAPI.  # noqa: E501

        Summary of the API  # noqa: E501

        :return: The summary of this DiscoveryAPI.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this DiscoveryAPI.

        Summary of the API  # noqa: E501

        :param summary: The summary of this DiscoveryAPI.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def id(self):
        """Gets the id of this DiscoveryAPI.  # noqa: E501

        The unique identifier for the API  # noqa: E501

        :return: The id of this DiscoveryAPI.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DiscoveryAPI.

        The unique identifier for the API  # noqa: E501

        :param id: The id of this DiscoveryAPI.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def uri(self):
        """Gets the uri of this DiscoveryAPI.  # noqa: E501

        The URL of where further information of the API is available in the portal  # noqa: E501

        :return: The uri of this DiscoveryAPI.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this DiscoveryAPI.

        The URL of where further information of the API is available in the portal  # noqa: E501

        :param uri: The uri of this DiscoveryAPI.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def type(self):
        """Gets the type of this DiscoveryAPI.  # noqa: E501

        The type of API, either rest or wsdl  # noqa: E501

        :return: The type of this DiscoveryAPI.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DiscoveryAPI.

        The type of API, either rest or wsdl  # noqa: E501

        :param type: The type of this DiscoveryAPI.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DiscoveryAPI, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DiscoveryAPI):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other