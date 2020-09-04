# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.15   3Di core release: 2.0.11  deployed on:  12:24PM (UTC) on September 02, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class WaterLevelProfileRequest(object):
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
        'geometry': 'Linestring',
        'points_limit': 'int',
        'subscribe': 'bool',
        'subscribe_rate_limit': 'float'
    }

    attribute_map = {
        'geometry': 'geometry',
        'points_limit': 'points_limit',
        'subscribe': 'subscribe',
        'subscribe_rate_limit': 'subscribe_rate_limit'
    }

    def __init__(self, geometry=None, points_limit=None, subscribe=None, subscribe_rate_limit=None, local_vars_configuration=None):  # noqa: E501
        """WaterLevelProfileRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._geometry = None
        self._points_limit = None
        self._subscribe = None
        self._subscribe_rate_limit = None
        self.discriminator = None

        self.geometry = geometry
        if points_limit is not None:
            self.points_limit = points_limit
        self.subscribe = subscribe
        if subscribe_rate_limit is not None:
            self.subscribe_rate_limit = subscribe_rate_limit

    @property
    def geometry(self):
        """Gets the geometry of this WaterLevelProfileRequest.  # noqa: E501


        :return: The geometry of this WaterLevelProfileRequest.  # noqa: E501
        :rtype: Linestring
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this WaterLevelProfileRequest.


        :param geometry: The geometry of this WaterLevelProfileRequest.  # noqa: E501
        :type: Linestring
        """
        if self.local_vars_configuration.client_side_validation and geometry is None:  # noqa: E501
            raise ValueError("Invalid value for `geometry`, must not be `None`")  # noqa: E501

        self._geometry = geometry

    @property
    def points_limit(self):
        """Gets the points_limit of this WaterLevelProfileRequest.  # noqa: E501

        Maximum number of points to return  # noqa: E501

        :return: The points_limit of this WaterLevelProfileRequest.  # noqa: E501
        :rtype: int
        """
        return self._points_limit

    @points_limit.setter
    def points_limit(self, points_limit):
        """Sets the points_limit of this WaterLevelProfileRequest.

        Maximum number of points to return  # noqa: E501

        :param points_limit: The points_limit of this WaterLevelProfileRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                points_limit is not None and points_limit > 200):  # noqa: E501
            raise ValueError("Invalid value for `points_limit`, must be a value less than or equal to `200`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                points_limit is not None and points_limit < 1):  # noqa: E501
            raise ValueError("Invalid value for `points_limit`, must be a value greater than or equal to `1`")  # noqa: E501

        self._points_limit = points_limit

    @property
    def subscribe(self):
        """Gets the subscribe of this WaterLevelProfileRequest.  # noqa: E501

        Subscribe for new results during simulation  # noqa: E501

        :return: The subscribe of this WaterLevelProfileRequest.  # noqa: E501
        :rtype: bool
        """
        return self._subscribe

    @subscribe.setter
    def subscribe(self, subscribe):
        """Sets the subscribe of this WaterLevelProfileRequest.

        Subscribe for new results during simulation  # noqa: E501

        :param subscribe: The subscribe of this WaterLevelProfileRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and subscribe is None:  # noqa: E501
            raise ValueError("Invalid value for `subscribe`, must not be `None`")  # noqa: E501

        self._subscribe = subscribe

    @property
    def subscribe_rate_limit(self):
        """Gets the subscribe_rate_limit of this WaterLevelProfileRequest.  # noqa: E501

        Max number of items per second for subscription  # noqa: E501

        :return: The subscribe_rate_limit of this WaterLevelProfileRequest.  # noqa: E501
        :rtype: float
        """
        return self._subscribe_rate_limit

    @subscribe_rate_limit.setter
    def subscribe_rate_limit(self, subscribe_rate_limit):
        """Sets the subscribe_rate_limit of this WaterLevelProfileRequest.

        Max number of items per second for subscription  # noqa: E501

        :param subscribe_rate_limit: The subscribe_rate_limit of this WaterLevelProfileRequest.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                subscribe_rate_limit is not None and subscribe_rate_limit > 1):  # noqa: E501
            raise ValueError("Invalid value for `subscribe_rate_limit`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                subscribe_rate_limit is not None and subscribe_rate_limit < 0.25):  # noqa: E501
            raise ValueError("Invalid value for `subscribe_rate_limit`, must be a value greater than or equal to `0.25`")  # noqa: E501

        self._subscribe_rate_limit = subscribe_rate_limit

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
        if not isinstance(other, WaterLevelProfileRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WaterLevelProfileRequest):
            return True

        return self.to_dict() != other.to_dict()
