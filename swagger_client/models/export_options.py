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


class ExportOptions(object):
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
        'filename': 'str',
        'password': 'str',
        'app_ids': 'list[str]',
        'quota': 'bool',
        'oauth': 'bool',
        'apikeys': 'bool'
    }

    attribute_map = {
        'filename': 'filename',
        'password': 'password',
        'app_ids': 'appIds',
        'quota': 'quota',
        'oauth': 'oauth',
        'apikeys': 'apikeys'
    }

    def __init__(self, filename=None, password=None, app_ids=None, quota=False, oauth=False, apikeys=False):  # noqa: E501
        """ExportOptions - a model defined in Swagger"""  # noqa: E501

        self._filename = None
        self._password = None
        self._app_ids = None
        self._quota = None
        self._oauth = None
        self._apikeys = None
        self.discriminator = None

        if filename is not None:
            self.filename = filename
        if password is not None:
            self.password = password
        if app_ids is not None:
            self.app_ids = app_ids
        if quota is not None:
            self.quota = quota
        if oauth is not None:
            self.oauth = oauth
        if apikeys is not None:
            self.apikeys = apikeys

    @property
    def filename(self):
        """Gets the filename of this ExportOptions.  # noqa: E501

        If specified, the name of the file that the exported applications will be wrote to  # noqa: E501

        :return: The filename of this ExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this ExportOptions.

        If specified, the name of the file that the exported applications will be wrote to  # noqa: E501

        :param filename: The filename of this ExportOptions.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def password(self):
        """Gets the password of this ExportOptions.  # noqa: E501

        Password value which, when specified, will be use to encrypt the output stream for the export  # noqa: E501

        :return: The password of this ExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ExportOptions.

        Password value which, when specified, will be use to encrypt the output stream for the export  # noqa: E501

        :param password: The password of this ExportOptions.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def app_ids(self):
        """Gets the app_ids of this ExportOptions.  # noqa: E501

        List of the application ids that was chosen for export  # noqa: E501

        :return: The app_ids of this ExportOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._app_ids

    @app_ids.setter
    def app_ids(self, app_ids):
        """Sets the app_ids of this ExportOptions.

        List of the application ids that was chosen for export  # noqa: E501

        :param app_ids: The app_ids of this ExportOptions.  # noqa: E501
        :type: list[str]
        """

        self._app_ids = app_ids

    @property
    def quota(self):
        """Gets the quota of this ExportOptions.  # noqa: E501

        Flag to indicate if api quota information is to be included in the export  # noqa: E501

        :return: The quota of this ExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this ExportOptions.

        Flag to indicate if api quota information is to be included in the export  # noqa: E501

        :param quota: The quota of this ExportOptions.  # noqa: E501
        :type: bool
        """

        self._quota = quota

    @property
    def oauth(self):
        """Gets the oauth of this ExportOptions.  # noqa: E501

        Flag to indicate if oauth credentials are to be included in the export  # noqa: E501

        :return: The oauth of this ExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._oauth

    @oauth.setter
    def oauth(self, oauth):
        """Sets the oauth of this ExportOptions.

        Flag to indicate if oauth credentials are to be included in the export  # noqa: E501

        :param oauth: The oauth of this ExportOptions.  # noqa: E501
        :type: bool
        """

        self._oauth = oauth

    @property
    def apikeys(self):
        """Gets the apikeys of this ExportOptions.  # noqa: E501

        Flag to indicate if api keys are to be included in the export  # noqa: E501

        :return: The apikeys of this ExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._apikeys

    @apikeys.setter
    def apikeys(self, apikeys):
        """Sets the apikeys of this ExportOptions.

        Flag to indicate if api keys are to be included in the export  # noqa: E501

        :param apikeys: The apikeys of this ExportOptions.  # noqa: E501
        :type: bool
        """

        self._apikeys = apikeys

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
        if issubclass(ExportOptions, dict):
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
        if not isinstance(other, ExportOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
