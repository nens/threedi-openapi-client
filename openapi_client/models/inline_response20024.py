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


class InlineResponse20024(object):
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
        'next': 'str',
        'previous': 'str',
        'count': 'int',
        'results': 'list[ThreediModelFlowState]'
    }

    attribute_map = {
        'next': 'next',
        'previous': 'previous',
        'count': 'count',
        'results': 'results'
    }

    def __init__(self, next=None, previous=None, count=None, results=None):  # noqa: E501
        """InlineResponse20024 - a model defined in OpenAPI"""  # noqa: E501

        self._next = None
        self._previous = None
        self._count = None
        self._results = None
        self.discriminator = None

        self.next = next
        self.previous = previous
        self.count = count
        self.results = results

    @property
    def next(self):
        """Gets the next of this InlineResponse20024.  # noqa: E501


        :return: The next of this InlineResponse20024.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this InlineResponse20024.


        :param next: The next of this InlineResponse20024.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def previous(self):
        """Gets the previous of this InlineResponse20024.  # noqa: E501


        :return: The previous of this InlineResponse20024.  # noqa: E501
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this InlineResponse20024.


        :param previous: The previous of this InlineResponse20024.  # noqa: E501
        :type: str
        """

        self._previous = previous

    @property
    def count(self):
        """Gets the count of this InlineResponse20024.  # noqa: E501


        :return: The count of this InlineResponse20024.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this InlineResponse20024.


        :param count: The count of this InlineResponse20024.  # noqa: E501
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def results(self):
        """Gets the results of this InlineResponse20024.  # noqa: E501


        :return: The results of this InlineResponse20024.  # noqa: E501
        :rtype: list[ThreediModelFlowState]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this InlineResponse20024.


        :param results: The results of this InlineResponse20024.  # noqa: E501
        :type: list[ThreediModelFlowState]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

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
        if not isinstance(other, InlineResponse20024):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
