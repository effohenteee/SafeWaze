# SafeWaze - fCSGsU

## MongoDB Setup Instructions for Encryption
1. Install `pymongocrypt` and `libmongocrypt`: [link](https://pypi.org/project/pymongocrypt/)
2. Install `mongodb-enterprise`: [link](https://docs.mongodb.com/manual/tutorial/install-mongodb-enterprise-on-ubuntu/#install-mongodb-enterprise-edition-on-ubuntu)
    ### Troubleshooting (Linux/Unix)
    * If you are unable to start the `mongod` service, try:
        1. Delete `/var/lib/mongodb` and/or
        2. Run `sudo chown -R mongodb:mongodb /var/lib/mongodb`
