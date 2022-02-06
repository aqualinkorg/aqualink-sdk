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
from swagger_client.api.sites_api import SitesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSitesApi(unittest.TestCase):
    """SitesApi unit test stubs"""

    def setUp(self):
        self.api = SitesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sites_controller_add_exclusion_dates(self):
        """Test case for sites_controller_add_exclusion_dates

        Adds exclusion dates to spotter's data  # noqa: E501
        """
        pass

    def test_sites_controller_create(self):
        """Test case for sites_controller_create

        Creates a new site and its site application  # noqa: E501
        """
        pass

    def test_sites_controller_delete(self):
        """Test case for sites_controller_delete

        Deletes specified site  # noqa: E501
        """
        pass

    def test_sites_controller_deploy_spotter(self):
        """Test case for sites_controller_deploy_spotter

        Deploys site's spotter  # noqa: E501
        """
        pass

    def test_sites_controller_find(self):
        """Test case for sites_controller_find

        Returns sites filtered by provided filters  # noqa: E501
        """
        pass

    def test_sites_controller_find_daily_data(self):
        """Test case for sites_controller_find_daily_data

        Returns daily data of the specified site  # noqa: E501
        """
        pass

    def test_sites_controller_find_exclusion_dates(self):
        """Test case for sites_controller_find_exclusion_dates

        Returns exclusion dates of specified site's spotter  # noqa: E501
        """
        pass

    def test_sites_controller_find_live_data(self):
        """Test case for sites_controller_find_live_data

        Returns live data of the specified site  # noqa: E501
        """
        pass

    def test_sites_controller_find_one(self):
        """Test case for sites_controller_find_one

        Returns specified site  # noqa: E501
        """
        pass

    def test_sites_controller_get_spotter_data(self):
        """Test case for sites_controller_get_spotter_data

        Returns spotter data of the specified site  # noqa: E501
        """
        pass

    def test_sites_controller_update(self):
        """Test case for sites_controller_update

        Updates specified site  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
