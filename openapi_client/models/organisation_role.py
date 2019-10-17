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


class OrganisationRole(object):
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
        'user': 'str',
        'role': 'str',
        'organisation': 'str',
        'organisation_name': 'str'
    }

    attribute_map = {
        'url': 'url',
        'user': 'user',
        'role': 'role',
        'organisation': 'organisation',
        'organisation_name': 'organisation_name'
    }

    def __init__(self, url=None, user=None, role=None, organisation=None, organisation_name=None):  # noqa: E501
        """OrganisationRole - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._user = None
        self._role = None
        self._organisation = None
        self._organisation_name = None
        self.discriminator = None

        if url is not None:
            self.url = url
        self.user = user
        self.role = role
        self.organisation = organisation
        if organisation_name is not None:
            self.organisation_name = organisation_name

    @property
    def url(self):
        """Gets the url of this OrganisationRole.  # noqa: E501


        :return: The url of this OrganisationRole.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this OrganisationRole.


        :param url: The url of this OrganisationRole.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def user(self):
        """Gets the user of this OrganisationRole.  # noqa: E501


        :return: The user of this OrganisationRole.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this OrganisationRole.


        :param user: The user of this OrganisationRole.  # noqa: E501
        :type: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501
        if user is not None and not re.search(r'^[\w.@+-]+$', user):  # noqa: E501
            raise ValueError(r"Invalid value for `user`, must be a follow pattern or equal to `/^[\w.@+-]+$/`")  # noqa: E501

        self._user = user

    @property
    def role(self):
        """Gets the role of this OrganisationRole.  # noqa: E501


        :return: The role of this OrganisationRole.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this OrganisationRole.


        :param role: The role of this OrganisationRole.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def organisation(self):
        """Gets the organisation of this OrganisationRole.  # noqa: E501


        :return: The organisation of this OrganisationRole.  # noqa: E501
        :rtype: str
        """
        return self._organisation

    @organisation.setter
    def organisation(self, organisation):
        """Sets the organisation of this OrganisationRole.


        :param organisation: The organisation of this OrganisationRole.  # noqa: E501
        :type: str
        """
        if organisation is None:
            raise ValueError("Invalid value for `organisation`, must not be `None`")  # noqa: E501

        self._organisation = organisation

    @property
    def organisation_name(self):
        """Gets the organisation_name of this OrganisationRole.  # noqa: E501


        :return: The organisation_name of this OrganisationRole.  # noqa: E501
        :rtype: str
        """
        return self._organisation_name

    @organisation_name.setter
    def organisation_name(self, organisation_name):
        """Sets the organisation_name of this OrganisationRole.


        :param organisation_name: The organisation_name of this OrganisationRole.  # noqa: E501
        :type: str
        """

        self._organisation_name = organisation_name

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
        if not isinstance(other, OrganisationRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
