# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 0.0.29   3Di core release: 2.0.3  deployed on:  02:21PM (UTC) on December 02, 2019  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Download(object):
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
        'get_url': 'str',
        'etag': 'str',
        'size': 'int'
    }

    attribute_map = {
        'get_url': 'get_url',
        'etag': 'etag',
        'size': 'size'
    }

    def __init__(self, get_url=None, etag=None, size=None, local_vars_configuration=None):  # noqa: E501
        """Download - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._get_url = None
        self._etag = None
        self._size = None
        self.discriminator = None

        if get_url is not None:
            self.get_url = get_url
        if etag is not None:
            self.etag = etag
        if size is not None:
            self.size = size

    @property
    def get_url(self):
        """Gets the get_url of this Download.  # noqa: E501


        :return: The get_url of this Download.  # noqa: E501
        :rtype: str
        """
        return self._get_url

    @get_url.setter
    def get_url(self, get_url):
        """Sets the get_url of this Download.


        :param get_url: The get_url of this Download.  # noqa: E501
        :type: str
        """

        self._get_url = get_url

    @property
    def etag(self):
        """Gets the etag of this Download.  # noqa: E501

        Optional eTag (md5sum)  # noqa: E501

        :return: The etag of this Download.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this Download.

        Optional eTag (md5sum)  # noqa: E501

        :param etag: The etag of this Download.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                etag is not None and len(etag) < 1):
            raise ValueError("Invalid value for `etag`, length must be greater than or equal to `1`")  # noqa: E501

        self._etag = etag

    @property
    def size(self):
        """Gets the size of this Download.  # noqa: E501

        Filesize in bytes  # noqa: E501

        :return: The size of this Download.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Download.

        Filesize in bytes  # noqa: E501

        :param size: The size of this Download.  # noqa: E501
        :type: int
        """

        self._size = size

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
        if not isinstance(other, Download):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Download):
            return True

        return self.to_dict() != other.to_dict()
