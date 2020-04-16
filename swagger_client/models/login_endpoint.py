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


class LoginEndpoint(object):
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
        'title': 'str',
        'description': 'str',
        'format': 'str',
        'required': 'list[str]',
        'properties': 'dict(str, SchemaObject)',
        'items': 'SchemaObject',
        'example': 'object',
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
        'discriminator': 'str',
        'url': 'str',
        'ref': 'str',
        'default': 'object',
        'type': 'str',
        'enum': 'list[object]'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'format': 'format',
        'required': 'required',
        'properties': 'properties',
        'items': 'items',
        'example': 'example',
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
        'discriminator': 'discriminator',
        'url': 'url',
        'ref': '$ref',
        'default': 'default',
        'type': 'type',
        'enum': 'enum'
    }

    def __init__(self, id=None, title=None, description=None, format=None, required=None, properties=None, items=None, example=None, max_length=None, min_length=None, pattern=None, exclusive_minimum=False, exclusive_maximum=False, minimum=None, maximum=None, multiple_of=None, max_items=None, min_items=None, unique_items=False, collection_format=None, discriminator=None, url=None, ref=None, default=None, type=None, enum=None):  # noqa: E501
        """LoginEndpoint - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._title = None
        self._description = None
        self._format = None
        self._required = None
        self._properties = None
        self._items = None
        self._example = None
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
        self._discriminator = None
        self._url = None
        self._ref = None
        self._default = None
        self._type = None
        self._enum = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if format is not None:
            self.format = format
        if required is not None:
            self.required = required
        if properties is not None:
            self.properties = properties
        if items is not None:
            self.items = items
        if example is not None:
            self.example = example
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
        if discriminator is not None:
            self.discriminator = discriminator
        if url is not None:
            self.url = url
        if ref is not None:
            self.ref = ref
        if default is not None:
            self.default = default
        if type is not None:
            self.type = type
        if enum is not None:
            self.enum = enum

    @property
    def id(self):
        """Gets the id of this LoginEndpoint.  # noqa: E501

        An identifier  # noqa: E501

        :return: The id of this LoginEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoginEndpoint.

        An identifier  # noqa: E501

        :param id: The id of this LoginEndpoint.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this LoginEndpoint.  # noqa: E501

        Schema title  # noqa: E501

        :return: The title of this LoginEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LoginEndpoint.

        Schema title  # noqa: E501

        :param title: The title of this LoginEndpoint.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this LoginEndpoint.  # noqa: E501

        Description of the Schema  # noqa: E501

        :return: The description of this LoginEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LoginEndpoint.

        Description of the Schema  # noqa: E501

        :param description: The description of this LoginEndpoint.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def format(self):
        """Gets the format of this LoginEndpoint.  # noqa: E501

        The format ex: int32, int64, float, double, byte, binary, date, date-time or password  # noqa: E501

        :return: The format of this LoginEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this LoginEndpoint.

        The format ex: int32, int64, float, double, byte, binary, date, date-time or password  # noqa: E501

        :param format: The format of this LoginEndpoint.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def required(self):
        """Gets the required of this LoginEndpoint.  # noqa: E501

        Specifies if the parameter is required  # noqa: E501

        :return: The required of this LoginEndpoint.  # noqa: E501
        :rtype: list[str]
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this LoginEndpoint.

        Specifies if the parameter is required  # noqa: E501

        :param required: The required of this LoginEndpoint.  # noqa: E501
        :type: list[str]
        """

        self._required = required

    @property
    def properties(self):
        """Gets the properties of this LoginEndpoint.  # noqa: E501

        Not used because our model does not support inline nested types  # noqa: E501

        :return: The properties of this LoginEndpoint.  # noqa: E501
        :rtype: dict(str, SchemaObject)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this LoginEndpoint.

        Not used because our model does not support inline nested types  # noqa: E501

        :param properties: The properties of this LoginEndpoint.  # noqa: E501
        :type: dict(str, SchemaObject)
        """

        self._properties = properties

    @property
    def items(self):
        """Gets the items of this LoginEndpoint.  # noqa: E501

        if the schema is an array specifies the items type  # noqa: E501

        :return: The items of this LoginEndpoint.  # noqa: E501
        :rtype: SchemaObject
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this LoginEndpoint.

        if the schema is an array specifies the items type  # noqa: E501

        :param items: The items of this LoginEndpoint.  # noqa: E501
        :type: SchemaObject
        """

        self._items = items

    @property
    def example(self):
        """Gets the example of this LoginEndpoint.  # noqa: E501

        if the schema is an array specifies the items type  # noqa: E501

        :return: The example of this LoginEndpoint.  # noqa: E501
        :rtype: object
        """
        return self._example

    @example.setter
    def example(self, example):
        """Sets the example of this LoginEndpoint.

        if the schema is an array specifies the items type  # noqa: E501

        :param example: The example of this LoginEndpoint.  # noqa: E501
        :type: object
        """

        self._example = example

    @property
    def max_length(self):
        """Gets the max_length of this LoginEndpoint.  # noqa: E501

        Indicates the maximum length of a parameter of type 'string'  # noqa: E501

        :return: The max_length of this LoginEndpoint.  # noqa: E501
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this LoginEndpoint.

        Indicates the maximum length of a parameter of type 'string'  # noqa: E501

        :param max_length: The max_length of this LoginEndpoint.  # noqa: E501
        :type: int
        """

        self._max_length = max_length

    @property
    def min_length(self):
        """Gets the min_length of this LoginEndpoint.  # noqa: E501

        Indicates the minimum length of a parameter of type 'string'. If not present, assumed default value is 0.  # noqa: E501

        :return: The min_length of this LoginEndpoint.  # noqa: E501
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this LoginEndpoint.

        Indicates the minimum length of a parameter of type 'string'. If not present, assumed default value is 0.  # noqa: E501

        :param min_length: The min_length of this LoginEndpoint.  # noqa: E501
        :type: int
        """

        self._min_length = min_length

    @property
    def pattern(self):
        """Gets the pattern of this LoginEndpoint.  # noqa: E501

        Specifies a valid regular expression against which a parameter of type 'string' is validated.  # noqa: E501

        :return: The pattern of this LoginEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this LoginEndpoint.

        Specifies a valid regular expression against which a parameter of type 'string' is validated.  # noqa: E501

        :param pattern: The pattern of this LoginEndpoint.  # noqa: E501
        :type: str
        """

        self._pattern = pattern

    @property
    def exclusive_minimum(self):
        """Gets the exclusive_minimum of this LoginEndpoint.  # noqa: E501

        If true, specifies that the value of the number parameter must be greater than the specified minimum value, otherwise the value must be great than, or equal to, the specified minimum value.  # noqa: E501

        :return: The exclusive_minimum of this LoginEndpoint.  # noqa: E501
        :rtype: bool
        """
        return self._exclusive_minimum

    @exclusive_minimum.setter
    def exclusive_minimum(self, exclusive_minimum):
        """Sets the exclusive_minimum of this LoginEndpoint.

        If true, specifies that the value of the number parameter must be greater than the specified minimum value, otherwise the value must be great than, or equal to, the specified minimum value.  # noqa: E501

        :param exclusive_minimum: The exclusive_minimum of this LoginEndpoint.  # noqa: E501
        :type: bool
        """

        self._exclusive_minimum = exclusive_minimum

    @property
    def exclusive_maximum(self):
        """Gets the exclusive_maximum of this LoginEndpoint.  # noqa: E501

        If true, specifies that the value of the number parameter must be less than the specified maximum value, otherwise the value must be less than, or equal to, the specified maximum value.  # noqa: E501

        :return: The exclusive_maximum of this LoginEndpoint.  # noqa: E501
        :rtype: bool
        """
        return self._exclusive_maximum

    @exclusive_maximum.setter
    def exclusive_maximum(self, exclusive_maximum):
        """Sets the exclusive_maximum of this LoginEndpoint.

        If true, specifies that the value of the number parameter must be less than the specified maximum value, otherwise the value must be less than, or equal to, the specified maximum value.  # noqa: E501

        :param exclusive_maximum: The exclusive_maximum of this LoginEndpoint.  # noqa: E501
        :type: bool
        """

        self._exclusive_maximum = exclusive_maximum

    @property
    def minimum(self):
        """Gets the minimum of this LoginEndpoint.  # noqa: E501

        Specifies the minimum possible value of the number parameter.  # noqa: E501

        :return: The minimum of this LoginEndpoint.  # noqa: E501
        :rtype: object
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this LoginEndpoint.

        Specifies the minimum possible value of the number parameter.  # noqa: E501

        :param minimum: The minimum of this LoginEndpoint.  # noqa: E501
        :type: object
        """

        self._minimum = minimum

    @property
    def maximum(self):
        """Gets the maximum of this LoginEndpoint.  # noqa: E501

        Specifies the maximum possible value of the number parameter.  # noqa: E501

        :return: The maximum of this LoginEndpoint.  # noqa: E501
        :rtype: object
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this LoginEndpoint.

        Specifies the maximum possible value of the number parameter.  # noqa: E501

        :param maximum: The maximum of this LoginEndpoint.  # noqa: E501
        :type: object
        """

        self._maximum = maximum

    @property
    def multiple_of(self):
        """Gets the multiple_of of this LoginEndpoint.  # noqa: E501

        Specifies that the value of the number parameter must be divisible by this value. Must be an integer value > 0  # noqa: E501

        :return: The multiple_of of this LoginEndpoint.  # noqa: E501
        :rtype: Number
        """
        return self._multiple_of

    @multiple_of.setter
    def multiple_of(self, multiple_of):
        """Sets the multiple_of of this LoginEndpoint.

        Specifies that the value of the number parameter must be divisible by this value. Must be an integer value > 0  # noqa: E501

        :param multiple_of: The multiple_of of this LoginEndpoint.  # noqa: E501
        :type: Number
        """

        self._multiple_of = multiple_of

    @property
    def max_items(self):
        """Gets the max_items of this LoginEndpoint.  # noqa: E501

        Specifies the maximum number of items permitted for array parameters. Must be an integer value greater than, or equal to 0  # noqa: E501

        :return: The max_items of this LoginEndpoint.  # noqa: E501
        :rtype: int
        """
        return self._max_items

    @max_items.setter
    def max_items(self, max_items):
        """Sets the max_items of this LoginEndpoint.

        Specifies the maximum number of items permitted for array parameters. Must be an integer value greater than, or equal to 0  # noqa: E501

        :param max_items: The max_items of this LoginEndpoint.  # noqa: E501
        :type: int
        """

        self._max_items = max_items

    @property
    def min_items(self):
        """Gets the min_items of this LoginEndpoint.  # noqa: E501

        Specifies the minimum number of items permitted for array parameters. Must be an integer value greater than, or equal to 0  # noqa: E501

        :return: The min_items of this LoginEndpoint.  # noqa: E501
        :rtype: int
        """
        return self._min_items

    @min_items.setter
    def min_items(self, min_items):
        """Sets the min_items of this LoginEndpoint.

        Specifies the minimum number of items permitted for array parameters. Must be an integer value greater than, or equal to 0  # noqa: E501

        :param min_items: The min_items of this LoginEndpoint.  # noqa: E501
        :type: int
        """

        self._min_items = min_items

    @property
    def unique_items(self):
        """Gets the unique_items of this LoginEndpoint.  # noqa: E501

        Specifies whether or not all array items should be unique.  # noqa: E501

        :return: The unique_items of this LoginEndpoint.  # noqa: E501
        :rtype: bool
        """
        return self._unique_items

    @unique_items.setter
    def unique_items(self, unique_items):
        """Sets the unique_items of this LoginEndpoint.

        Specifies whether or not all array items should be unique.  # noqa: E501

        :param unique_items: The unique_items of this LoginEndpoint.  # noqa: E501
        :type: bool
        """

        self._unique_items = unique_items

    @property
    def collection_format(self):
        """Gets the collection_format of this LoginEndpoint.  # noqa: E501


        :return: The collection_format of this LoginEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._collection_format

    @collection_format.setter
    def collection_format(self, collection_format):
        """Sets the collection_format of this LoginEndpoint.


        :param collection_format: The collection_format of this LoginEndpoint.  # noqa: E501
        :type: str
        """

        self._collection_format = collection_format

    @property
    def discriminator(self):
        """Gets the discriminator of this LoginEndpoint.  # noqa: E501


        :return: The discriminator of this LoginEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._discriminator

    @discriminator.setter
    def discriminator(self, discriminator):
        """Sets the discriminator of this LoginEndpoint.


        :param discriminator: The discriminator of this LoginEndpoint.  # noqa: E501
        :type: str
        """

        self._discriminator = discriminator

    @property
    def url(self):
        """Gets the url of this LoginEndpoint.  # noqa: E501

        The URL of the authorization endpoint for the implicit grant flow. The value should be in a URL format.  # noqa: E501

        :return: The url of this LoginEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this LoginEndpoint.

        The URL of the authorization endpoint for the implicit grant flow. The value should be in a URL format.  # noqa: E501

        :param url: The url of this LoginEndpoint.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def ref(self):
        """Gets the ref of this LoginEndpoint.  # noqa: E501

        A Reference to a definition on definitions object  # noqa: E501

        :return: The ref of this LoginEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this LoginEndpoint.

        A Reference to a definition on definitions object  # noqa: E501

        :param ref: The ref of this LoginEndpoint.  # noqa: E501
        :type: str
        """

        self._ref = ref

    @property
    def default(self):
        """Gets the default of this LoginEndpoint.  # noqa: E501

        Default value for this schema if it is applicable  # noqa: E501

        :return: The default of this LoginEndpoint.  # noqa: E501
        :rtype: object
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this LoginEndpoint.

        Default value for this schema if it is applicable  # noqa: E501

        :param default: The default of this LoginEndpoint.  # noqa: E501
        :type: object
        """

        self._default = default

    @property
    def type(self):
        """Gets the type of this LoginEndpoint.  # noqa: E501

        The type ex: array , boolean, integer , null , number, object, string  # noqa: E501

        :return: The type of this LoginEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LoginEndpoint.

        The type ex: array , boolean, integer , null , number, object, string  # noqa: E501

        :param type: The type of this LoginEndpoint.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def enum(self):
        """Gets the enum of this LoginEndpoint.  # noqa: E501


        :return: The enum of this LoginEndpoint.  # noqa: E501
        :rtype: list[object]
        """
        return self._enum

    @enum.setter
    def enum(self, enum):
        """Sets the enum of this LoginEndpoint.


        :param enum: The enum of this LoginEndpoint.  # noqa: E501
        :type: list[object]
        """

        self._enum = enum

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
        if issubclass(LoginEndpoint, dict):
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
        if not isinstance(other, LoginEndpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
