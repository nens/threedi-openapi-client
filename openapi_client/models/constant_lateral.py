# coding: utf-8

"""
    3DI API

    3DI simulation API  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ConstantLateral(object):
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
        'offset': 'int',
        'duration': 'int',
        'value': 'float',
        'units': 'str',
        'epsg': 'int',
        'point': 'str',
        'connection_node': 'int',
        'state': 'str',
        'state_detail': 'str',
        'node': 'int',
        'id': 'int'
    }

    attribute_map = {
        'url': 'url',
        'simulation': 'simulation',
        'offset': 'offset',
        'duration': 'duration',
        'value': 'value',
        'units': 'units',
        'epsg': 'epsg',
        'point': 'point',
        'connection_node': 'connection_node',
        'state': 'state',
        'state_detail': 'state_detail',
        'node': 'node',
        'id': 'id'
    }

    def __init__(self, url=None, simulation=None, offset=None, duration=None, value=None, units=None, epsg=None, point=None, connection_node=None, state=None, state_detail=None, node=None, id=None):  # noqa: E501
        """ConstantLateral - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._simulation = None
        self._offset = None
        self._duration = None
        self._value = None
        self._units = None
        self._epsg = None
        self._point = None
        self._connection_node = None
        self._state = None
        self._state_detail = None
        self._node = None
        self._id = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if simulation is not None:
            self.simulation = simulation
        self.offset = offset
        self.duration = duration
        self.value = value
        self.units = units
        self.epsg = epsg
        self.point = point
        self.connection_node = connection_node
        if state is not None:
            self.state = state
        if state_detail is not None:
            self.state_detail = state_detail
        if node is not None:
            self.node = node
        if id is not None:
            self.id = id

    @property
    def url(self):
        """Gets the url of this ConstantLateral.  # noqa: E501


        :return: The url of this ConstantLateral.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ConstantLateral.


        :param url: The url of this ConstantLateral.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def simulation(self):
        """Gets the simulation of this ConstantLateral.  # noqa: E501


        :return: The simulation of this ConstantLateral.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this ConstantLateral.


        :param simulation: The simulation of this ConstantLateral.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def offset(self):
        """Gets the offset of this ConstantLateral.  # noqa: E501

        offset of event in simulation in seconds  # noqa: E501

        :return: The offset of this ConstantLateral.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ConstantLateral.

        offset of event in simulation in seconds  # noqa: E501

        :param offset: The offset of this ConstantLateral.  # noqa: E501
        :type: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501
        if offset is not None and offset > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if offset is not None and offset < 0:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._offset = offset

    @property
    def duration(self):
        """Gets the duration of this ConstantLateral.  # noqa: E501

        Duration of event in seconds  # noqa: E501

        :return: The duration of this ConstantLateral.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ConstantLateral.

        Duration of event in seconds  # noqa: E501

        :param duration: The duration of this ConstantLateral.  # noqa: E501
        :type: int
        """
        if duration is not None and duration > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if duration is not None and duration < 0:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value greater than or equal to `0`")  # noqa: E501

        self._duration = duration

    @property
    def value(self):
        """Gets the value of this ConstantLateral.  # noqa: E501


        :return: The value of this ConstantLateral.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ConstantLateral.


        :param value: The value of this ConstantLateral.  # noqa: E501
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def units(self):
        """Gets the units of this ConstantLateral.  # noqa: E501

        'm3/s' (only option for now)  # noqa: E501

        :return: The units of this ConstantLateral.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this ConstantLateral.

        'm3/s' (only option for now)  # noqa: E501

        :param units: The units of this ConstantLateral.  # noqa: E501
        :type: str
        """
        if units is None:
            raise ValueError("Invalid value for `units`, must not be `None`")  # noqa: E501
        allowed_values = ["m3/s"]  # noqa: E501
        if units not in allowed_values:
            raise ValueError(
                "Invalid value for `units` ({0}), must be one of {1}"  # noqa: E501
                .format(units, allowed_values)
            )

        self._units = units

    @property
    def epsg(self):
        """Gets the epsg of this ConstantLateral.  # noqa: E501


        :return: The epsg of this ConstantLateral.  # noqa: E501
        :rtype: int
        """
        return self._epsg

    @epsg.setter
    def epsg(self, epsg):
        """Sets the epsg of this ConstantLateral.


        :param epsg: The epsg of this ConstantLateral.  # noqa: E501
        :type: int
        """
        if epsg is not None and epsg > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `epsg`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if epsg is not None and epsg < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `epsg`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._epsg = epsg

    @property
    def point(self):
        """Gets the point of this ConstantLateral.  # noqa: E501


        :return: The point of this ConstantLateral.  # noqa: E501
        :rtype: str
        """
        return self._point

    @point.setter
    def point(self, point):
        """Sets the point of this ConstantLateral.


        :param point: The point of this ConstantLateral.  # noqa: E501
        :type: str
        """

        self._point = point

    @property
    def connection_node(self):
        """Gets the connection_node of this ConstantLateral.  # noqa: E501


        :return: The connection_node of this ConstantLateral.  # noqa: E501
        :rtype: int
        """
        return self._connection_node

    @connection_node.setter
    def connection_node(self, connection_node):
        """Sets the connection_node of this ConstantLateral.


        :param connection_node: The connection_node of this ConstantLateral.  # noqa: E501
        :type: int
        """
        if connection_node is not None and connection_node > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `connection_node`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if connection_node is not None and connection_node < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `connection_node`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._connection_node = connection_node

    @property
    def state(self):
        """Gets the state of this ConstantLateral.  # noqa: E501


        :return: The state of this ConstantLateral.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ConstantLateral.


        :param state: The state of this ConstantLateral.  # noqa: E501
        :type: str
        """
        allowed_values = ["processing", "valid", "invalid"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def state_detail(self):
        """Gets the state_detail of this ConstantLateral.  # noqa: E501


        :return: The state_detail of this ConstantLateral.  # noqa: E501
        :rtype: str
        """
        return self._state_detail

    @state_detail.setter
    def state_detail(self, state_detail):
        """Sets the state_detail of this ConstantLateral.


        :param state_detail: The state_detail of this ConstantLateral.  # noqa: E501
        :type: str
        """

        self._state_detail = state_detail

    @property
    def node(self):
        """Gets the node of this ConstantLateral.  # noqa: E501


        :return: The node of this ConstantLateral.  # noqa: E501
        :rtype: int
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this ConstantLateral.


        :param node: The node of this ConstantLateral.  # noqa: E501
        :type: int
        """

        self._node = node

    @property
    def id(self):
        """Gets the id of this ConstantLateral.  # noqa: E501


        :return: The id of this ConstantLateral.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConstantLateral.


        :param id: The id of this ConstantLateral.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if not isinstance(other, ConstantLateral):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
