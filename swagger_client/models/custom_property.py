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

from swagger_client.models.custom_property_option import CustomPropertyOption  # noqa: F401,E501
from swagger_client.models.custom_property_permission import CustomPropertyPermission  # noqa: F401,E501


class CustomProperty(object):
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
        'label': 'str',
        'type': 'str',
        'disabled': 'bool',
        'required': 'bool',
        'help': 'str',
        'permissions': 'dict(str, CustomPropertyPermission)',
        'options': 'list[CustomPropertyOption]',
        'default_value': 'object',
        'regex': 'str',
        'min_value': 'object',
        'max_value': 'object',
        'decimal_places': 'int',
        'error': 'str',
        'custom': 'object'
    }

    attribute_map = {
        'label': 'label',
        'type': 'type',
        'disabled': 'disabled',
        'required': 'required',
        'help': 'help',
        'permissions': 'permissions',
        'options': 'options',
        'default_value': 'defaultValue',
        'regex': 'regex',
        'min_value': 'minValue',
        'max_value': 'maxValue',
        'decimal_places': 'decimalPlaces',
        'error': 'error',
        'custom': 'custom'
    }

    def __init__(self, label=None, type=None, disabled=False, required=False, help=None, permissions=None, options=None, default_value=None, regex=None, min_value=None, max_value=None, decimal_places=None, error=None, custom=None):  # noqa: E501
        """CustomProperty - a model defined in Swagger"""  # noqa: E501

        self._label = None
        self._type = None
        self._disabled = None
        self._required = None
        self._help = None
        self._permissions = None
        self._options = None
        self._default_value = None
        self._regex = None
        self._min_value = None
        self._max_value = None
        self._decimal_places = None
        self._error = None
        self._custom = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if type is not None:
            self.type = type
        if disabled is not None:
            self.disabled = disabled
        if required is not None:
            self.required = required
        if help is not None:
            self.help = help
        if permissions is not None:
            self.permissions = permissions
        if options is not None:
            self.options = options
        if default_value is not None:
            self.default_value = default_value
        if regex is not None:
            self.regex = regex
        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value
        if decimal_places is not None:
            self.decimal_places = decimal_places
        if error is not None:
            self.error = error
        if custom is not None:
            self.custom = custom

    @property
    def label(self):
        """Gets the label of this CustomProperty.  # noqa: E501

        The label for the custom property, which will be displayed in the API Manager UI  # noqa: E501

        :return: The label of this CustomProperty.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CustomProperty.

        The label for the custom property, which will be displayed in the API Manager UI  # noqa: E501

        :param label: The label of this CustomProperty.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this CustomProperty.  # noqa: E501

        The type of the custom property. Can be one of the following values: ['custom', 'switch', 'select', 'number']. Default value is 'custom' (i.e. free-form text)  # noqa: E501

        :return: The type of this CustomProperty.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CustomProperty.

        The type of the custom property. Can be one of the following values: ['custom', 'switch', 'select', 'number']. Default value is 'custom' (i.e. free-form text)  # noqa: E501

        :param type: The type of this CustomProperty.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def disabled(self):
        """Gets the disabled of this CustomProperty.  # noqa: E501

        Specifies whether the custom property is disabled. Default value is false  # noqa: E501

        :return: The disabled of this CustomProperty.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this CustomProperty.

        Specifies whether the custom property is disabled. Default value is false  # noqa: E501

        :param disabled: The disabled of this CustomProperty.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def required(self):
        """Gets the required of this CustomProperty.  # noqa: E501

        Specifies whether the custom property is required or optional. Default value is false  # noqa: E501

        :return: The required of this CustomProperty.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this CustomProperty.

        Specifies whether the custom property is required or optional. Default value is false  # noqa: E501

        :param required: The required of this CustomProperty.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def help(self):
        """Gets the help of this CustomProperty.  # noqa: E501

        Specifies the help text for the custom property that will appear in the API Manager UI. This field is optional  # noqa: E501

        :return: The help of this CustomProperty.  # noqa: E501
        :rtype: str
        """
        return self._help

    @help.setter
    def help(self, help):
        """Sets the help of this CustomProperty.

        Specifies the help text for the custom property that will appear in the API Manager UI. This field is optional  # noqa: E501

        :param help: The help of this CustomProperty.  # noqa: E501
        :type: str
        """

        self._help = help

    @property
    def permissions(self):
        """Gets the permissions of this CustomProperty.  # noqa: E501

        Specifies the read/write permissions per role (admin, oadmin and user) for the custom property. This field is optional. By default all roles have read/write access  # noqa: E501

        :return: The permissions of this CustomProperty.  # noqa: E501
        :rtype: dict(str, CustomPropertyPermission)
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this CustomProperty.

        Specifies the read/write permissions per role (admin, oadmin and user) for the custom property. This field is optional. By default all roles have read/write access  # noqa: E501

        :param permissions: The permissions of this CustomProperty.  # noqa: E501
        :type: dict(str, CustomPropertyPermission)
        """

        self._permissions = permissions

    @property
    def options(self):
        """Gets the options of this CustomProperty.  # noqa: E501

        Specifies the options for 'switch' and 'select' custom properties which will be available in the API Manager UI. This field is conditional and only required for custom properties of type 'switch' or 'select', otherwise it is ignored.  # noqa: E501

        :return: The options of this CustomProperty.  # noqa: E501
        :rtype: list[CustomPropertyOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this CustomProperty.

        Specifies the options for 'switch' and 'select' custom properties which will be available in the API Manager UI. This field is conditional and only required for custom properties of type 'switch' or 'select', otherwise it is ignored.  # noqa: E501

        :param options: The options of this CustomProperty.  # noqa: E501
        :type: list[CustomPropertyOption]
        """

        self._options = options

    @property
    def default_value(self):
        """Gets the default_value of this CustomProperty.  # noqa: E501

        Specifies the default value for the custom property. This field is optional, but recommended. This type of this field depends on the type of the custom property. It can be one of the following: string, integer, double, boolean  # noqa: E501

        :return: The default_value of this CustomProperty.  # noqa: E501
        :rtype: object
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this CustomProperty.

        Specifies the default value for the custom property. This field is optional, but recommended. This type of this field depends on the type of the custom property. It can be one of the following: string, integer, double, boolean  # noqa: E501

        :param default_value: The default_value of this CustomProperty.  # noqa: E501
        :type: object
        """

        self._default_value = default_value

    @property
    def regex(self):
        """Gets the regex of this CustomProperty.  # noqa: E501

        Specifies a validation regular expression for custom properties of type 'custom'. This field is conditional, i.e. optional for custom properties of type 'custom', otherwise ignored  # noqa: E501

        :return: The regex of this CustomProperty.  # noqa: E501
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        """Sets the regex of this CustomProperty.

        Specifies a validation regular expression for custom properties of type 'custom'. This field is conditional, i.e. optional for custom properties of type 'custom', otherwise ignored  # noqa: E501

        :param regex: The regex of this CustomProperty.  # noqa: E501
        :type: str
        """

        self._regex = regex

    @property
    def min_value(self):
        """Gets the min_value of this CustomProperty.  # noqa: E501

        Specifies a validation minimum value for custom properties of type 'number'. Can be an integer, a floating point number, or a string represation of an integer or floating point number. This field is conditional, i.e. optional for custom properties of type 'number', otherwise ignored. minValue and maxValue must both be of the same type so as to avoid unexpected behaviour during validation. Scientific notation is not supported.  # noqa: E501

        :return: The min_value of this CustomProperty.  # noqa: E501
        :rtype: object
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this CustomProperty.

        Specifies a validation minimum value for custom properties of type 'number'. Can be an integer, a floating point number, or a string represation of an integer or floating point number. This field is conditional, i.e. optional for custom properties of type 'number', otherwise ignored. minValue and maxValue must both be of the same type so as to avoid unexpected behaviour during validation. Scientific notation is not supported.  # noqa: E501

        :param min_value: The min_value of this CustomProperty.  # noqa: E501
        :type: object
        """

        self._min_value = min_value

    @property
    def max_value(self):
        """Gets the max_value of this CustomProperty.  # noqa: E501

        Specifies a validation maximum value for custom properties of type 'number'. Can be an integer, a floating point number, or a string represation of an integer or floating point number. This field is conditional, i.e. optional for custom properties of type 'number', otherwise ignored. minValue and maxValue must both be of the same type so as to avoid unexpected behaviour during validation. Scientific notation is not supported.  # noqa: E501

        :return: The max_value of this CustomProperty.  # noqa: E501
        :rtype: object
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this CustomProperty.

        Specifies a validation maximum value for custom properties of type 'number'. Can be an integer, a floating point number, or a string represation of an integer or floating point number. This field is conditional, i.e. optional for custom properties of type 'number', otherwise ignored. minValue and maxValue must both be of the same type so as to avoid unexpected behaviour during validation. Scientific notation is not supported.  # noqa: E501

        :param max_value: The max_value of this CustomProperty.  # noqa: E501
        :type: object
        """

        self._max_value = max_value

    @property
    def decimal_places(self):
        """Gets the decimal_places of this CustomProperty.  # noqa: E501

        Specifies the number of decimal places to be used when validating 'number' fields. Default value is 0, which indicates that the value is a whole number.  # noqa: E501

        :return: The decimal_places of this CustomProperty.  # noqa: E501
        :rtype: int
        """
        return self._decimal_places

    @decimal_places.setter
    def decimal_places(self, decimal_places):
        """Sets the decimal_places of this CustomProperty.

        Specifies the number of decimal places to be used when validating 'number' fields. Default value is 0, which indicates that the value is a whole number.  # noqa: E501

        :param decimal_places: The decimal_places of this CustomProperty.  # noqa: E501
        :type: int
        """

        self._decimal_places = decimal_places

    @property
    def error(self):
        """Gets the error of this CustomProperty.  # noqa: E501

        Specifies an error message which will appear when input validation fails. The format of this field is a string. This field is only valid for custom properties of type 'custom' and 'number', otherwise ignored  # noqa: E501

        :return: The error of this CustomProperty.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this CustomProperty.

        Specifies an error message which will appear when input validation fails. The format of this field is a string. This field is only valid for custom properties of type 'custom' and 'number', otherwise ignored  # noqa: E501

        :param error: The error of this CustomProperty.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def custom(self):
        """Gets the custom of this CustomProperty.  # noqa: E501

        Optional field allowing for the definition of custom metadata for the custom property. This will be used by clients other than API Manager, but API Manager may populate this field with API Manager-specific values in the future. If present, must be a valid JSON 'object'.  # noqa: E501

        :return: The custom of this CustomProperty.  # noqa: E501
        :rtype: object
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this CustomProperty.

        Optional field allowing for the definition of custom metadata for the custom property. This will be used by clients other than API Manager, but API Manager may populate this field with API Manager-specific values in the future. If present, must be a valid JSON 'object'.  # noqa: E501

        :param custom: The custom of this CustomProperty.  # noqa: E501
        :type: object
        """

        self._custom = custom

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
        if issubclass(CustomProperty, dict):
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
        if not isinstance(other, CustomProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other