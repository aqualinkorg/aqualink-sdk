# coding: utf-8

"""
    Aqualink API documentation

    The Aqualink public API documentation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.regions_api import RegionsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRegionsApi(unittest.TestCase):
    """RegionsApi unit test stubs"""

    def setUp(self):
        self.api = RegionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_regions_controller_create(self):
        """Test case for regions_controller_create

        Creates new region  # noqa: E501
        """
        pass

    def test_regions_controller_delete(self):
        """Test case for regions_controller_delete

        Deletes specified region  # noqa: E501
        """
        pass

    def test_regions_controller_find(self):
        """Test case for regions_controller_find

        Returns regions filtered by provided filters  # noqa: E501
        """
        pass

    def test_regions_controller_find_one(self):
        """Test case for regions_controller_find_one

        Returns specified region  # noqa: E501
        """
        pass

    def test_regions_controller_update(self):
        """Test case for regions_controller_update

        Updates specified region  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
