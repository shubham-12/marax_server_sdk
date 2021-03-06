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
from marax_server_sdk.models.response200 import Response200  # noqa: E501
from marax_server_sdk.rest import ApiException

class TestResponse200(unittest.TestCase):
    """Response200 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Response200
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = marax_server_sdk.models.response200.Response200()  # noqa: E501
        if include_optional :
            return Response200(
                status = 'processed', 
                message = 'Success'
            )
        else :
            return Response200(
        )

    def testResponse200(self):
        """Test Response200"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
