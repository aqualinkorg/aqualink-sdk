"""Simple Test for the Aqualink Python SDK"""
# pip install -i https://test.pypi.org/simple/ aqualink-api
import aqualink_sdk

def test_sdk():
    # List all sites
    site_api = aqualink_sdk.SitesApi()
    site_data = site_api.sites_controller_find()
    # print(site_data)

    # Get available date ranges
    time_series_api = aqualink_sdk.TimeSeriesApi()
    range_data = time_series_api.time_series_controller_find_site_data_range(
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
    data = time_series_api.time_series_controller_find_aggregate_site_data(
        site_id=1006,
        metrics=["bottom_temperature"],
        start="2021-01-01",
        end="2022-01-10",
        aggregate_frequency="10min",
        aggregate_mapping={"bottom_temperature": "max"}
    )
    print(data)

if __name__ == '__main__':
    test_sdk()
