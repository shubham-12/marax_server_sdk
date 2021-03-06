# coding: utf-8

"""
    marax-server-sdk

    Marax Server SDK to send transactional events from client server to marax server  # noqa: E501

    The version of the OpenAPI document: 0.2.0
    Contact: team@marax.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import marax_server_sdk
from marax_server_sdk.models.request_body_properties_fulfillment import RequestBodyPropertiesFulfillment  # noqa: E501
from marax_server_sdk.rest import ApiException

class TestRequestBodyPropertiesFulfillment(unittest.TestCase):
    """RequestBodyPropertiesFulfillment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RequestBodyPropertiesFulfillment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = marax_server_sdk.models.request_body_properties_fulfillment.RequestBodyPropertiesFulfillment()  # noqa: E501
        if include_optional :
            return RequestBodyPropertiesFulfillment(
                type = 'surcharge', 
                price = 10.5, 
                price_units = 'rupees', 
                discount = 0, 
                discount_type = 'monetory'
            )
        else :
            return RequestBodyPropertiesFulfillment(
        )

    def testRequestBodyPropertiesFulfillment(self):
        """Test RequestBodyPropertiesFulfillment"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
