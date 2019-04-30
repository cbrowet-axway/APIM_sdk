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

from swagger_client.models.authentication_profile import AuthenticationProfile  # noqa: F401,E501
from swagger_client.models.ca_cert import CACert  # noqa: F401,E501
from swagger_client.models.cors_profile import CORSProfile  # noqa: F401,E501
from swagger_client.models.inbound_profiles import InboundProfiles  # noqa: F401,E501
from swagger_client.models.outbound_profiles import OutboundProfiles  # noqa: F401,E501
from swagger_client.models.security_profile import SecurityProfile  # noqa: F401,E501
from swagger_client.models.service_profiles import ServiceProfiles  # noqa: F401,E501


class VirtualizedAPI(object):
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
        'organization_id': 'str',
        'api_id': 'str',
        'name': 'str',
        'version': 'str',
        'api_routing_key': 'str',
        'vhost': 'str',
        'path': 'str',
        'description_type': 'str',
        'description_manual': 'str',
        'description_markdown': 'str',
        'description_url': 'str',
        'summary': 'str',
        'retired': 'bool',
        'expired': 'bool',
        'image': 'str',
        'retirement_date': 'int',
        'deprecated': 'bool',
        'state': 'str',
        'created_on': 'int',
        'created_by': 'str',
        'cors_profiles': 'list[CORSProfile]',
        'security_profiles': 'list[SecurityProfile]',
        'authentication_profiles': 'list[AuthenticationProfile]',
        'inbound_profiles': 'dict(str, InboundProfiles)',
        'outbound_profiles': 'dict(str, OutboundProfiles)',
        'service_profiles': 'dict(str, ServiceProfiles)',
        'ca_certs': 'list[CACert]',
        'tags': 'dict(str, list[str])'
    }

    attribute_map = {
        'id': 'id',
        'organization_id': 'organizationId',
        'api_id': 'apiId',
        'name': 'name',
        'version': 'version',
        'api_routing_key': 'apiRoutingKey',
        'vhost': 'vhost',
        'path': 'path',
        'description_type': 'descriptionType',
        'description_manual': 'descriptionManual',
        'description_markdown': 'descriptionMarkdown',
        'description_url': 'descriptionUrl',
        'summary': 'summary',
        'retired': 'retired',
        'expired': 'expired',
        'image': 'image',
        'retirement_date': 'retirementDate',
        'deprecated': 'deprecated',
        'state': 'state',
        'created_on': 'createdOn',
        'created_by': 'createdBy',
        'cors_profiles': 'corsProfiles',
        'security_profiles': 'securityProfiles',
        'authentication_profiles': 'authenticationProfiles',
        'inbound_profiles': 'inboundProfiles',
        'outbound_profiles': 'outboundProfiles',
        'service_profiles': 'serviceProfiles',
        'ca_certs': 'caCerts',
        'tags': 'tags'
    }

    def __init__(self, id=None, organization_id=None, api_id=None, name=None, version=None, api_routing_key=None, vhost=None, path=None, description_type=None, description_manual=None, description_markdown=None, description_url=None, summary=None, retired=False, expired=False, image=None, retirement_date=None, deprecated=False, state=None, created_on=None, created_by=None, cors_profiles=None, security_profiles=None, authentication_profiles=None, inbound_profiles=None, outbound_profiles=None, service_profiles=None, ca_certs=None, tags=None):  # noqa: E501
        """VirtualizedAPI - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._organization_id = None
        self._api_id = None
        self._name = None
        self._version = None
        self._api_routing_key = None
        self._vhost = None
        self._path = None
        self._description_type = None
        self._description_manual = None
        self._description_markdown = None
        self._description_url = None
        self._summary = None
        self._retired = None
        self._expired = None
        self._image = None
        self._retirement_date = None
        self._deprecated = None
        self._state = None
        self._created_on = None
        self._created_by = None
        self._cors_profiles = None
        self._security_profiles = None
        self._authentication_profiles = None
        self._inbound_profiles = None
        self._outbound_profiles = None
        self._service_profiles = None
        self._ca_certs = None
        self._tags = None
        self.discriminator = None

        self.id = id
        self.organization_id = organization_id
        self.api_id = api_id
        self.name = name
        self.version = version
        self.api_routing_key = api_routing_key
        self.vhost = vhost
        self.path = path
        self.description_type = description_type
        self.description_manual = description_manual
        self.description_markdown = description_markdown
        self.description_url = description_url
        self.summary = summary
        self.retired = retired
        self.expired = expired
        self.image = image
        self.retirement_date = retirement_date
        self.deprecated = deprecated
        self.state = state
        if created_on is not None:
            self.created_on = created_on
        if created_by is not None:
            self.created_by = created_by
        self.cors_profiles = cors_profiles
        self.security_profiles = security_profiles
        self.authentication_profiles = authentication_profiles
        self.inbound_profiles = inbound_profiles
        if outbound_profiles is not None:
            self.outbound_profiles = outbound_profiles
        self.service_profiles = service_profiles
        self.ca_certs = ca_certs
        self.tags = tags

    @property
    def id(self):
        """Gets the id of this VirtualizedAPI.  # noqa: E501

        Unique ID of the virtualized API.  # noqa: E501

        :return: The id of this VirtualizedAPI.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VirtualizedAPI.

        Unique ID of the virtualized API.  # noqa: E501

        :param id: The id of this VirtualizedAPI.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def organization_id(self):
        """Gets the organization_id of this VirtualizedAPI.  # noqa: E501

        The organization that created the virtualized API.  # noqa: E501

        :return: The organization_id of this VirtualizedAPI.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this VirtualizedAPI.

        The organization that created the virtualized API.  # noqa: E501

        :param organization_id: The organization_id of this VirtualizedAPI.  # noqa: E501
        :type: str
        """
        self._organization_id = organization_id

    @property
    def api_id(self):
        """Gets the api_id of this VirtualizedAPI.  # noqa: E501

        The identifier of the API that was virtualized.  This is the only attribute that is required to create a virtualized API.  # noqa: E501

        :return: The api_id of this VirtualizedAPI.  # noqa: E501
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this VirtualizedAPI.

        The identifier of the API that was virtualized.  This is the only attribute that is required to create a virtualized API.  # noqa: E501

        :param api_id: The api_id of this VirtualizedAPI.  # noqa: E501
        :type: str
        """
        if api_id is None:
            raise ValueError("Invalid value for `api_id`, must not be `None`")  # noqa: E501

        self._api_id = api_id

    @property
    def name(self):
        """Gets the name of this VirtualizedAPI.  # noqa: E501

        The name of this virtualized API.  # noqa: E501

        :return: The name of this VirtualizedAPI.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VirtualizedAPI.

        The name of this virtualized API.  # noqa: E501

        :param name: The name of this VirtualizedAPI.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def version(self):
        """Gets the version of this VirtualizedAPI.  # noqa: E501

        The API version.  # noqa: E501

        :return: The version of this VirtualizedAPI.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VirtualizedAPI.

        The API version.  # noqa: E501

        :param version: The version of this VirtualizedAPI.  # noqa: E501
        :type: str
        """
        self._version = version

    @property
    def api_routing_key(self):
        """Gets the api_routing_key of this VirtualizedAPI.  # noqa: E501

        The key for routing between two APIs on the same path.  # noqa: E501

        :return: The api_routing_key of this VirtualizedAPI.  # noqa: E501
        :rtype: str
        """
        return self._api_routing_key

    @api_routing_key.setter
    def api_routing_key(self, api_routing_key):
        """Sets the api_routing_key of this VirtualizedAPI.

        The key for routing between two APIs on the same path.  # noqa: E501

        :param api_routing_key: The api_routing_key of this VirtualizedAPI.  # noqa: E501
        :type: str
        """
        self._api_routing_key = api_routing_key

    @property
    def vhost(self):
        """Gets the vhost of this VirtualizedAPI.  # noqa: E501

        The virtual host of this virtualized API.  # noqa: E501

        :return: The vhost of this VirtualizedAPI.  # noqa: E501
        :rtype: str
        """
        return self._vhost

    @vhost.setter
    def vhost(self, vhost):
        """Sets the vhost of this VirtualizedAPI.

        The virtual host of this virtualized API.  # noqa: E501

        :param vhost: The vhost of this VirtualizedAPI.  # noqa: E501
        :type: str
        """
        self._vhost = vhost

    @property
    def path(self):
        """Gets the path of this VirtualizedAPI.  # noqa: E501

        The path that services this virtualized API.  # noqa: E501

        :return: The path of this VirtualizedAPI.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this VirtualizedAPI.

        The path that services this virtualized API.  # noqa: E501

        :param path: The path of this VirtualizedAPI.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def description_type(self):
        """Gets the description_type of this VirtualizedAPI.  # noqa: E501

        Type of descripton to use.  One of: _manual_, _markdown_, _url_, or _original_ (default).  # noqa: E501

        :return: The description_type of this VirtualizedAPI.  # noqa: E501
        :rtype: str
        """
        return self._description_type

    @description_type.setter
    def description_type(self, description_type):
        """Sets the description_type of this VirtualizedAPI.

        Type of descripton to use.  One of: _manual_, _markdown_, _url_, or _original_ (default).  # noqa: E501

        :param description_type: The description_type of this VirtualizedAPI.  # noqa: E501
        :type: str
        """
        if description_type is None:
            raise ValueError("Invalid value for `description_type`, must not be `None`")  # noqa: E501

        self._description_type = description_type

    @property
    def description_manual(self):
        """Gets the description_manual of this VirtualizedAPI.  # noqa: E501

        Markdown string to use as the description of the API.  # noqa: E501

        :return: The description_manual of this VirtualizedAPI.  # noqa: E501
        :rtype: str
        """
        return self._description_manual

    @description_manual.setter
    def description_manual(self, description_manual):
        """Sets the description_manual of this VirtualizedAPI.

        Markdown string to use as the description of the API.  # noqa: E501

        :param description_manual: The description_manual of this VirtualizedAPI.  # noqa: E501
        :type: str
        """
        self._description_manual = description_manual

    @property
    def description_markdown(self):
        """Gets the description_markdown of this VirtualizedAPI.  # noqa: E501

        Markdown file to use as the description of the API within the API Catalog.  # noqa: E501

        :return: The description_markdown of this VirtualizedAPI.  # noqa: E501
        :rtype: str
        """
        return self._description_markdown

    @description_markdown.setter
    def description_markdown(self, description_markdown):
        """Sets the description_markdown of this VirtualizedAPI.

        Markdown file to use as the description of the API within the API Catalog.  # noqa: E501

        :param description_markdown: The description_markdown of this VirtualizedAPI.  # noqa: E501
        :type: str
        """
        self._description_markdown = description_markdown

    @property
    def description_url(self):
        """Gets the description_url of this VirtualizedAPI.  # noqa: E501

        External URL to use as the description of the API.  # noqa: E501

        :return: The description_url of this VirtualizedAPI.  # noqa: E501
        :rtype: str
        """
        return self._description_url

    @description_url.setter
    def description_url(self, description_url):
        """Sets the description_url of this VirtualizedAPI.

        External URL to use as the description of the API.  # noqa: E501

        :param description_url: The description_url of this VirtualizedAPI.  # noqa: E501
        :type: str
        """
        self._description_url = description_url

    @property
    def summary(self):
        """Gets the summary of this VirtualizedAPI.  # noqa: E501

        A short summary description of the API.  # noqa: E501

        :return: The summary of this VirtualizedAPI.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this VirtualizedAPI.

        A short summary description of the API.  # noqa: E501

        :param summary: The summary of this VirtualizedAPI.  # noqa: E501
        :type: str
        """
        self._summary = summary

    @property
    def retired(self):
        """Gets the retired of this VirtualizedAPI.  # noqa: E501

        Immediately retires the virtualized API.  # noqa: E501

        :return: The retired of this VirtualizedAPI.  # noqa: E501
        :rtype: bool
        """
        return self._retired

    @retired.setter
    def retired(self, retired):
        """Sets the retired of this VirtualizedAPI.

        Immediately retires the virtualized API.  # noqa: E501

        :param retired: The retired of this VirtualizedAPI.  # noqa: E501
        :type: bool
        """
        if retired is None:
            raise ValueError("Invalid value for `retired`, must not be `None`")  # noqa: E501

        self._retired = retired

    @property
    def expired(self):
        """Gets the expired of this VirtualizedAPI.  # noqa: E501

        Immediately expires the virtualized API.  # noqa: E501

        :return: The expired of this VirtualizedAPI.  # noqa: E501
        :rtype: bool
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """Sets the expired of this VirtualizedAPI.

        Immediately expires the virtualized API.  # noqa: E501

        :param expired: The expired of this VirtualizedAPI.  # noqa: E501
        :type: bool
        """
        if expired is None:
            raise ValueError("Invalid value for `expired`, must not be `None`")  # noqa: E501

        self._expired = expired

    @property
    def image(self):
        """Gets the image of this VirtualizedAPI.  # noqa: E501

        URI of the image to be used for this virtualized API. To update the image, please refer to the API.  # noqa: E501

        :return: The image of this VirtualizedAPI.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this VirtualizedAPI.

        URI of the image to be used for this virtualized API. To update the image, please refer to the API.  # noqa: E501

        :param image: The image of this VirtualizedAPI.  # noqa: E501
        :type: str
        """
        self._image = image

    @property
    def retirement_date(self):
        """Gets the retirement_date of this VirtualizedAPI.  # noqa: E501

        Date to retire the virtualized API.  If _retired_ is true, this is the date on which it was retired.  # noqa: E501

        :return: The retirement_date of this VirtualizedAPI.  # noqa: E501
        :rtype: int
        """
        return self._retirement_date

    @retirement_date.setter
    def retirement_date(self, retirement_date):
        """Sets the retirement_date of this VirtualizedAPI.

        Date to retire the virtualized API.  If _retired_ is true, this is the date on which it was retired.  # noqa: E501

        :param retirement_date: The retirement_date of this VirtualizedAPI.  # noqa: E501
        :type: int
        """
        if retirement_date is None:
            raise ValueError("Invalid value for `retirement_date`, must not be `None`")  # noqa: E501

        self._retirement_date = retirement_date

    @property
    def deprecated(self):
        """Gets the deprecated of this VirtualizedAPI.  # noqa: E501

        Immediately deprecates the virtualized API.  If deprecated, then _retiredOn_ is optionally used to retire the virtualized API on the specified date.  # noqa: E501

        :return: The deprecated of this VirtualizedAPI.  # noqa: E501
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this VirtualizedAPI.

        Immediately deprecates the virtualized API.  If deprecated, then _retiredOn_ is optionally used to retire the virtualized API on the specified date.  # noqa: E501

        :param deprecated: The deprecated of this VirtualizedAPI.  # noqa: E501
        :type: bool
        """
        if deprecated is None:
            raise ValueError("Invalid value for `deprecated`, must not be `None`")  # noqa: E501

        self._deprecated = deprecated

    @property
    def state(self):
        """Gets the state of this VirtualizedAPI.  # noqa: E501

        The state of the virtualized API.  One of: unpublished, pending, or published.  # noqa: E501

        :return: The state of this VirtualizedAPI.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this VirtualizedAPI.

        The state of the virtualized API.  One of: unpublished, pending, or published.  # noqa: E501

        :param state: The state of this VirtualizedAPI.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def created_on(self):
        """Gets the created_on of this VirtualizedAPI.  # noqa: E501

        Epoch/Unix time stamp when the virtualized API was created.  # noqa: E501

        :return: The created_on of this VirtualizedAPI.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this VirtualizedAPI.

        Epoch/Unix time stamp when the virtualized API was created.  # noqa: E501

        :param created_on: The created_on of this VirtualizedAPI.  # noqa: E501
        :type: int
        """

        self._created_on = created_on

    @property
    def created_by(self):
        """Gets the created_by of this VirtualizedAPI.  # noqa: E501

        The unique identifier for user that created the virtualized API.  # noqa: E501

        :return: The created_by of this VirtualizedAPI.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this VirtualizedAPI.

        The unique identifier for user that created the virtualized API.  # noqa: E501

        :param created_by: The created_by of this VirtualizedAPI.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def cors_profiles(self):
        """Gets the cors_profiles of this VirtualizedAPI.  # noqa: E501

        The suite of CORS Profiles for this virtualized API.  # noqa: E501

        :return: The cors_profiles of this VirtualizedAPI.  # noqa: E501
        :rtype: list[CORSProfile]
        """
        return self._cors_profiles

    @cors_profiles.setter
    def cors_profiles(self, cors_profiles):
        """Sets the cors_profiles of this VirtualizedAPI.

        The suite of CORS Profiles for this virtualized API.  # noqa: E501

        :param cors_profiles: The cors_profiles of this VirtualizedAPI.  # noqa: E501
        :type: list[CORSProfile]
        """
        if cors_profiles is None:
            raise ValueError("Invalid value for `cors_profiles`, must not be `None`")  # noqa: E501

        self._cors_profiles = cors_profiles

    @property
    def security_profiles(self):
        """Gets the security_profiles of this VirtualizedAPI.  # noqa: E501

        The suite of Security Profiles for this virtualized API.  # noqa: E501

        :return: The security_profiles of this VirtualizedAPI.  # noqa: E501
        :rtype: list[SecurityProfile]
        """
        return self._security_profiles

    @security_profiles.setter
    def security_profiles(self, security_profiles):
        """Sets the security_profiles of this VirtualizedAPI.

        The suite of Security Profiles for this virtualized API.  # noqa: E501

        :param security_profiles: The security_profiles of this VirtualizedAPI.  # noqa: E501
        :type: list[SecurityProfile]
        """
        if security_profiles is None:
            raise ValueError("Invalid value for `security_profiles`, must not be `None`")  # noqa: E501

        self._security_profiles = security_profiles

    @property
    def authentication_profiles(self):
        """Gets the authentication_profiles of this VirtualizedAPI.  # noqa: E501

        The suite of Security Profiles for this virtualized API.  # noqa: E501

        :return: The authentication_profiles of this VirtualizedAPI.  # noqa: E501
        :rtype: list[AuthenticationProfile]
        """
        return self._authentication_profiles

    @authentication_profiles.setter
    def authentication_profiles(self, authentication_profiles):
        """Sets the authentication_profiles of this VirtualizedAPI.

        The suite of Security Profiles for this virtualized API.  # noqa: E501

        :param authentication_profiles: The authentication_profiles of this VirtualizedAPI.  # noqa: E501
        :type: list[AuthenticationProfile]
        """
        if authentication_profiles is None:
            raise ValueError("Invalid value for `authentication_profiles`, must not be `None`")  # noqa: E501

        self._authentication_profiles = authentication_profiles

    @property
    def inbound_profiles(self):
        """Gets the inbound_profiles of this VirtualizedAPI.  # noqa: E501

        The inbound profiles that apply to the virtualized API.  There must always a *\\_default* profile.  # noqa: E501

        :return: The inbound_profiles of this VirtualizedAPI.  # noqa: E501
        :rtype: dict(str, InboundProfiles)
        """
        return self._inbound_profiles

    @inbound_profiles.setter
    def inbound_profiles(self, inbound_profiles):
        """Sets the inbound_profiles of this VirtualizedAPI.

        The inbound profiles that apply to the virtualized API.  There must always a *\\_default* profile.  # noqa: E501

        :param inbound_profiles: The inbound_profiles of this VirtualizedAPI.  # noqa: E501
        :type: dict(str, InboundProfiles)
        """
        if inbound_profiles is None:
            raise ValueError("Invalid value for `inbound_profiles`, must not be `None`")  # noqa: E501

        self._inbound_profiles = inbound_profiles

    @property
    def outbound_profiles(self):
        """Gets the outbound_profiles of this VirtualizedAPI.  # noqa: E501

        The outbound profiles that apply to the virtualized API.  There must always a *\\_default* profile.  # noqa: E501

        :return: The outbound_profiles of this VirtualizedAPI.  # noqa: E501
        :rtype: dict(str, OutboundProfiles)
        """
        return self._outbound_profiles

    @outbound_profiles.setter
    def outbound_profiles(self, outbound_profiles):
        """Sets the outbound_profiles of this VirtualizedAPI.

        The outbound profiles that apply to the virtualized API.  There must always a *\\_default* profile.  # noqa: E501

        :param outbound_profiles: The outbound_profiles of this VirtualizedAPI.  # noqa: E501
        :type: dict(str, OutboundProfiles)
        """

        self._outbound_profiles = outbound_profiles

    @property
    def service_profiles(self):
        """Gets the service_profiles of this VirtualizedAPI.  # noqa: E501

        The inbound profiles that apply to the virtualized API.  There must always a *\\_default* profile.  # noqa: E501

        :return: The service_profiles of this VirtualizedAPI.  # noqa: E501
        :rtype: dict(str, ServiceProfiles)
        """
        return self._service_profiles

    @service_profiles.setter
    def service_profiles(self, service_profiles):
        """Sets the service_profiles of this VirtualizedAPI.

        The inbound profiles that apply to the virtualized API.  There must always a *\\_default* profile.  # noqa: E501

        :param service_profiles: The service_profiles of this VirtualizedAPI.  # noqa: E501
        :type: dict(str, ServiceProfiles)
        """
        if service_profiles is None:
            raise ValueError("Invalid value for `service_profiles`, must not be `None`")  # noqa: E501

        self._service_profiles = service_profiles

    @property
    def ca_certs(self):
        """Gets the ca_certs of this VirtualizedAPI.  # noqa: E501

        The outbound profiles that apply to the virtualized API.  There must always a *\\_default* profile.  # noqa: E501

        :return: The ca_certs of this VirtualizedAPI.  # noqa: E501
        :rtype: list[CACert]
        """
        return self._ca_certs

    @ca_certs.setter
    def ca_certs(self, ca_certs):
        """Sets the ca_certs of this VirtualizedAPI.

        The outbound profiles that apply to the virtualized API.  There must always a *\\_default* profile.  # noqa: E501

        :param ca_certs: The ca_certs of this VirtualizedAPI.  # noqa: E501
        :type: list[CACert]
        """
        if ca_certs is None:
            raise ValueError("Invalid value for `ca_certs`, must not be `None`")  # noqa: E501

        self._ca_certs = ca_certs

    @property
    def tags(self):
        """Gets the tags of this VirtualizedAPI.  # noqa: E501

        The list of tags associated with this API. Each tag can have multiple values  # noqa: E501

        :return: The tags of this VirtualizedAPI.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VirtualizedAPI.

        The list of tags associated with this API. Each tag can have multiple values  # noqa: E501

        :param tags: The tags of this VirtualizedAPI.  # noqa: E501
        :type: dict(str, list[str])
        """
        if tags is None:
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

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
        if issubclass(VirtualizedAPI, dict):
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
        if not isinstance(other, VirtualizedAPI):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other