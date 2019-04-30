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


class Application(object):
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
        'description': 'str',
        'organization_id': 'str',
        'phone': 'str',
        'email': 'str',
        'created_by': 'str',
        'managed_by': 'list[str]',
        'created_on': 'int',
        'enabled': 'bool',
        'image': 'str',
        'state': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'organization_id': 'organizationId',
        'phone': 'phone',
        'email': 'email',
        'created_by': 'createdBy',
        'managed_by': 'managedBy',
        'created_on': 'createdOn',
        'enabled': 'enabled',
        'image': 'image',
        'state': 'state'
    }

    def __init__(self, id=None, name=None, description=None, organization_id=None, phone=None, email=None, created_by=None, managed_by=None, created_on=None, enabled=False, image=None, state=None):  # noqa: E501
        """Application - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._organization_id = None
        self._phone = None
        self._email = None
        self._created_by = None
        self._managed_by = None
        self._created_on = None
        self._enabled = None
        self._image = None
        self._state = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.organization_id = organization_id
        if phone is not None:
            self.phone = phone
        if email is not None:
            self.email = email
        if created_by is not None:
            self.created_by = created_by
        if managed_by is not None:
            self.managed_by = managed_by
        if created_on is not None:
            self.created_on = created_on
        if enabled is not None:
            self.enabled = enabled
        if image is not None:
            self.image = image
        if state is not None:
            self.state = state

    @property
    def id(self):
        """Gets the id of this Application.  # noqa: E501

        The unique identifier for the application  # noqa: E501

        :return: The id of this Application.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Application.

        The unique identifier for the application  # noqa: E501

        :param id: The id of this Application.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Application.  # noqa: E501

        The display name for the application  # noqa: E501

        :return: The name of this Application.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Application.

        The display name for the application  # noqa: E501

        :param name: The name of this Application.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Application.  # noqa: E501

        Descriptive text for the application  # noqa: E501

        :return: The description of this Application.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Application.

        Descriptive text for the application  # noqa: E501

        :param description: The description of this Application.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def organization_id(self):
        """Gets the organization_id of this Application.  # noqa: E501

        The organization identifier to which the application belongs  # noqa: E501

        :return: The organization_id of this Application.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Application.

        The organization identifier to which the application belongs  # noqa: E501

        :param organization_id: The organization_id of this Application.  # noqa: E501
        :type: str
        """
        if organization_id is None:
            raise ValueError("Invalid value for `organization_id`, must not be `None`")  # noqa: E501

        self._organization_id = organization_id

    @property
    def phone(self):
        """Gets the phone of this Application.  # noqa: E501

        Contact phone number of the application  # noqa: E501

        :return: The phone of this Application.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Application.

        Contact phone number of the application  # noqa: E501

        :param phone: The phone of this Application.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this Application.  # noqa: E501

        The contact email address associated with the application  # noqa: E501

        :return: The email of this Application.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Application.

        The contact email address associated with the application  # noqa: E501

        :param email: The email of this Application.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def created_by(self):
        """Gets the created_by of this Application.  # noqa: E501

        The unique identifier for user that created the application  # noqa: E501

        :return: The created_by of this Application.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Application.

        The unique identifier for user that created the application  # noqa: E501

        :param created_by: The created_by of this Application.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def managed_by(self):
        """Gets the managed_by of this Application.  # noqa: E501

        A list of unique identifier for users that manages the application  # noqa: E501

        :return: The managed_by of this Application.  # noqa: E501
        :rtype: list[str]
        """
        return self._managed_by

    @managed_by.setter
    def managed_by(self, managed_by):
        """Sets the managed_by of this Application.

        A list of unique identifier for users that manages the application  # noqa: E501

        :param managed_by: The managed_by of this Application.  # noqa: E501
        :type: list[str]
        """

        self._managed_by = managed_by

    @property
    def created_on(self):
        """Gets the created_on of this Application.  # noqa: E501

        Epoch/Unix time stamp when the application was created  # noqa: E501

        :return: The created_on of this Application.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Application.

        Epoch/Unix time stamp when the application was created  # noqa: E501

        :param created_on: The created_on of this Application.  # noqa: E501
        :type: int
        """

        self._created_on = created_on

    @property
    def enabled(self):
        """Gets the enabled of this Application.  # noqa: E501

        Flag to indicate if this application is enabled or not  # noqa: E501

        :return: The enabled of this Application.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Application.

        Flag to indicate if this application is enabled or not  # noqa: E501

        :param enabled: The enabled of this Application.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def image(self):
        """Gets the image of this Application.  # noqa: E501

        URI of the image to be used for this application, this field only indicates that the application has an image assigned to it. In order to retrieve the actual image use the following URL /api/portal/applications/{id}/image/  # noqa: E501

        :return: The image of this Application.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Application.

        URI of the image to be used for this application, this field only indicates that the application has an image assigned to it. In order to retrieve the actual image use the following URL /api/portal/applications/{id}/image/  # noqa: E501

        :param image: The image of this Application.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def state(self):
        """Gets the state of this Application.  # noqa: E501

        Flag to indicate if an application has been approved by the API Manager admin or if delegated then the org admin  # noqa: E501

        :return: The state of this Application.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Application.

        Flag to indicate if an application has been approved by the API Manager admin or if delegated then the org admin  # noqa: E501

        :param state: The state of this Application.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if issubclass(Application, dict):
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
        if not isinstance(other, Application):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other