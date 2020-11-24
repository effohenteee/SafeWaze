#!/usr/bin/env python3

"""
Course: ECE 4574
Team: fCsGsU - SafeWaze
Author: Fonte Clanton
Date: November 23, 2020

Generates a master-key file used for encryption/decryption of the MongoDB database.
"""

import os
import pathlib
path = str(pathlib.Path().absolute()) + "/master-key.txt"
file_bytes = os.urandom(96)
with open(path, "wb") as f:
    f.write(file_bytes)
