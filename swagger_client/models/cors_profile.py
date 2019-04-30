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


class CORSProfile(object):
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
        'is_default': 'bool',
        'origins': 'list[str]',
        'allowed_headers': 'list[str]',
        'exposed_headers': 'list[str]',
        'support_credentials': 'bool',
        'max_age_seconds': 'int'
    }

    attribute_map = {
        'name': 'name',
        'is_default': 'isDefault',
        'origins': 'origins',
        'allowed_headers': 'allowedHeaders',
        'exposed_headers': 'exposedHeaders',
        'support_credentials': 'supportCredentials',
        'max_age_seconds': 'maxAgeSeconds'
    }

    def __init__(self, name=None, is_default=False, origins=None, allowed_headers=None, exposed_headers=None, support_credentials=False, max_age_seconds=None):  # noqa: E501
        """CORSProfile - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._is_default = None
        self._origins = None
        self._allowed_headers = None
        self._exposed_headers = None
        self._support_credentials = None
        self._max_age_seconds = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if is_default is not None:
            self.is_default = is_default
        if origins is not None:
            self.origins = origins
        if allowed_headers is not None:
            self.allowed_headers = allowed_headers
        if exposed_headers is not None:
            self.exposed_headers = exposed_headers
        if support_credentials is not None:
            self.support_credentials = support_credentials
        if max_age_seconds is not None:
            self.max_age_seconds = max_age_seconds

    @property
    def name(self):
        """Gets the name of this CORSProfile.  # noqa: E501

        Unique name of the Profile  # noqa: E501

        :return: The name of this CORSProfile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CORSProfile.

        Unique name of the Profile  # noqa: E501

        :param name: The name of this CORSProfile.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_default(self):
        """Gets the is_default of this CORSProfile.  # noqa: E501

        Indicates that this is the default profile.  There can be only one default.  # noqa: E501

        :return: The is_default of this CORSProfile.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this CORSProfile.

        Indicates that this is the default profile.  There can be only one default.  # noqa: E501

        :param is_default: The is_default of this CORSProfile.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def origins(self):
        """Gets the origins of this CORSProfile.  # noqa: E501

        List of origins for this CORS Profile  # noqa: E501

        :return: The origins of this CORSProfile.  # noqa: E501
        :rtype: list[str]
        """
        return self._origins

    @origins.setter
    def origins(self, origins):
        """Sets the origins of this CORSProfile.

        List of origins for this CORS Profile  # noqa: E501

        :param origins: The origins of this CORSProfile.  # noqa: E501
        :type: list[str]
        """

        self._origins = origins

    @property
    def allowed_headers(self):
        """Gets the allowed_headers of this CORSProfile.  # noqa: E501

        List of headers...  # noqa: E501

        :return: The allowed_headers of this CORSProfile.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_headers

    @allowed_headers.setter
    def allowed_headers(self, allowed_headers):
        """Sets the allowed_headers of this CORSProfile.

        List of headers...  # noqa: E501

        :param allowed_headers: The allowed_headers of this CORSProfile.  # noqa: E501
        :type: list[str]
        """

        self._allowed_headers = allowed_headers

    @property
    def exposed_headers(self):
        """Gets the exposed_headers of this CORSProfile.  # noqa: E501

        List of headers...  # noqa: E501

        :return: The exposed_headers of this CORSProfile.  # noqa: E501
        :rtype: list[str]
        """
        return self._exposed_headers

    @exposed_headers.setter
    def exposed_headers(self, exposed_headers):
        """Sets the exposed_headers of this CORSProfile.

        List of headers...  # noqa: E501

        :param exposed_headers: The exposed_headers of this CORSProfile.  # noqa: E501
        :type: list[str]
        """

        self._exposed_headers = exposed_headers

    @property
    def support_credentials(self):
        """Gets the support_credentials of this CORSProfile.  # noqa: E501

        Specifies whether or credentials are supported for APIs/API Methods employing this CORS Profile.  # noqa: E501

        :return: The support_credentials of this CORSProfile.  # noqa: E501
        :rtype: bool
        """
        return self._support_credentials

    @support_credentials.setter
    def support_credentials(self, support_credentials):
        """Sets the support_credentials of this CORSProfile.

        Specifies whether or credentials are supported for APIs/API Methods employing this CORS Profile.  # noqa: E501

        :param support_credentials: The support_credentials of this CORSProfile.  # noqa: E501
        :type: bool
        """

        self._support_credentials = support_credentials

    @property
    def max_age_seconds(self):
        """Gets the max_age_seconds of this CORSProfile.  # noqa: E501

        Specifies the amount of time responses to OPTIONS requests are stored, in seconds, in the preflight result cache  # noqa: E501

        :return: The max_age_seconds of this CORSProfile.  # noqa: E501
        :rtype: int
        """
        return self._max_age_seconds

    @max_age_seconds.setter
    def max_age_seconds(self, max_age_seconds):
        """Sets the max_age_seconds of this CORSProfile.

        Specifies the amount of time responses to OPTIONS requests are stored, in seconds, in the preflight result cache  # noqa: E501

        :param max_age_seconds: The max_age_seconds of this CORSProfile.  # noqa: E501
        :type: int
        """

        self._max_age_seconds = max_age_seconds

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
        if issubclass(CORSProfile, dict):
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
        if not isinstance(other, CORSProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other