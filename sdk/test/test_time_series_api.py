"""
    Aqualink API documentation

    The Aqualink public API documentation  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import aqualink_sdk
from aqualink_sdk.api.time_series_api import TimeSeriesApi  # noqa: E501


class TestTimeSeriesApi(unittest.TestCase):
    """TimeSeriesApi unit test stubs"""

    def setUp(self):
        self.api = TimeSeriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_time_series_controller_find_site_data(self):
        """Test case for time_series_controller_find_site_data

        Returns specified time series data for a specified site  # noqa: E501
        """
        pass

    def test_time_series_controller_find_site_data_range(self):
        """Test case for time_series_controller_find_site_data_range

        Returns the range of the available time series data for a specified site  # noqa: E501
        """
        pass

    def test_time_series_controller_find_survey_point_data(self):
        """Test case for time_series_controller_find_survey_point_data

        Returns specified time series data for a specified site point of interest  # noqa: E501
        """
        pass

    def test_time_series_controller_find_survey_point_data_range(self):
        """Test case for time_series_controller_find_survey_point_data_range

        Returns the range of the available time series data for a specified site point of interest  # noqa: E501
        """
        pass

    def test_time_series_controller_upload_time_series_data(self):
        """Test case for time_series_controller_upload_time_series_data

        Upload time series data  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
