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


class RequestBodyPropertiesFulfillment(object):
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
        'type': 'str',
        'price': 'float',
        'price_units': 'str',
        'discount': 'float',
        'discount_type': 'str'
    }

    attribute_map = {
        'type': 'type',
        'price': 'price',
        'price_units': 'priceUnits',
        'discount': 'discount',
        'discount_type': 'discountType'
    }

    def __init__(self, type=None, price=None, price_units=None, discount=None, discount_type=None, local_vars_configuration=None):  # noqa: E501
        """RequestBodyPropertiesFulfillment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._price = None
        self._price_units = None
        self._discount = None
        self._discount_type = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if price is not None:
            self.price = price
        if price_units is not None:
            self.price_units = price_units
        if discount is not None:
            self.discount = discount
        if discount_type is not None:
            self.discount_type = discount_type

    @property
    def type(self):
        """Gets the type of this RequestBodyPropertiesFulfillment.  # noqa: E501


        :return: The type of this RequestBodyPropertiesFulfillment.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RequestBodyPropertiesFulfillment.


        :param type: The type of this RequestBodyPropertiesFulfillment.  # noqa: E501
        :type: str
        """
        allowed_values = ["surcharge", "convenience", "delivery", "packaging"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def price(self):
        """Gets the price of this RequestBodyPropertiesFulfillment.  # noqa: E501


        :return: The price of this RequestBodyPropertiesFulfillment.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this RequestBodyPropertiesFulfillment.


        :param price: The price of this RequestBodyPropertiesFulfillment.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def price_units(self):
        """Gets the price_units of this RequestBodyPropertiesFulfillment.  # noqa: E501


        :return: The price_units of this RequestBodyPropertiesFulfillment.  # noqa: E501
        :rtype: str
        """
        return self._price_units

    @price_units.setter
    def price_units(self, price_units):
        """Sets the price_units of this RequestBodyPropertiesFulfillment.


        :param price_units: The price_units of this RequestBodyPropertiesFulfillment.  # noqa: E501
        :type: str
        """

        self._price_units = price_units

    @property
    def discount(self):
        """Gets the discount of this RequestBodyPropertiesFulfillment.  # noqa: E501


        :return: The discount of this RequestBodyPropertiesFulfillment.  # noqa: E501
        :rtype: float
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this RequestBodyPropertiesFulfillment.


        :param discount: The discount of this RequestBodyPropertiesFulfillment.  # noqa: E501
        :type: float
        """

        self._discount = discount

    @property
    def discount_type(self):
        """Gets the discount_type of this RequestBodyPropertiesFulfillment.  # noqa: E501


        :return: The discount_type of this RequestBodyPropertiesFulfillment.  # noqa: E501
        :rtype: str
        """
        return self._discount_type

    @discount_type.setter
    def discount_type(self, discount_type):
        """Sets the discount_type of this RequestBodyPropertiesFulfillment.


        :param discount_type: The discount_type of this RequestBodyPropertiesFulfillment.  # noqa: E501
        :type: str
        """

        self._discount_type = discount_type

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
        if not isinstance(other, RequestBodyPropertiesFulfillment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequestBodyPropertiesFulfillment):
            return True

        return self.to_dict() != other.to_dict()
