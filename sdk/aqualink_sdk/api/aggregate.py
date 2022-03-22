import pandas as pd
from pprint import pprint

default_mapping = {
    'min_temperature':'min',
    'precipitation':'sum',
    'alert_level':'max',
    'bottom_temperature':'mean'
}

# TODO - Build on top of TimeSeriesApi ?

def aggregate_data(timeseries_data, aggregate_frequency, aggregate_mapping=default_mapping):
    # TODO - verify that all the metrics requested in "metrics" have a mapping
    # TODO - strongly type the frequency or regex
    # TODO - Hourly and aggregate are incompatible

    data = timeseries_data._data_store
    # Data is in the form:
    # {'bottom_temperature': {
    #     'spotter': {
    #         'data': [
    #             {'timestamp': '2022-01-08T00:04:00.000Z', 'value': 25.32},
    #             {'timestamp': '2022-01-08T00:14:00.000Z', 'value': 25.259999999999998},
    #             {'timestamp': '2022-01-08T00:24:00.000Z', 'value': 25.28}]}}
    # }

    new_data = {}
    for metric_name, metric_data in data.items():
        for sonde_type_name, sonde_data in metric_data.items():
            dataframe = pd.DataFrame(sonde_data['data'])
            dataframe['timestamp_index'] = pd.to_datetime(dataframe['timestamp']) # convert column to datetime object
            dataframe.set_index('timestamp_index', inplace=True)

            temp_aggregate_mapping = {"value": aggregate_mapping[metric_name]}

            aggregate_data = dataframe.groupby(pd.Grouper(freq=aggregate_frequency)).agg(temp_aggregate_mapping)

            # Convert timestamp back to string
            aggregate_data["timestamp"] = aggregate_data.index.map(
                lambda ts: ts.isoformat(timespec='milliseconds').replace('+00:00', 'Z')
            )

            aggregate_data.dropna()

            new_metric_data = {sonde_type_name: {"data": aggregate_data.to_dict('records')}}
            new_data[metric_name] = new_metric_data

    return new_data
