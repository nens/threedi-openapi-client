# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.10   3Di core release: 2.0.10  deployed on:  09:44AM (UTC) on July 02, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class RasterEditUrls(object):
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
        'raster_type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'raster_type': 'raster_type',
        'url': 'url'
    }

    def __init__(self, raster_type=None, url=None, local_vars_configuration=None):  # noqa: E501
        """RasterEditUrls - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._raster_type = None
        self._url = None
        self.discriminator = None

        self.raster_type = raster_type
        self.url = url

    @property
    def raster_type(self):
        """Gets the raster_type of this RasterEditUrls.  # noqa: E501


        :return: The raster_type of this RasterEditUrls.  # noqa: E501
        :rtype: str
        """
        return self._raster_type

    @raster_type.setter
    def raster_type(self, raster_type):
        """Sets the raster_type of this RasterEditUrls.


        :param raster_type: The raster_type of this RasterEditUrls.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and raster_type is None:  # noqa: E501
            raise ValueError("Invalid value for `raster_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                raster_type is not None and len(raster_type) < 1):
            raise ValueError("Invalid value for `raster_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._raster_type = raster_type

    @property
    def url(self):
        """Gets the url of this RasterEditUrls.  # noqa: E501


        :return: The url of this RasterEditUrls.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RasterEditUrls.


        :param url: The url of this RasterEditUrls.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

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
        if not isinstance(other, RasterEditUrls):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RasterEditUrls):
            return True

        return self.to_dict() != other.to_dict()
