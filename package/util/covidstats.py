#!/usr/bin/env python

import pandas as pd
from sodapy import Socrata


def convert_datetime_column(data_frame):
    df = pd.DataFrame(data_frame, columns=['report_date'])
    df = pd.to_datetime(df['report_date'], format='%Y-%m-%dT%H:%M:%S')
    data_frame['report_date'] = df

    return data_frame


# TODO: Error handling? Make a class for parsing?
def get_blacksburg_data(max_=2000):
    """
    Returns max_ number of results from the COVID dashboard for zip code 24060.

    Link to VDH Socrata API Documentation:
    https://dev.socrata.com/foundry/data.virginia.gov/8bkr-zfqv

    Pre-conditions: Internet connection

    :param max_: Maximum number of results
    :return: Pandas DataFrame containing the dataset
    """
    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token, and no username or password:
    client = Socrata('data.virginia.gov', None)

    # Example authenticated client(needed for non - public datasets):
    # client = Socrata(data.virginia.gov,
    #                  MyAppToken,
    #                  username="user@example.com",
    #                  password="AFakePassword")

    # https://data.virginia.gov/resource/8bkr-zfqv.json?$where=zip_code=%2724060%27&$order=report_date%20DESC
    results = client.get('8bkr-zfqv', 'json', where='zip_code=\'24060\'',
                         order='report_date DESC', limit=max_)

    # Convert to pandas DataFrame
    results = pd.DataFrame.from_records(results)
    # Convert report_date to pandas Timestamp class
    results = convert_datetime_column(results)
    return results


if __name__ == '__main__':
    data = get_blacksburg_data()
    print(data)
