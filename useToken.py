#!/usr/bin/env python
# coding: utf-8
"""
SpotRM API with Python: token usage

BSD 3-Clause License<br>
Copyright (c) 2020, Awametox AB<br>
You should have received a copy of the BSD 3-Clause License
along with this script; <br>
if not, see <https://github.com/Awamegit/SpotRM_API_examples/blob/master/LICENSE>

Added usage of dotenv as a more secure and convenient to define username, password, etc.
"""

import json
import os

import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

#
#  Start by defining the server, the access credentials and a few convenience shortcuts.
#
load_dotenv()
BASEURL = "https://www.spotrm.com/api/v1"
# Read the your SpotRM username / password from the environment:
authData = HTTPBasicAuth(os.environ["USER"], os.environ["PASSWORD"])
"""
 One could for quicktesting also use this syntax:
 authData = HTTPBasicAuth('my_email@somewhere.com', 'my_super_secure_PassW0rd!')
 but it has the disadvantage of leaking the credentials in the code.
 """
headers = {"content-type": "application/json"}


# Example of getting and using an authorisation access token rather than sending
# one's credentials with every request.
#
# Here using a smiles string based search


def get_api_token() -> tuple[str, str] | None:
    """Function to retrieve api authentication token
    :return: The token to use for authentication; second element required, but not used.
    """
    url = f"{BASEURL}/tokens/"
    response = requests.post(url, auth=authData)
    if response.status_code == 200:
        return response.json().get("token", ""), ""
    else:
        error_message = response.json().get("message", "Unknown error")
        print(f"There was an error: {error_message}")
        return None


def get_alerts(smiles: list, token: str) -> dict | None:
    """Use token to query database to find alerts for a smiles string

    :param smiles: The SMILES string for which to find alerts
    :param token: The token to use for authentication
    :return: alert ID and the alert description
    """

    url = f"{BASEURL}/search/smarts/smiles"
    response = requests.post(url, data=json.dumps(smiles), headers=headers, auth=token)
    if response.status_code == 200:
        return response.json()
    else:
        error_message = response.json().get("message", "Unknown error")
        print(f"There was an error: {error_message}")
        return None


def get_drug(alertID: list, token: tuple) -> dict | None:
    """Use the obained token to find drugs associated with an alert ID:
    :param alertID: The alert ID for which to find drugs
    :param token: The token to use for authentication
    :return: A dictionary with the drugs associated with the alert ID
    """
    url = f"{BASEURL}/get/drug/smarts_id/{alertID}"
    response = requests.get(url, auth=token)
    if response.status_code == 200:
        return response.json()
    else:
        error_message = response.json().get("message", "Unknown error")
        print(f"There was an error in get_drug function: {error_message}")
        return None


def main():
    token = get_api_token()
    if token:
        alerts = get_alerts("c1ccccc1N(C)C", token)

        print("\nThe following alert was found for your structure:")
        for item in alerts:
            print("Alert ID: " + item[0] + ' is "' + item[1] + '"')
        drugs = get_drug(alerts[0][0], token)
        print("\nThe following drugs are associated with this alert:")
        for key in drugs:
            print(drugs[key]["DrugName"])
    else:
        print("Failed to retrieve token.")


if __name__ == "__main__":
    main()
