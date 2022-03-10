import pandas as pd


default_mapping = {
    'min_temperature':'min',
    'precipitation':'sum',
    'alert_level':'max',
    'bottom_temperature':'mean'
}

# TODO - Build on top of TimeSeriesApi ?

def aggregate_data(timeseries_data, aggregate_frequency, aggregate_mapping=default_mapping):
    dataframe = pd.DataFrame.from_dict(timeseries_data)

    # TODO - verify that all the metrics requested in "metrics" have a mapping
    # TODO - strongly type the frequency or regex
    # TODO - Hourly and aggregate are incompatible

    return dataframe.groupby(pd.Grouper(freq=aggregate_frequency)).agg(aggregate_mapping)
