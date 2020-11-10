#!/usr/bin/env python
"""
Course: ECE 4574
Team: fCsGsU - SafeWaze
Author: Fonte Clanton
Date: October 14, 2020

Modified: November 10, 2020
Add documentation

This package contains helper functions for accessing the Socrata API. This API
is used to collect statistical data for the Blacksburg area using zipcode 24060.
"""

import pandas as pd
import sodapy


def convert_datetime_column(data_frame):
    """
    Converts the report_date column into Pandas datetime objects. Pandas
    datetime objects are compatible with the standard Python datetime object.

    :param data_frame: Pandas dataframe object(s).
    :return: Dataframe with converted report_date field.
    """
    df = pd.DataFrame(data_frame, columns=['report_date'])
    df = pd.to_datetime(df['report_date'], format='%Y-%m-%dT%H:%M:%S')
    data_frame['report_date'] = df

    return data_frame


def get_blacksburg_data(max_=2000):
    """
    Returns max_ number of results from the COVID dashboard for zip code 24060.

    Link to VDH Socrata API Documentation:
    https://dev.socrata.com/foundry/data.virginia.gov/8bkr-zfqv

    :param max_: Maximum number of results
    :return: Pandas DataFrame containing the dataset
    """
    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token, and no username or password:
    client = sodapy.Socrata('data.virginia.gov', None)

    # Example authenticated client(needed for non - public datasets):
    # client = Socrata(data.virginia.gov, MyAppToken,
    #                  username="user@example.com",
    #                  password="AFakePassword")

    # https://data.virginia.gov/resource/8bkr-zfqv.json?$where=zip_code=%2724060%27&$order=report_date%20DESC
    results = client.get('8bkr-zfqv', 'json', where='zip_code=\'24060\'',
                         order='report_date DESC', limit=max_)

    # Convert to pandas DataFrame
    results = pd.DataFrame.from_records(results)

    # Convert report_date to pandas Datetime object
    results = convert_datetime_column(results)
    return results


if __name__ == '__main__':
    data = get_blacksburg_data()
    print('First five results:')
    print(data.head(5))
