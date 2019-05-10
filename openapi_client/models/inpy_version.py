# coding: utf-8

"""
    3DI API

    3DI simulation API  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InpyVersion(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'url': 'str',
        'threedi_version': 'str',
        'threedicore_version': 'str',
        'slug': 'str'
    }

    attribute_map = {
        'url': 'url',
        'threedi_version': 'threedi_version',
        'threedicore_version': 'threedicore_version',
        'slug': 'slug'
    }

    def __init__(self, url=None, threedi_version=None, threedicore_version=None, slug=None):  # noqa: E501
        """InpyVersion - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._threedi_version = None
        self._threedicore_version = None
        self._slug = None
        self.discriminator = None

        if url is not None:
            self.url = url
        self.threedi_version = threedi_version
        self.threedicore_version = threedicore_version
        if slug is not None:
            self.slug = slug

    @property
    def url(self):
        """Gets the url of this InpyVersion.  # noqa: E501


        :return: The url of this InpyVersion.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InpyVersion.


        :param url: The url of this InpyVersion.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def threedi_version(self):
        """Gets the threedi_version of this InpyVersion.  # noqa: E501


        :return: The threedi_version of this InpyVersion.  # noqa: E501
        :rtype: str
        """
        return self._threedi_version

    @threedi_version.setter
    def threedi_version(self, threedi_version):
        """Sets the threedi_version of this InpyVersion.


        :param threedi_version: The threedi_version of this InpyVersion.  # noqa: E501
        :type: str
        """
        if threedi_version is None:
            raise ValueError("Invalid value for `threedi_version`, must not be `None`")  # noqa: E501
        if threedi_version is not None and len(threedi_version) > 80:
            raise ValueError("Invalid value for `threedi_version`, length must be less than or equal to `80`")  # noqa: E501
        if threedi_version is not None and len(threedi_version) < 1:
            raise ValueError("Invalid value for `threedi_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._threedi_version = threedi_version

    @property
    def threedicore_version(self):
        """Gets the threedicore_version of this InpyVersion.  # noqa: E501


        :return: The threedicore_version of this InpyVersion.  # noqa: E501
        :rtype: str
        """
        return self._threedicore_version

    @threedicore_version.setter
    def threedicore_version(self, threedicore_version):
        """Sets the threedicore_version of this InpyVersion.


        :param threedicore_version: The threedicore_version of this InpyVersion.  # noqa: E501
        :type: str
        """
        if threedicore_version is None:
            raise ValueError("Invalid value for `threedicore_version`, must not be `None`")  # noqa: E501
        if threedicore_version is not None and len(threedicore_version) > 80:
            raise ValueError("Invalid value for `threedicore_version`, length must be less than or equal to `80`")  # noqa: E501
        if threedicore_version is not None and len(threedicore_version) < 1:
            raise ValueError("Invalid value for `threedicore_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._threedicore_version = threedicore_version

    @property
    def slug(self):
        """Gets the slug of this InpyVersion.  # noqa: E501


        :return: The slug of this InpyVersion.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this InpyVersion.


        :param slug: The slug of this InpyVersion.  # noqa: E501
        :type: str
        """
        if slug is not None and len(slug) < 1:
            raise ValueError("Invalid value for `slug`, length must be greater than or equal to `1`")  # noqa: E501

        self._slug = slug

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InpyVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
