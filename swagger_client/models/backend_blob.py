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


class BackendBlob(object):
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
        'type': 'str',
        'blob': 'str',
        'name': 'str',
        'import_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'blob': 'blob',
        'name': 'name',
        'import_url': 'importURL'
    }

    def __init__(self, id=None, type=None, blob=None, name=None, import_url=None):  # noqa: E501
        """BackendBlob - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._type = None
        self._blob = None
        self._name = None
        self._import_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if blob is not None:
            self.blob = blob
        if name is not None:
            self.name = name
        if import_url is not None:
            self.import_url = import_url

    @property
    def id(self):
        """Gets the id of this BackendBlob.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The id of this BackendBlob.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BackendBlob.

        Unique identifier  # noqa: E501

        :param id: The id of this BackendBlob.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this BackendBlob.  # noqa: E501

        Type of blob  # noqa: E501

        :return: The type of this BackendBlob.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BackendBlob.

        Type of blob  # noqa: E501

        :param type: The type of this BackendBlob.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def blob(self):
        """Gets the blob of this BackendBlob.  # noqa: E501

        Base64 encoded API  # noqa: E501

        :return: The blob of this BackendBlob.  # noqa: E501
        :rtype: str
        """
        return self._blob

    @blob.setter
    def blob(self, blob):
        """Sets the blob of this BackendBlob.

        Base64 encoded API  # noqa: E501

        :param blob: The blob of this BackendBlob.  # noqa: E501
        :type: str
        """

        self._blob = blob

    @property
    def name(self):
        """Gets the name of this BackendBlob.  # noqa: E501

        API name  # noqa: E501

        :return: The name of this BackendBlob.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BackendBlob.

        API name  # noqa: E501

        :param name: The name of this BackendBlob.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def import_url(self):
        """Gets the import_url of this BackendBlob.  # noqa: E501

        Original URL  # noqa: E501

        :return: The import_url of this BackendBlob.  # noqa: E501
        :rtype: str
        """
        return self._import_url

    @import_url.setter
    def import_url(self, import_url):
        """Sets the import_url of this BackendBlob.

        Original URL  # noqa: E501

        :param import_url: The import_url of this BackendBlob.  # noqa: E501
        :type: str
        """

        self._import_url = import_url

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
        if issubclass(BackendBlob, dict):
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
        if not isinstance(other, BackendBlob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
