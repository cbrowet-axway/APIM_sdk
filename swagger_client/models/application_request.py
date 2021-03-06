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


class ApplicationRequest(object):
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
        'image': 'str',
        'apis': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'organization_id': 'organizationId',
        'phone': 'phone',
        'email': 'email',
        'image': 'image',
        'apis': 'apis'
    }

    def __init__(self, id=None, name=None, description=None, organization_id=None, phone=None, email=None, image=None, apis=None):  # noqa: E501
        """ApplicationRequest - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._organization_id = None
        self._phone = None
        self._email = None
        self._image = None
        self._apis = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if organization_id is not None:
            self.organization_id = organization_id
        if phone is not None:
            self.phone = phone
        if email is not None:
            self.email = email
        if image is not None:
            self.image = image
        if apis is not None:
            self.apis = apis

    @property
    def id(self):
        """Gets the id of this ApplicationRequest.  # noqa: E501

        The unique identifier for the application request  # noqa: E501

        :return: The id of this ApplicationRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApplicationRequest.

        The unique identifier for the application request  # noqa: E501

        :param id: The id of this ApplicationRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ApplicationRequest.  # noqa: E501

        The display name for the application  # noqa: E501

        :return: The name of this ApplicationRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationRequest.

        The display name for the application  # noqa: E501

        :param name: The name of this ApplicationRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ApplicationRequest.  # noqa: E501

        Descriptive text for the application  # noqa: E501

        :return: The description of this ApplicationRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApplicationRequest.

        Descriptive text for the application  # noqa: E501

        :param description: The description of this ApplicationRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def organization_id(self):
        """Gets the organization_id of this ApplicationRequest.  # noqa: E501

        The organization identifier to which the application request belongs  # noqa: E501

        :return: The organization_id of this ApplicationRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this ApplicationRequest.

        The organization identifier to which the application request belongs  # noqa: E501

        :param organization_id: The organization_id of this ApplicationRequest.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def phone(self):
        """Gets the phone of this ApplicationRequest.  # noqa: E501

        Contact phone number of the application  # noqa: E501

        :return: The phone of this ApplicationRequest.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ApplicationRequest.

        Contact phone number of the application  # noqa: E501

        :param phone: The phone of this ApplicationRequest.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this ApplicationRequest.  # noqa: E501

        The contact email address associated with the application  # noqa: E501

        :return: The email of this ApplicationRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ApplicationRequest.

        The contact email address associated with the application  # noqa: E501

        :param email: The email of this ApplicationRequest.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def image(self):
        """Gets the image of this ApplicationRequest.  # noqa: E501

        URI of the image to be used for this application, this field only indicates that the application has an image assigned to it. In order to retrieve the actual image use the following URL /api/portal/organizations/{uid of org}/image/  # noqa: E501

        :return: The image of this ApplicationRequest.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ApplicationRequest.

        URI of the image to be used for this application, this field only indicates that the application has an image assigned to it. In order to retrieve the actual image use the following URL /api/portal/organizations/{uid of org}/image/  # noqa: E501

        :param image: The image of this ApplicationRequest.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def apis(self):
        """Gets the apis of this ApplicationRequest.  # noqa: E501

        A list of unqiue API identifiers to which the application wants to use.  # noqa: E501

        :return: The apis of this ApplicationRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._apis

    @apis.setter
    def apis(self, apis):
        """Sets the apis of this ApplicationRequest.

        A list of unqiue API identifiers to which the application wants to use.  # noqa: E501

        :param apis: The apis of this ApplicationRequest.  # noqa: E501
        :type: list[str]
        """

        self._apis = apis

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
        if issubclass(ApplicationRequest, dict):
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
        if not isinstance(other, ApplicationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
