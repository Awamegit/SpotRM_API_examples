#!/usr/bin/env python

#
# SpotRM API test
# An examnple on how to access the API using a token as credential.
#
# BSD 3-Clause License
# Copyright (c) 2020, Awametox AB
# You should have received a copy of the BSD 3-Clause License
# along with this script; if not, see <https://github.com/Awamegit/SpotRM_API_examples/blob/master/LICENSE>
#
import requests
import json
from requests.auth import HTTPBasicAuth
import os

#
#  Start by defining the server, the access credentials and a few convenience shortcuts.
#
BASEURL = "https://www.spotrm.com/api/v1"
# Read the your SpotRM username / password from the environment:
authData = HTTPBasicAuth(os.environ["TEST_USERNAME"], os.environ["TEST_PASSWORD"])
# Could also encode it in clear text in the script but take care shareing it or
# using version control:
# authData = HTTPBasicAuth('my_email@somewhere.com', 'my_super_secure_PassW0rd!')
headers = {"content-type": "application/json"}


#
# Example of getting and using an authorisation access token rather than sending
# one's credentials withevery request.
#

#
# Function to retrieve token
#
def getToken():
    url = BASEURL + "/tokens/"
    response = requests.post(url, auth=authData)
    if response.status_code == 200:
        return (json.loads(response.text)["token"], "")
    else:
        print("There was an error: " + json.loads(response.text)["message"])


#
# Use token to query database to find alerts for a smiles string:
#
def getAlerts(smiles, token):
    url = BASEURL + "/search/smarts/smiles"
    response = requests.post(url, data=json.dumps(smiles), headers=headers, auth=token)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print("There was an error: " + json.loads(response.text)["message"])


#
# Use the token again to find drugs associated with an alert ID:
#
def getDrug(alertID, token):
    url = BASEURL + "/get/drug/smarts_id/" + alertID
    response = requests.get(url, auth=token)
    if response.status_code == 200:
        respDict = json.loads(response.text)
        return respDict
    else:
        print("There was an error: " + json.loads(response.text)["message"])


def main():
    token = getToken()
    alerts = getAlerts("c1ccccc1N(C)C", token)
    print("\nThe following alert was found for your structure:")
    for item in alerts:
        print("Alert ID: " + item[0] + ' is "' + item[1] + '"')
    drugs = getDrug(alerts[0][0], token)
    print("\nThe following drugs are associated with this alert:")
    for key in drugs:
        print(drugs[key]["DrugName"])


if __name__ == "__main__":

    main()
