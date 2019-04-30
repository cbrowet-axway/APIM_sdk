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


class OAuthAppScope(object):
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
        'id': 'str',
        'application_id': 'str',
        'scope': 'str',
        'is_default': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'application_id': 'applicationId',
        'scope': 'scope',
        'is_default': 'isDefault'
    }

    def __init__(self, id=None, application_id=None, scope=None, is_default=False):  # noqa: E501
        """OAuthAppScope - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._application_id = None
        self._scope = None
        self._is_default = None
        self.discriminator = None

        self.id = id
        self.application_id = application_id
        if scope is not None:
            self.scope = scope
        if is_default is not None:
            self.is_default = is_default

    @property
    def id(self):
        """Gets the id of this OAuthAppScope.  # noqa: E501

        The unique identifier for the oauth protected resource  # noqa: E501

        :return: The id of this OAuthAppScope.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OAuthAppScope.

        The unique identifier for the oauth protected resource  # noqa: E501

        :param id: The id of this OAuthAppScope.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def application_id(self):
        """Gets the application_id of this OAuthAppScope.  # noqa: E501

        The unique identifier for the application that has this scope  # noqa: E501

        :return: The application_id of this OAuthAppScope.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this OAuthAppScope.

        The unique identifier for the application that has this scope  # noqa: E501

        :param application_id: The application_id of this OAuthAppScope.  # noqa: E501
        :type: str
        """
        if application_id is None:
            raise ValueError("Invalid value for `application_id`, must not be `None`")  # noqa: E501

        self._application_id = application_id

    @property
    def scope(self):
        """Gets the scope of this OAuthAppScope.  # noqa: E501

        The scope string  # noqa: E501

        :return: The scope of this OAuthAppScope.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this OAuthAppScope.

        The scope string  # noqa: E501

        :param scope: The scope of this OAuthAppScope.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def is_default(self):
        """Gets the is_default of this OAuthAppScope.  # noqa: E501

        Flag to indicate if this scope is one of the applications default scopes  # noqa: E501

        :return: The is_default of this OAuthAppScope.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this OAuthAppScope.

        Flag to indicate if this scope is one of the applications default scopes  # noqa: E501

        :param is_default: The is_default of this OAuthAppScope.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

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
        if issubclass(OAuthAppScope, dict):
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
        if not isinstance(other, OAuthAppScope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other