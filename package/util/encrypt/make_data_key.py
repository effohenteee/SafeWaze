#!/usr/bin/env python3

#
# Copyright 2019-present MongoDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""This file finds and prints or makes and prints a data key used for
encrpytion."""

"""
Course: ECE 4574
Team: fCsGsU - SafeWaze
Author: Fonte Clanton
Date: November 23, 2020

Data key generation. 
Obtained from: https://github.com/mongodb-university/csfle-guides/tree/master/python 
"""

import base64
from uuid import UUID
from helpers import read_master_key, CsfleHelper

def main():

    local_master_key = read_master_key()

    kms_provider = {
        "local": {
            "key": local_master_key,
        },
    }

    csfle_helper = CsfleHelper(kms_provider=kms_provider)
    binary_data_key = csfle_helper.find_or_create_data_key()
    data_key = base64.b64encode(binary_data_key).decode("utf-8")

    print("Base64 data key. Copy and paste this into app.py\t", data_key)


if __name__ == "__main__":
    main()
