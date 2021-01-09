#!/usr/bin/env python

#
# SpotRM API test
# An example on how to use the API to retrieve an image after a structure query.
# 
# BSD 3-Clause License
# Copyright (c) 2020/2021, Awametox AB
# You should have received a copy of the BSD 3-Clause License
# along with this script; if not, see <https://github.com/Awamegit/SpotRM_API_examples/blob/master/LICENSE>
#

import requests
import json
from requests.auth import HTTPBasicAuth
import os
import datetime

#
#  Start by defining the server, the access credentials and a few convenience shortcuts.
#
BASEURL = "https://www.spotrm.com/api/v1"

# Read the your SpotRM username / password from the environment:
authData = HTTPBasicAuth(os.environ["TEST_USERNAME"], os.environ["TEST_PASSWORD"])
headers = {"content-type": "application/json"}

#
# Function to retrieve an image highlighting the region in a query structure
# provided as a smiles string which triggers a particular reactive metabolite
# alert specified by its smarts id.
#
# Relevant smarts_id would be identified by an earlier search using the
# /api/v1/search/smarts/smiles route.
#
# Outputs an SVG image file smilesImage_<date>.svg
#
def getImage(smiles, smarts_id):
    url = BASEURL + "/get/image/smiles"
    query = {"smiles": smiles, "smarts_id": smarts_id}
    filename = "smilesImage_" + str(datetime.datetime.now().date()) + ".svg"
    print('Submitting query')
    response = requests.post(
        url, data=json.dumps(query), headers=headers, auth=authData
    )
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print("Analysis of input smiles ",smiles, "\n is stored as: ", filename)
    else:
        print("There was an error: " + json.loads(response.text)["message"])


if __name__ == "__main__":

    getImage("c1ccc(C)c(C)c1N", 1)
    
