import os
import pathlib
path = str(pathlib.Path().absolute()) + "/master-key.txt"
file_bytes = os.urandom(96)
with open(path, "wb") as f:
    f.write(file_bytes)
