"""
    Aqualink API documentation

    The Aqualink public API documentation  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import aqualink_sdk
from aqualink_sdk.api.surveys_api import SurveysApi  # noqa: E501


class TestSurveysApi(unittest.TestCase):
    """SurveysApi unit test stubs"""

    def setUp(self):
        self.api = SurveysApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_surveys_controller_create(self):
        """Test case for surveys_controller_create

        Creates a new survey  # noqa: E501
        """
        pass

    def test_surveys_controller_create_media(self):
        """Test case for surveys_controller_create_media

        Creates a new survey media  # noqa: E501
        """
        pass

    def test_surveys_controller_delete(self):
        """Test case for surveys_controller_delete

        Deletes a specified survey  # noqa: E501
        """
        pass

    def test_surveys_controller_delete_media(self):
        """Test case for surveys_controller_delete_media

        Deletes a specified survey media  # noqa: E501
        """
        pass

    def test_surveys_controller_find(self):
        """Test case for surveys_controller_find

        Returns all site's survey  # noqa: E501
        """
        pass

    def test_surveys_controller_find_media(self):
        """Test case for surveys_controller_find_media

        Returns all media of a specified survey  # noqa: E501
        """
        pass

    def test_surveys_controller_find_one(self):
        """Test case for surveys_controller_find_one

        Returns specified survey  # noqa: E501
        """
        pass

    def test_surveys_controller_update(self):
        """Test case for surveys_controller_update

        Updates a specified survey  # noqa: E501
        """
        pass

    def test_surveys_controller_update_media(self):
        """Test case for surveys_controller_update_media

        Updates a specified survey media  # noqa: E501
        """
        pass

    def test_surveys_controller_upload(self):
        """Test case for surveys_controller_upload

        Uploads a new survey media  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
