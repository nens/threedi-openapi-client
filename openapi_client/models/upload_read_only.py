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


class UploadReadOnly(object):
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
        'filename': 'str',
        'state': 'str'
    }

    attribute_map = {
        'url': 'url',
        'filename': 'filename',
        'state': 'state'
    }

    def __init__(self, url=None, filename=None, state=None):  # noqa: E501
        """UploadReadOnly - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._filename = None
        self._state = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if filename is not None:
            self.filename = filename
        if state is not None:
            self.state = state

    @property
    def url(self):
        """Gets the url of this UploadReadOnly.  # noqa: E501


        :return: The url of this UploadReadOnly.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UploadReadOnly.


        :param url: The url of this UploadReadOnly.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def filename(self):
        """Gets the filename of this UploadReadOnly.  # noqa: E501


        :return: The filename of this UploadReadOnly.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this UploadReadOnly.


        :param filename: The filename of this UploadReadOnly.  # noqa: E501
        :type: str
        """
        if filename is not None and len(filename) < 1:
            raise ValueError("Invalid value for `filename`, length must be greater than or equal to `1`")  # noqa: E501

        self._filename = filename

    @property
    def state(self):
        """Gets the state of this UploadReadOnly.  # noqa: E501


        :return: The state of this UploadReadOnly.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this UploadReadOnly.


        :param state: The state of this UploadReadOnly.  # noqa: E501
        :type: str
        """
        allowed_values = ["created", "uploaded", "processed"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

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
        if not isinstance(other, UploadReadOnly):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
