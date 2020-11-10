#!/usr/bin/env python3

"""
Course: ECE 4574
Team: fCsGsU - SafeWaze
Author: Fonte Clanton
Date: November 4, 2020

Modified: November 10, 2020
Add documentation

This package contains the DBHelper class which provides methods for accessing
the MongoDB database.
"""

from datetime import datetime
from pymongo import MongoClient
import package.util.covidstats as covidstats


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

    def add_user(self, username, email, password):
        """
        Attempts to add a new user to the database.
        *** Password is currently stored in PLAINTEXT ***

        :param username: New user's username
        :param email: New user's email address
        :param password: New user's password
        :return: True if adding user was successful, otherwise false
        """
        email_in_db = self._users_collection.find(
            {
                'email': email
            }
        )

        email_in_db = bool(email_in_db.count())

        if not email_in_db:
            # FIXME: PASSWORD IS IN PLAINTEXT
            self._users_collection.insert(
                {
                    'username': username,
                    'email': email,
                    'password': password
                }
            )

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
        users = self._users_collection.find()

        valid_credentials = False
        for user in users:
            if user['email'] == email and user['password'] == password:
                valid_credentials = True
                break

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

    def get_results_collection(self):
        """
        Return the entire results_history collection.

        :return: Documents from the results_history collection
        """
        results = self._results_collection.find()

        return results

    def update_database(self):
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
    db.update_database()
    print('First 5 entries in results:')
    first_five = db.get_results_collection().limit(5)

    for x in first_five:
        print(x)
