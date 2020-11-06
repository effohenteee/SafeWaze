#!/usr/bin/env python3

from pymongo import MongoClient
import package.util.covidstats as covidstats


class DBHelper:
    def __init__(self, address=None):
        self._client = MongoClient(address)
        self._safewaze_db = self._client['safewaze']
        self._results_collection = self._safewaze_db['results_history']
        self._users_collection = self._safewaze_db['users']

    def add_user(self, username, email, password):
        email_in_db = self._users_collection.find(
            {
                'email': email
            }
        )

        email_in_db = email_in_db.count()

        if not email_in_db:
            self._users_collection.insert(
                {
                    'username': username,
                    'email': email,
                    'password': password
                }
            )

        return not bool(email_in_db)

    def clear_database(self):
        self._results_collection.remove()

        return

    def get_results_database(self):
        results = self._results_collection.find()

        return results

    def update_database(self):
        results_df = covidstats.get_blacksburg_data()
        # Use rows as entries to the dictionary
        results_dict = results_df.to_dict(orient='records')

        self.clear_database()
        self._results_collection.insert(results_dict)

        return


if __name__ == '__main__':
    db = DBHelper()
    print('First 5 entries in results:')
    first_five = db.get_results_database().limit(5)

    for x in first_five:
        print(x)
