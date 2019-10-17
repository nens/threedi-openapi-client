# coding: utf-8

"""
    3DI API

    3DI simulation API   Framework release: 0.0.10   3Di core release: 2.0.2.dev6  deployed on:  01:51PM (UTC) on October 07, 2019  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class TwoDWaterLevel(object):
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
        'simulation': 'str',
        'value': 'float'
    }

    attribute_map = {
        'url': 'url',
        'simulation': 'simulation',
        'value': 'value'
    }

    def __init__(self, url=None, simulation=None, value=None):  # noqa: E501
        """TwoDWaterLevel - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._simulation = None
        self._value = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if simulation is not None:
            self.simulation = simulation
        self.value = value

    @property
    def url(self):
        """Gets the url of this TwoDWaterLevel.  # noqa: E501


        :return: The url of this TwoDWaterLevel.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TwoDWaterLevel.


        :param url: The url of this TwoDWaterLevel.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def simulation(self):
        """Gets the simulation of this TwoDWaterLevel.  # noqa: E501


        :return: The simulation of this TwoDWaterLevel.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this TwoDWaterLevel.


        :param simulation: The simulation of this TwoDWaterLevel.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def value(self):
        """Gets the value of this TwoDWaterLevel.  # noqa: E501


        :return: The value of this TwoDWaterLevel.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TwoDWaterLevel.


        :param value: The value of this TwoDWaterLevel.  # noqa: E501
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, TwoDWaterLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
