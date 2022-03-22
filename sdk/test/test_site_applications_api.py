"""
    Aqualink API documentation

    The Aqualink public API documentation  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import aqualink_sdk
from aqualink_sdk.api.site_applications_api import SiteApplicationsApi  # noqa: E501


class TestSiteApplicationsApi(unittest.TestCase):
    """SiteApplicationsApi unit test stubs"""

    def setUp(self):
        self.api = SiteApplicationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_site_applications_controller_find_one_from_site(self):
        """Test case for site_applications_controller_find_one_from_site

        Returns site application of specified site  # noqa: E501
        """
        pass

    def test_site_applications_controller_update(self):
        """Test case for site_applications_controller_update

        Updates site application by providing its appId. Needs authentication.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
