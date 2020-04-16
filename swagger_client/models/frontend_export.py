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


class FrontendExport(object):
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
        'apis': 'list[VirtualizedAPI]',
        'methods': 'list[VirtualizedMethodExport]',
        'backend_methods': 'list[BackendMethodExport]',
        'imagedata': 'dict(str, str)'
    }

    attribute_map = {
        'apis': 'apis',
        'methods': 'methods',
        'backend_methods': 'backendMethods',
        'imagedata': 'imagedata'
    }

    def __init__(self, apis=None, methods=None, backend_methods=None, imagedata=None):  # noqa: E501
        """FrontendExport - a model defined in Swagger"""  # noqa: E501

        self._apis = None
        self._methods = None
        self._backend_methods = None
        self._imagedata = None
        self.discriminator = None

        if apis is not None:
            self.apis = apis
        if methods is not None:
            self.methods = methods
        if backend_methods is not None:
            self.backend_methods = backend_methods
        if imagedata is not None:
            self.imagedata = imagedata

    @property
    def apis(self):
        """Gets the apis of this FrontendExport.  # noqa: E501

        List of frontend API  # noqa: E501

        :return: The apis of this FrontendExport.  # noqa: E501
        :rtype: list[VirtualizedAPI]
        """
        return self._apis

    @apis.setter
    def apis(self, apis):
        """Sets the apis of this FrontendExport.

        List of frontend API  # noqa: E501

        :param apis: The apis of this FrontendExport.  # noqa: E501
        :type: list[VirtualizedAPI]
        """

        self._apis = apis

    @property
    def methods(self):
        """Gets the methods of this FrontendExport.  # noqa: E501

        List of frontend API methods  # noqa: E501

        :return: The methods of this FrontendExport.  # noqa: E501
        :rtype: list[VirtualizedMethodExport]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """Sets the methods of this FrontendExport.

        List of frontend API methods  # noqa: E501

        :param methods: The methods of this FrontendExport.  # noqa: E501
        :type: list[VirtualizedMethodExport]
        """

        self._methods = methods

    @property
    def backend_methods(self):
        """Gets the backend_methods of this FrontendExport.  # noqa: E501

        List of backend API methods  # noqa: E501

        :return: The backend_methods of this FrontendExport.  # noqa: E501
        :rtype: list[BackendMethodExport]
        """
        return self._backend_methods

    @backend_methods.setter
    def backend_methods(self, backend_methods):
        """Sets the backend_methods of this FrontendExport.

        List of backend API methods  # noqa: E501

        :param backend_methods: The backend_methods of this FrontendExport.  # noqa: E501
        :type: list[BackendMethodExport]
        """

        self._backend_methods = backend_methods

    @property
    def imagedata(self):
        """Gets the imagedata of this FrontendExport.  # noqa: E501

        Image Export  # noqa: E501

        :return: The imagedata of this FrontendExport.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._imagedata

    @imagedata.setter
    def imagedata(self, imagedata):
        """Sets the imagedata of this FrontendExport.

        Image Export  # noqa: E501

        :param imagedata: The imagedata of this FrontendExport.  # noqa: E501
        :type: dict(str, str)
        """

        self._imagedata = imagedata

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
        if issubclass(FrontendExport, dict):
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
        if not isinstance(other, FrontendExport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
