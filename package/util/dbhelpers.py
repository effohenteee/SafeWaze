#!/usr/bin/env python3

from pymongo import MongoClient
import package.util.covidstats as covidstats


def add_user(username, email, password):
    # TODO: Implement functionality
    pass

    return


def clear_database():
    client = MongoClient()
    mydb = client['safewaze']
    mycol = mydb['results_history']
    mycol.remove()

    return


def get_results_database():
    client = MongoClient()
    mydb = client['safewaze']
    mycol = mydb['results_history']
    results = mycol.find()

    return results


def update_database():
    results_df = covidstats.get_blacksburg_data()
    # Use rows as entries to the dictionary
    results_dict = results_df.to_dict(orient='records')

    client = MongoClient()
    mydb = client['safewaze']
    mycol = mydb['results_history']

    clear_database()
    mycol.insert(results_dict)

    return
