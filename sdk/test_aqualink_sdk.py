"""Simple Test for the Aqualink Python SDK"""
# pip install -i https://test.pypi.org/simple/ aqualink-api
import time
import aqualink_sdk
from aqualink_sdk.api import sites_api, time_series_api
from aqualink_sdk.model.exclude_spotter_dates_dto import ExcludeSpotterDatesDto
from aqualink_sdk.model.inline_response404 import InlineResponse404
from aqualink_sdk.model.inline_response400 import InlineResponse400
from pprint import pprint


def test_sdk():
    with aqualink_sdk.ApiClient() as api_client:
        # List all sites
        site_api = sites_api.SitesApi(api_client)
        site_data = site_api.sites_controller_find()
        pprint(site_data)

        # Get available date ranges
        ts_api = time_series_api.TimeSeriesApi()
        range_data = ts_api.time_series_controller_find_site_data_range(
            site_id=1006,
        )
        # print(range_data)

        # Get time series data
        # data = time_series_api.time_series_controller_find_site_data(
        #     site_id=1006,
        #     metrics=["bottom_temperature"],
        #     start="2021-01-02",
        #     end="2022-01-01",
        #     hourly=False
        # )
        # print(data)

        # Get aggregated time series data
        data = ts_api.time_series_controller_find_aggregate_site_data(
            site_id=1006,
            metrics=["bottom_temperature"],
            start="2021-01-01",
            end="2022-01-10",
            aggregate_frequency="10min",
            aggregate_mapping={"bottom_temperature": "max"}
        )
        pprint(data)

if __name__ == '__main__':
    test_sdk()
