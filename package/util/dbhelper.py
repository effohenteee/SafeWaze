#!/usr/bin/env python3

"""
Course: ECE 4574
Team: fCsGsU - SafeWaze
Author: Fonte Clanton
Date: November 4, 2020

Modified: November 10, 2020
Add documentation
Modified: November 23, 2020
Add methods and refactor for use with encryption

This package contains the DBHelper class which provides methods for accessing
the MongoDB database.
"""

from datetime import datetime
from pymongo import MongoClient
import os

from package.util.encrypt.helpers import CsfleHelper
import package.util.covidstats as covidstats


def read_master_key(path="./encrypt/master-key.txt"):
    pwd = os.path.abspath(os.path.curdir)
    last = pwd.split('/')[-1]
    if last == 'SafeWaze':
        path = pwd + '/package/util' + path[1:]

    with open(path, "rb") as f:
        return f.read(96)


class DBHelper:
    def __init__(self, address=None):
        """
        Initializes a MongoClient with references to the safewaze database,
        the results_history collection, and the users collection.

        :param address: Optional IP address of the database. If None, will use
        127.0.0.1 by default.
        """
        self._client = MongoClient(address)
        self._safewaze_db = self._client['safewaze']
        self._results_collection = self._safewaze_db['results_history']
        self._users_collection = self._safewaze_db['users']

    def add_user(self, document):
        """
        Attempts to add a new user to the database.

        :param document: User account details in the appropriate schema
        :return: True if adding user was successful, otherwise false
        """

        # perform a read using the csfle enabled client. We expect all fields to
        # be readable.
        # querying on an encrypted field using strict equality
        encrypted_client = self.get_encrypted_client()
        email_in_db = encrypted_client.safewaze.users.find_one({"email": document["email"]})

        email_in_db = bool(email_in_db)

        if not email_in_db:
            encrypted_client.safewaze.users.insert(document)
        encrypted_client.close()

        # Successful if account was not already in the database
        success = not email_in_db

        return success

    def authenticate_user(self, email, password):
        """
        Attemps to authenticate the user base on an email/password
        combination. The password is in plaintext as is the password in the
        database.

        :param email: Email address used to authenticate
        :param password: Password used to authenticate
        :return: True if authentication is affirmed, otherwise false
        """
        encrypted_client = self.get_encrypted_client()
        user = encrypted_client.safewaze.users.find_one({"email": email})

        valid_credentials = False
        if user and user['password'] == password:
            valid_credentials = True

        return valid_credentials

    def clear_collection(self, collection='results_history'):
        """
        Delete all documents from a collection. Default clears results_history.

        :param collection: Name of the collection to clear
        :return: None
        """
        if collection == 'users':
            self._users_collection.remove()
        else:
            self._results_collection.remove()

        return

    @staticmethod
    def get_encrypted_client():
        # For local master key
        master_key = read_master_key()
        kms_provider_name = "local"
        kms_provider = {
            "local": {
                "key": master_key,
            },
        }

        key_db = "encryption"
        key_coll = "__keyVault"

        data_db = "safewaze"
        data_coll = "users"

        csfle_helper = CsfleHelper(kms_provider_name=kms_provider_name,
                                   kms_provider=kms_provider, master_key=master_key, key_db=key_db, key_coll=key_coll)

        # Insert your key generated by make_data_key.py here.
        # Or comment this out if you already have a data key for your provider stored.
        data_key = CsfleHelper.key_from_base64("1xNaOKmHThiniJ1Q/EW9/w==")

        # if you already have a data key or are using a remote KMS, uncomment the line below
        # data_key = csfle_helper.find_or_create_data_key()

        # set a JSON schema for automatic encryption
        schema = CsfleHelper.create_json_schema(data_key=data_key, dbName=data_db, collName=data_coll)

        return csfle_helper.get_csfle_enabled_client(schema)

    def get_results_collection(self):
        """
        Return the entire results_history collection.

        :return: Documents from the results_history collection
        """
        results = self._results_collection.find()

        return results

    def update_covid_numbers(self):
        """
        Updates the results_history collection with the latest data from
        Socrata.

        :return: True if the database was updated, otherwise false
        """
        results_df = covidstats.get_blacksburg_data()
        # Use rows as entries to the dictionary
        results_dict = results_df.to_dict(orient='records')

        updated = False
        most_recent_report_date = results_dict[0]['report_date']
        if most_recent_report_date < datetime.today():
            self.clear_collection()
            self._results_collection.insert(results_dict)
            updated = True

        return updated


if __name__ == '__main__':
    db = DBHelper()

    # TODO: Figure out fields
    example_document = {
        "name": "Jon Doe",
        "email": "jondoe@email.com",
        "address": {
            "street": "123 Main St.",
            "city": "Richmond",
            "state": "Virginia",
            "zip_code": 23224
        },
        "dob": {
            "month": 1,
            "day": 31,
            "year": 1996
        },
        "height": 68,
        "weight": 165,
        "healthy": True,
        "password": "password"
    }

    result = db.add_user(example_document)

    if result:
        print(f'User: {example_document["name"]} added to the database.')
    else:
        print(f'User {example_document["name"]} could not be added or is already in the database.')

    if db.authenticate_user('jondoe@email.com', 'password'):
        print('User authenticated successfully.')
    else:
        print('User authenticated unsuccessfully.')
