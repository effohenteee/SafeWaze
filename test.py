from mongoengine import *
from datetime import datetime
import os
import json

connect("mongo-dev-db")

# defining documents

class SW_user(Document):
    firstname = StringField(required=True)
    lastname = StringField(required=True)
    email = StringField(required=True, unique=True)
    city = StringField(required=True)
    age = IntField(required=True)
    zip_code = IntField(required=True)
    categories = ListField()
    log_info = BooleanField(default= False)
    registered_user = BooleanField(default=False)
    date_created = DateTimeField(default=datetime.utcnow)

    #class method below will return json object of SW_user
    def json(self):
        user_dict = {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "age": self.age,
            "city": self.city,
            "zip_code": self.zip_code,
            "log_info": self.log_info,
            "first_time": self.registered_user,
            "creation": self.date_created
        }
        return json.dumps(user_dict)
    #create some meta data about SW_user. Will help with querying
    meta = {
        "indexes": ["zip_code", "email"],
        "ordering": ["-date_created"]
    }

# Save document

user_0 = SW_user(
    firstname="Sree",
    lastname="Giridhar",
    email="sreeg23@vt.edu",
    city="Blacksburg",
    age=21,
    zip_code=24061,
).save()

#print("Done!")