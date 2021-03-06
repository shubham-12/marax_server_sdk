# coding: utf-8

"""
    marax-server-sdk

    Marax Server SDK to send transactional events from client server to marax server  # noqa: E501

    The version of the OpenAPI document: 0.2.0
    Contact: team@marax.ai
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from marax_server_sdk.configuration import Configuration


class RequestBody(object):
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
        'event': 'str',
        'properties': 'RequestBodyProperties'
    }

    attribute_map = {
        'event': 'event',
        'properties': 'properties'
    }

    def __init__(self, event=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """RequestBody - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._event = None
        self._properties = None
        self.discriminator = None

        self.event = event
        self.properties = properties

    @property
    def event(self):
        """Gets the event of this RequestBody.  # noqa: E501


        :return: The event of this RequestBody.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this RequestBody.


        :param event: The event of this RequestBody.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and event is None:  # noqa: E501
            raise ValueError("Invalid value for `event`, must not be `None`")  # noqa: E501

        self._event = event

    @property
    def properties(self):
        """Gets the properties of this RequestBody.  # noqa: E501


        :return: The properties of this RequestBody.  # noqa: E501
        :rtype: RequestBodyProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this RequestBody.


        :param properties: The properties of this RequestBody.  # noqa: E501
        :type: RequestBodyProperties
        """
        if self.local_vars_configuration.client_side_validation and properties is None:  # noqa: E501
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

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
        if not isinstance(other, RequestBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequestBody):
            return True

        return self.to_dict() != other.to_dict()
