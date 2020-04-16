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


class Topology(object):
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
        'version': 'int',
        'timestamp': 'int',
        'product_version': 'str',
        'hosts': 'list[Host]',
        'groups': 'list[Group]',
        'unique_id_counters': 'dict(str, int)',
        'emt_enabled': 'bool',
        'services': 'list[Service]'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'timestamp': 'timestamp',
        'product_version': 'productVersion',
        'hosts': 'hosts',
        'groups': 'groups',
        'unique_id_counters': 'uniqueIdCounters',
        'emt_enabled': 'emtEnabled',
        'services': 'services'
    }

    def __init__(self, id=None, version=None, timestamp=None, product_version=None, hosts=None, groups=None, unique_id_counters=None, emt_enabled=False, services=None):  # noqa: E501
        """Topology - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._version = None
        self._timestamp = None
        self._product_version = None
        self._hosts = None
        self._groups = None
        self._unique_id_counters = None
        self._emt_enabled = None
        self._services = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if timestamp is not None:
            self.timestamp = timestamp
        if product_version is not None:
            self.product_version = product_version
        if hosts is not None:
            self.hosts = hosts
        if groups is not None:
            self.groups = groups
        if unique_id_counters is not None:
            self.unique_id_counters = unique_id_counters
        if emt_enabled is not None:
            self.emt_enabled = emt_enabled
        if services is not None:
            self.services = services

    @property
    def id(self):
        """Gets the id of this Topology.  # noqa: E501


        :return: The id of this Topology.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Topology.


        :param id: The id of this Topology.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def version(self):
        """Gets the version of this Topology.  # noqa: E501


        :return: The version of this Topology.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Topology.


        :param version: The version of this Topology.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def timestamp(self):
        """Gets the timestamp of this Topology.  # noqa: E501


        :return: The timestamp of this Topology.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Topology.


        :param timestamp: The timestamp of this Topology.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def product_version(self):
        """Gets the product_version of this Topology.  # noqa: E501


        :return: The product_version of this Topology.  # noqa: E501
        :rtype: str
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        """Sets the product_version of this Topology.


        :param product_version: The product_version of this Topology.  # noqa: E501
        :type: str
        """

        self._product_version = product_version

    @property
    def hosts(self):
        """Gets the hosts of this Topology.  # noqa: E501


        :return: The hosts of this Topology.  # noqa: E501
        :rtype: list[Host]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this Topology.


        :param hosts: The hosts of this Topology.  # noqa: E501
        :type: list[Host]
        """

        self._hosts = hosts

    @property
    def groups(self):
        """Gets the groups of this Topology.  # noqa: E501


        :return: The groups of this Topology.  # noqa: E501
        :rtype: list[Group]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this Topology.


        :param groups: The groups of this Topology.  # noqa: E501
        :type: list[Group]
        """

        self._groups = groups

    @property
    def unique_id_counters(self):
        """Gets the unique_id_counters of this Topology.  # noqa: E501


        :return: The unique_id_counters of this Topology.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._unique_id_counters

    @unique_id_counters.setter
    def unique_id_counters(self, unique_id_counters):
        """Sets the unique_id_counters of this Topology.


        :param unique_id_counters: The unique_id_counters of this Topology.  # noqa: E501
        :type: dict(str, int)
        """

        self._unique_id_counters = unique_id_counters

    @property
    def emt_enabled(self):
        """Gets the emt_enabled of this Topology.  # noqa: E501


        :return: The emt_enabled of this Topology.  # noqa: E501
        :rtype: bool
        """
        return self._emt_enabled

    @emt_enabled.setter
    def emt_enabled(self, emt_enabled):
        """Sets the emt_enabled of this Topology.


        :param emt_enabled: The emt_enabled of this Topology.  # noqa: E501
        :type: bool
        """

        self._emt_enabled = emt_enabled

    @property
    def services(self):
        """Gets the services of this Topology.  # noqa: E501


        :return: The services of this Topology.  # noqa: E501
        :rtype: list[Service]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this Topology.


        :param services: The services of this Topology.  # noqa: E501
        :type: list[Service]
        """

        self._services = services

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
        if issubclass(Topology, dict):
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
        if not isinstance(other, Topology):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
