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


class Parameter(object):
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
        'type': 'str',
        'format': 'str',
        'description': 'str',
        'required': 'bool',
        'allow_multiple': 'bool',
        'items': 'SchemaObject',
        'default_value': 'object',
        'max_length': 'int',
        'min_length': 'int',
        'pattern': 'str',
        'exclusive_minimum': 'bool',
        'exclusive_maximum': 'bool',
        'minimum': 'object',
        'maximum': 'object',
        'multiple_of': 'Number',
        'max_items': 'int',
        'min_items': 'int',
        'unique_items': 'bool',
        'collection_format': 'str',
        'schema': 'SchemaObject',
        'enum': 'list[object]',
        'param_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'format': 'format',
        'description': 'description',
        'required': 'required',
        'allow_multiple': 'allowMultiple',
        'items': 'items',
        'default_value': 'defaultValue',
        'max_length': 'maxLength',
        'min_length': 'minLength',
        'pattern': 'pattern',
        'exclusive_minimum': 'exclusiveMinimum',
        'exclusive_maximum': 'exclusiveMaximum',
        'minimum': 'minimum',
        'maximum': 'maximum',
        'multiple_of': 'multipleOf',
        'max_items': 'maxItems',
        'min_items': 'minItems',
        'unique_items': 'uniqueItems',
        'collection_format': 'collectionFormat',
        'schema': 'schema',
        'enum': 'enum',
        'param_type': 'paramType'
    }

    def __init__(self, name=None, type=None, format=None, description=None, required=False, allow_multiple=False, items=None, default_value=None, max_length=None, min_length=None, pattern=None, exclusive_minimum=False, exclusive_maximum=False, minimum=None, maximum=None, multiple_of=None, max_items=None, min_items=None, unique_items=False, collection_format=None, schema=None, enum=None, param_type=None):  # noqa: E501
        """Parameter - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._type = None
        self._format = None
        self._description = None
        self._required = None
        self._allow_multiple = None
        self._items = None
        self._default_value = None
        self._max_length = None
        self._min_length = None
        self._pattern = None
        self._exclusive_minimum = None
        self._exclusive_maximum = None
        self._minimum = None
        self._maximum = None
        self._multiple_of = None
        self._max_items = None
        self._min_items = None
        self._unique_items = None
        self._collection_format = None
        self._schema = None
        self._enum = None
        self._param_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if format is not None:
            self.format = format
        if description is not None:
            self.description = description
        if required is not None:
            self.required = required
        if allow_multiple is not None:
            self.allow_multiple = allow_multiple
        if items is not None:
            self.items = items
        if default_value is not None:
            self.default_value = default_value
        if max_length is not None:
            self.max_length = max_length
        if min_length is not None:
            self.min_length = min_length
        if pattern is not None:
            self.pattern = pattern
        if exclusive_minimum is not None:
            self.exclusive_minimum = exclusive_minimum
        if exclusive_maximum is not None:
            self.exclusive_maximum = exclusive_maximum
        if minimum is not None:
            self.minimum = minimum
        if maximum is not None:
            self.maximum = maximum
        if multiple_of is not None:
            self.multiple_of = multiple_of
        if max_items is not None:
            self.max_items = max_items
        if min_items is not None:
            self.min_items = min_items
        if unique_items is not None:
            self.unique_items = unique_items
        if collection_format is not None:
            self.collection_format = collection_format
        if schema is not None:
            self.schema = schema
        if enum is not None:
            self.enum = enum
        if param_type is not None:
            self.param_type = param_type

    @property
    def name(self):
        """Gets the name of this Parameter.  # noqa: E501

        The parameter name.  # noqa: E501

        :return: The name of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Parameter.

        The parameter name.  # noqa: E501

        :param name: The name of this Parameter.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this Parameter.  # noqa: E501

        The parameter data type, e.g. *boolean*, *byte*, *date*, *double*, *float*, *integer*, *long*, *string*, or a type name found in [APIDefinition models](APIDefinition.html#models).  # noqa: E501

        :return: The type of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Parameter.

        The parameter data type, e.g. *boolean*, *byte*, *date*, *double*, *float*, *integer*, *long*, *string*, or a type name found in [APIDefinition models](APIDefinition.html#models).  # noqa: E501

        :param type: The type of this Parameter.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def format(self):
        """Gets the format of this Parameter.  # noqa: E501


        :return: The format of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Parameter.


        :param format: The format of this Parameter.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def description(self):
        """Gets the description of this Parameter.  # noqa: E501


        :return: The description of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Parameter.


        :param description: The description of this Parameter.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def required(self):
        """Gets the required of this Parameter.  # noqa: E501

        Indicates that the parameter is required  # noqa: E501

        :return: The required of this Parameter.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this Parameter.

        Indicates that the parameter is required  # noqa: E501

        :param required: The required of this Parameter.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def allow_multiple(self):
        """Gets the allow_multiple of this Parameter.  # noqa: E501

        Indicates that the parameter can be included multiple times (e.g. query or form)  # noqa: E501

        :return: The allow_multiple of this Parameter.  # noqa: E501
        :rtype: bool
        """
        return self._allow_multiple

    @allow_multiple.setter
    def allow_multiple(self, allow_multiple):
        """Sets the allow_multiple of this Parameter.

        Indicates that the parameter can be included multiple times (e.g. query or form)  # noqa: E501

        :param allow_multiple: The allow_multiple of this Parameter.  # noqa: E501
        :type: bool
        """

        self._allow_multiple = allow_multiple

    @property
    def items(self):
        """Gets the items of this Parameter.  # noqa: E501


        :return: The items of this Parameter.  # noqa: E501
        :rtype: SchemaObject
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Parameter.


        :param items: The items of this Parameter.  # noqa: E501
        :type: SchemaObject
        """

        self._items = items

    @property
    def default_value(self):
        """Gets the default_value of this Parameter.  # noqa: E501

        Provides a default value for the parameter  # noqa: E501

        :return: The default_value of this Parameter.  # noqa: E501
        :rtype: object
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this Parameter.

        Provides a default value for the parameter  # noqa: E501

        :param default_value: The default_value of this Parameter.  # noqa: E501
        :type: object
        """

        self._default_value = default_value

    @property
    def max_length(self):
        """Gets the max_length of this Parameter.  # noqa: E501

        Indicates the maximum length of a parameter of type 'string'  # noqa: E501

        :return: The max_length of this Parameter.  # noqa: E501
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this Parameter.

        Indicates the maximum length of a parameter of type 'string'  # noqa: E501

        :param max_length: The max_length of this Parameter.  # noqa: E501
        :type: int
        """

        self._max_length = max_length

    @property
    def min_length(self):
        """Gets the min_length of this Parameter.  # noqa: E501

        Indicates the minimum length of a parameter of type 'string'. If not present, assumed default value is 0.  # noqa: E501

        :return: The min_length of this Parameter.  # noqa: E501
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this Parameter.

        Indicates the minimum length of a parameter of type 'string'. If not present, assumed default value is 0.  # noqa: E501

        :param min_length: The min_length of this Parameter.  # noqa: E501
        :type: int
        """

        self._min_length = min_length

    @property
    def pattern(self):
        """Gets the pattern of this Parameter.  # noqa: E501

        Specifies a valid regular expression against which a parameter of type 'string' is validated.  # noqa: E501

        :return: The pattern of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this Parameter.

        Specifies a valid regular expression against which a parameter of type 'string' is validated.  # noqa: E501

        :param pattern: The pattern of this Parameter.  # noqa: E501
        :type: str
        """

        self._pattern = pattern

    @property
    def exclusive_minimum(self):
        """Gets the exclusive_minimum of this Parameter.  # noqa: E501

        If true, specifies that the value of the number parameter must be greater than the specified minimum value, otherwise the value must be great than, or equal to, the specified minimum value.  # noqa: E501

        :return: The exclusive_minimum of this Parameter.  # noqa: E501
        :rtype: bool
        """
        return self._exclusive_minimum

    @exclusive_minimum.setter
    def exclusive_minimum(self, exclusive_minimum):
        """Sets the exclusive_minimum of this Parameter.

        If true, specifies that the value of the number parameter must be greater than the specified minimum value, otherwise the value must be great than, or equal to, the specified minimum value.  # noqa: E501

        :param exclusive_minimum: The exclusive_minimum of this Parameter.  # noqa: E501
        :type: bool
        """

        self._exclusive_minimum = exclusive_minimum

    @property
    def exclusive_maximum(self):
        """Gets the exclusive_maximum of this Parameter.  # noqa: E501

        If true, specifies that the value of the number parameter must be less than the specified maximum value, otherwise the value must be less than, or equal to, the specified maximum value.  # noqa: E501

        :return: The exclusive_maximum of this Parameter.  # noqa: E501
        :rtype: bool
        """
        return self._exclusive_maximum

    @exclusive_maximum.setter
    def exclusive_maximum(self, exclusive_maximum):
        """Sets the exclusive_maximum of this Parameter.

        If true, specifies that the value of the number parameter must be less than the specified maximum value, otherwise the value must be less than, or equal to, the specified maximum value.  # noqa: E501

        :param exclusive_maximum: The exclusive_maximum of this Parameter.  # noqa: E501
        :type: bool
        """

        self._exclusive_maximum = exclusive_maximum

    @property
    def minimum(self):
        """Gets the minimum of this Parameter.  # noqa: E501

        Specifies the minimum possible value of the number parameter.  # noqa: E501

        :return: The minimum of this Parameter.  # noqa: E501
        :rtype: object
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this Parameter.

        Specifies the minimum possible value of the number parameter.  # noqa: E501

        :param minimum: The minimum of this Parameter.  # noqa: E501
        :type: object
        """

        self._minimum = minimum

    @property
    def maximum(self):
        """Gets the maximum of this Parameter.  # noqa: E501

        Specifies the maximum possible value of the number parameter.  # noqa: E501

        :return: The maximum of this Parameter.  # noqa: E501
        :rtype: object
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this Parameter.

        Specifies the maximum possible value of the number parameter.  # noqa: E501

        :param maximum: The maximum of this Parameter.  # noqa: E501
        :type: object
        """

        self._maximum = maximum

    @property
    def multiple_of(self):
        """Gets the multiple_of of this Parameter.  # noqa: E501

        Specifies that the value of the number parameter must be divisible by this value. Must be an integer value > 0  # noqa: E501

        :return: The multiple_of of this Parameter.  # noqa: E501
        :rtype: Number
        """
        return self._multiple_of

    @multiple_of.setter
    def multiple_of(self, multiple_of):
        """Sets the multiple_of of this Parameter.

        Specifies that the value of the number parameter must be divisible by this value. Must be an integer value > 0  # noqa: E501

        :param multiple_of: The multiple_of of this Parameter.  # noqa: E501
        :type: Number
        """

        self._multiple_of = multiple_of

    @property
    def max_items(self):
        """Gets the max_items of this Parameter.  # noqa: E501

        Specifies the maximum number of items permitted for array parameters. Must be an integer value greater than, or equal to 0  # noqa: E501

        :return: The max_items of this Parameter.  # noqa: E501
        :rtype: int
        """
        return self._max_items

    @max_items.setter
    def max_items(self, max_items):
        """Sets the max_items of this Parameter.

        Specifies the maximum number of items permitted for array parameters. Must be an integer value greater than, or equal to 0  # noqa: E501

        :param max_items: The max_items of this Parameter.  # noqa: E501
        :type: int
        """

        self._max_items = max_items

    @property
    def min_items(self):
        """Gets the min_items of this Parameter.  # noqa: E501

        Specifies the minimum number of items permitted for array parameters. Must be an integer value greater than, or equal to 0  # noqa: E501

        :return: The min_items of this Parameter.  # noqa: E501
        :rtype: int
        """
        return self._min_items

    @min_items.setter
    def min_items(self, min_items):
        """Sets the min_items of this Parameter.

        Specifies the minimum number of items permitted for array parameters. Must be an integer value greater than, or equal to 0  # noqa: E501

        :param min_items: The min_items of this Parameter.  # noqa: E501
        :type: int
        """

        self._min_items = min_items

    @property
    def unique_items(self):
        """Gets the unique_items of this Parameter.  # noqa: E501

        Specifies whether or not all array items should be unique.  # noqa: E501

        :return: The unique_items of this Parameter.  # noqa: E501
        :rtype: bool
        """
        return self._unique_items

    @unique_items.setter
    def unique_items(self, unique_items):
        """Sets the unique_items of this Parameter.

        Specifies whether or not all array items should be unique.  # noqa: E501

        :param unique_items: The unique_items of this Parameter.  # noqa: E501
        :type: bool
        """

        self._unique_items = unique_items

    @property
    def collection_format(self):
        """Gets the collection_format of this Parameter.  # noqa: E501

        Specifies the format of array parameters. Possible values: [ csv, ssv, tsv, pipes, multi ].  # noqa: E501

        :return: The collection_format of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._collection_format

    @collection_format.setter
    def collection_format(self, collection_format):
        """Sets the collection_format of this Parameter.

        Specifies the format of array parameters. Possible values: [ csv, ssv, tsv, pipes, multi ].  # noqa: E501

        :param collection_format: The collection_format of this Parameter.  # noqa: E501
        :type: str
        """

        self._collection_format = collection_format

    @property
    def schema(self):
        """Gets the schema of this Parameter.  # noqa: E501

        The response schema  # noqa: E501

        :return: The schema of this Parameter.  # noqa: E501
        :rtype: SchemaObject
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this Parameter.

        The response schema  # noqa: E501

        :param schema: The schema of this Parameter.  # noqa: E501
        :type: SchemaObject
        """

        self._schema = schema

    @property
    def enum(self):
        """Gets the enum of this Parameter.  # noqa: E501


        :return: The enum of this Parameter.  # noqa: E501
        :rtype: list[object]
        """
        return self._enum

    @enum.setter
    def enum(self, enum):
        """Sets the enum of this Parameter.


        :param enum: The enum of this Parameter.  # noqa: E501
        :type: list[object]
        """

        self._enum = enum

    @property
    def param_type(self):
        """Gets the param_type of this Parameter.  # noqa: E501

        The parameter type, e.g. query, form, path, body, header  # noqa: E501

        :return: The param_type of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._param_type

    @param_type.setter
    def param_type(self, param_type):
        """Sets the param_type of this Parameter.

        The parameter type, e.g. query, form, path, body, header  # noqa: E501

        :param param_type: The param_type of this Parameter.  # noqa: E501
        :type: str
        """

        self._param_type = param_type

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
        if issubclass(Parameter, dict):
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
        if not isinstance(other, Parameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
