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


class MetricTimeline(object):
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
        'name': 'str',
        'series': 'list[Series]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'series': 'series'
    }

    def __init__(self, id=None, name=None, series=None):  # noqa: E501
        """MetricTimeline - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._series = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if series is not None:
            self.series = series

    @property
    def id(self):
        """Gets the id of this MetricTimeline.  # noqa: E501


        :return: The id of this MetricTimeline.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MetricTimeline.


        :param id: The id of this MetricTimeline.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MetricTimeline.  # noqa: E501

        The metric name.  # noqa: E501

        :return: The name of this MetricTimeline.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MetricTimeline.

        The metric name.  # noqa: E501

        :param name: The name of this MetricTimeline.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def series(self):
        """Gets the series of this MetricTimeline.  # noqa: E501

        The time series.  # noqa: E501

        :return: The series of this MetricTimeline.  # noqa: E501
        :rtype: list[Series]
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this MetricTimeline.

        The time series.  # noqa: E501

        :param series: The series of this MetricTimeline.  # noqa: E501
        :type: list[Series]
        """

        self._series = series

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
        if issubclass(MetricTimeline, dict):
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
        if not isinstance(other, MetricTimeline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
