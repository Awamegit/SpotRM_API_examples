#!/usr/bin/env python
# coding: utf-8

"""
SpotRM API test
Some *examples* on how to access the API.

BSD 3-Clause License
Copyright (c) 2020, Awametox AB
You should have received a copy of the BSD 3-Clause License
along with this script; if not, see <https://github.com/Awamegit/SpotRM_API_examples/blob/master/LICENSE>
"""

import json
import os

import requests
from requests.auth import HTTPBasicAuth

#
#  Start by defining the server, the access credentials and a few convenience shortcuts.
#
BASEURL = "https://www.spotrm.com/api/v1"

# Read the your SpotRM username / password from the environment, preferably via .env file using python dotenv.
authData = HTTPBasicAuth(os.environ["TEST_USERNAME"], os.environ["TEST_PASSWORD"])
# Could also encode it in clear text in the script but take care shareing it or
# using version control:
# authData = HTTPBasicAuth('my_email@somewhere.com', 'my_super_secure_PassW0rd!')

headers = {"content-type": "application/json"}


#
# Here a simple example (using a function) to retrieve help information:
#
def main():
    url = BASEURL + "/help"
    response = requests.get(url, auth=authData)
    print(response.status_code)  # 200 = ok; 40x or 50x different forms of http errors
    respDict = json.loads(response.text)
    for key in respDict:
        print(key + ": " + respDict[key])

    #
    # -----------------------------------------------------
    # Here an example of checking for a drug ID (ID = SpotRM database specific):
    #
    lookup_an_ID = requests.get(BASEURL + "/get/drug/id/1", auth=authData)
    # print(lookup_an_ID)  #optional
    respDict = json.loads(lookup_an_ID.text)

    print("\n---- JSON output unformatted -----")
    print(respDict)

    print("\n---- JSON output formatted 1 -----")
    print(json.dumps(respDict, indent=2))

    print("\n---- JSON output formatted 2 -----")
    for key, value in respDict.items():
        print(key, " = ", value)
    #
    # -----------------------------------------------------
    # Here an example of searching for a smiles (using POST):
    #
    url = BASEURL + "/search/drug/substructure/smiles"
    smiles = "C1CN(CCN1CC2=CC3=C(C=C2)OCO3)C(=O)COC4=CC=C(C=C4)Cl"
    response = requests.post(
        url, data=json.dumps(smiles), headers=headers, auth=authData
    )
    # print(response.status_code)  # optional
    respDict = json.loads(response.text)
    print("\nJSON formatted results from SMILES search")
    print(json.dumps(respDict, indent=2))  # JSON formatted


if __name__ == "__main__":
    main()
