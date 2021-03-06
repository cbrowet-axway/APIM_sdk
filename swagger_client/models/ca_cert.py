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


class CACert(object):
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
        'cert_blob': 'str',
        'name': 'str',
        'alias': 'str',
        'subject': 'str',
        'issuer': 'str',
        'version': 'int',
        'not_valid_before': 'int',
        'not_valid_after': 'int',
        'signature_algorithm': 'str',
        'sha1_fingerprint': 'str',
        'md5_fingerprint': 'str',
        'expired': 'bool',
        'not_yet_valid': 'bool',
        'inbound': 'bool',
        'outbound': 'bool'
    }

    attribute_map = {
        'cert_blob': 'certBlob',
        'name': 'name',
        'alias': 'alias',
        'subject': 'subject',
        'issuer': 'issuer',
        'version': 'version',
        'not_valid_before': 'notValidBefore',
        'not_valid_after': 'notValidAfter',
        'signature_algorithm': 'signatureAlgorithm',
        'sha1_fingerprint': 'sha1Fingerprint',
        'md5_fingerprint': 'md5Fingerprint',
        'expired': 'expired',
        'not_yet_valid': 'notYetValid',
        'inbound': 'inbound',
        'outbound': 'outbound'
    }

    def __init__(self, cert_blob=None, name=None, alias=None, subject=None, issuer=None, version=None, not_valid_before=None, not_valid_after=None, signature_algorithm=None, sha1_fingerprint=None, md5_fingerprint=None, expired=False, not_yet_valid=False, inbound=False, outbound=False):  # noqa: E501
        """CACert - a model defined in Swagger"""  # noqa: E501

        self._cert_blob = None
        self._name = None
        self._alias = None
        self._subject = None
        self._issuer = None
        self._version = None
        self._not_valid_before = None
        self._not_valid_after = None
        self._signature_algorithm = None
        self._sha1_fingerprint = None
        self._md5_fingerprint = None
        self._expired = None
        self._not_yet_valid = None
        self._inbound = None
        self._outbound = None
        self.discriminator = None

        if cert_blob is not None:
            self.cert_blob = cert_blob
        if name is not None:
            self.name = name
        if alias is not None:
            self.alias = alias
        if subject is not None:
            self.subject = subject
        if issuer is not None:
            self.issuer = issuer
        if version is not None:
            self.version = version
        if not_valid_before is not None:
            self.not_valid_before = not_valid_before
        if not_valid_after is not None:
            self.not_valid_after = not_valid_after
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm
        if sha1_fingerprint is not None:
            self.sha1_fingerprint = sha1_fingerprint
        if md5_fingerprint is not None:
            self.md5_fingerprint = md5_fingerprint
        if expired is not None:
            self.expired = expired
        if not_yet_valid is not None:
            self.not_yet_valid = not_yet_valid
        if inbound is not None:
            self.inbound = inbound
        if outbound is not None:
            self.outbound = outbound

    @property
    def cert_blob(self):
        """Gets the cert_blob of this CACert.  # noqa: E501

        Raw certificate data  # noqa: E501

        :return: The cert_blob of this CACert.  # noqa: E501
        :rtype: str
        """
        return self._cert_blob

    @cert_blob.setter
    def cert_blob(self, cert_blob):
        """Sets the cert_blob of this CACert.

        Raw certificate data  # noqa: E501

        :param cert_blob: The cert_blob of this CACert.  # noqa: E501
        :type: str
        """

        self._cert_blob = cert_blob

    @property
    def name(self):
        """Gets the name of this CACert.  # noqa: E501

        Name of the certificate  # noqa: E501

        :return: The name of this CACert.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CACert.

        Name of the certificate  # noqa: E501

        :param name: The name of this CACert.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def alias(self):
        """Gets the alias of this CACert.  # noqa: E501

        Certificate alias  # noqa: E501

        :return: The alias of this CACert.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this CACert.

        Certificate alias  # noqa: E501

        :param alias: The alias of this CACert.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def subject(self):
        """Gets the subject of this CACert.  # noqa: E501

        Certificate subject  # noqa: E501

        :return: The subject of this CACert.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this CACert.

        Certificate subject  # noqa: E501

        :param subject: The subject of this CACert.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def issuer(self):
        """Gets the issuer of this CACert.  # noqa: E501

        Certificate issuer  # noqa: E501

        :return: The issuer of this CACert.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this CACert.

        Certificate issuer  # noqa: E501

        :param issuer: The issuer of this CACert.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def version(self):
        """Gets the version of this CACert.  # noqa: E501

        Version of the certificate  # noqa: E501

        :return: The version of this CACert.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CACert.

        Version of the certificate  # noqa: E501

        :param version: The version of this CACert.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def not_valid_before(self):
        """Gets the not_valid_before of this CACert.  # noqa: E501

        Start date of the certificate  # noqa: E501

        :return: The not_valid_before of this CACert.  # noqa: E501
        :rtype: int
        """
        return self._not_valid_before

    @not_valid_before.setter
    def not_valid_before(self, not_valid_before):
        """Sets the not_valid_before of this CACert.

        Start date of the certificate  # noqa: E501

        :param not_valid_before: The not_valid_before of this CACert.  # noqa: E501
        :type: int
        """

        self._not_valid_before = not_valid_before

    @property
    def not_valid_after(self):
        """Gets the not_valid_after of this CACert.  # noqa: E501

        Expiry date of the certificate  # noqa: E501

        :return: The not_valid_after of this CACert.  # noqa: E501
        :rtype: int
        """
        return self._not_valid_after

    @not_valid_after.setter
    def not_valid_after(self, not_valid_after):
        """Sets the not_valid_after of this CACert.

        Expiry date of the certificate  # noqa: E501

        :param not_valid_after: The not_valid_after of this CACert.  # noqa: E501
        :type: int
        """

        self._not_valid_after = not_valid_after

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this CACert.  # noqa: E501

        The algorithm used to sign the certificate.  # noqa: E501

        :return: The signature_algorithm of this CACert.  # noqa: E501
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this CACert.

        The algorithm used to sign the certificate.  # noqa: E501

        :param signature_algorithm: The signature_algorithm of this CACert.  # noqa: E501
        :type: str
        """

        self._signature_algorithm = signature_algorithm

    @property
    def sha1_fingerprint(self):
        """Gets the sha1_fingerprint of this CACert.  # noqa: E501

        SHA1 fingerprint.  # noqa: E501

        :return: The sha1_fingerprint of this CACert.  # noqa: E501
        :rtype: str
        """
        return self._sha1_fingerprint

    @sha1_fingerprint.setter
    def sha1_fingerprint(self, sha1_fingerprint):
        """Sets the sha1_fingerprint of this CACert.

        SHA1 fingerprint.  # noqa: E501

        :param sha1_fingerprint: The sha1_fingerprint of this CACert.  # noqa: E501
        :type: str
        """

        self._sha1_fingerprint = sha1_fingerprint

    @property
    def md5_fingerprint(self):
        """Gets the md5_fingerprint of this CACert.  # noqa: E501

        MD5 fingerprint.  # noqa: E501

        :return: The md5_fingerprint of this CACert.  # noqa: E501
        :rtype: str
        """
        return self._md5_fingerprint

    @md5_fingerprint.setter
    def md5_fingerprint(self, md5_fingerprint):
        """Sets the md5_fingerprint of this CACert.

        MD5 fingerprint.  # noqa: E501

        :param md5_fingerprint: The md5_fingerprint of this CACert.  # noqa: E501
        :type: str
        """

        self._md5_fingerprint = md5_fingerprint

    @property
    def expired(self):
        """Gets the expired of this CACert.  # noqa: E501

        Flag indicating whether or not the certificate is expired.  # noqa: E501

        :return: The expired of this CACert.  # noqa: E501
        :rtype: bool
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """Sets the expired of this CACert.

        Flag indicating whether or not the certificate is expired.  # noqa: E501

        :param expired: The expired of this CACert.  # noqa: E501
        :type: bool
        """

        self._expired = expired

    @property
    def not_yet_valid(self):
        """Gets the not_yet_valid of this CACert.  # noqa: E501

        Flag indicating whether or not the certificate is valid yet.  # noqa: E501

        :return: The not_yet_valid of this CACert.  # noqa: E501
        :rtype: bool
        """
        return self._not_yet_valid

    @not_yet_valid.setter
    def not_yet_valid(self, not_yet_valid):
        """Sets the not_yet_valid of this CACert.

        Flag indicating whether or not the certificate is valid yet.  # noqa: E501

        :param not_yet_valid: The not_yet_valid of this CACert.  # noqa: E501
        :type: bool
        """

        self._not_yet_valid = not_yet_valid

    @property
    def inbound(self):
        """Gets the inbound of this CACert.  # noqa: E501

        Flag indicating whether this certificate is used for inbound SSL connections when invoking the virtualized API.  # noqa: E501

        :return: The inbound of this CACert.  # noqa: E501
        :rtype: bool
        """
        return self._inbound

    @inbound.setter
    def inbound(self, inbound):
        """Sets the inbound of this CACert.

        Flag indicating whether this certificate is used for inbound SSL connections when invoking the virtualized API.  # noqa: E501

        :param inbound: The inbound of this CACert.  # noqa: E501
        :type: bool
        """

        self._inbound = inbound

    @property
    def outbound(self):
        """Gets the outbound of this CACert.  # noqa: E501

        Flag indicating whether this certificate is used for outbound SSL connections when invoking the virtualized API.  # noqa: E501

        :return: The outbound of this CACert.  # noqa: E501
        :rtype: bool
        """
        return self._outbound

    @outbound.setter
    def outbound(self, outbound):
        """Sets the outbound of this CACert.

        Flag indicating whether this certificate is used for outbound SSL connections when invoking the virtualized API.  # noqa: E501

        :param outbound: The outbound of this CACert.  # noqa: E501
        :type: bool
        """

        self._outbound = outbound

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
        if issubclass(CACert, dict):
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
        if not isinstance(other, CACert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
