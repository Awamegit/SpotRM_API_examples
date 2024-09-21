#!/usr/bin/env python
"""
SpotRM API test
An example on how to use the API to retrieve an image after a structure query.

BSD 3-Clause License
Copyright (c) 2020, Awametox AB
You should have received a copy of the BSD 3-Clause License
along with this script; if not, see <https://github.com/Awamegit/SpotRM_API_examples/blob/master/LICENSE>
"""

import datetime
import json
import os

import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

#
#  Start by defining the server, the access credentials and a few convenience shortcuts.
#
BASEURL = "https://www.spotrm.com/api/v1"
load_dotenv()
authData = HTTPBasicAuth(os.environ["USER"], os.environ["PASSWORD"])
headers = {"content-type": "application/json"}


def get_image(smiles: str, smarts_id: int):
    """
    Function to retrieve an image highlighting the region in a query structure
    provided as a smiles string which triggers a particular reactive metabolite
    alert specified by its smarts id.

    Relevant smarts_id would be identified by an earlier search using the
    /api/v1/search/smarts/smiles route.

    Outputs an SVG image file smilesImage_<date>.svg
    """

    url = BASEURL + "/get/image/smiles"
    query = {"smiles": smiles, "smarts_id": smarts_id}
    fileOutput = "smilesImage_" + str(datetime.datetime.now().date()) + ".svg"
    # change path as needed

    response = requests.post(
        url, data=json.dumps(query), headers=headers, auth=authData
    )
    if response.status_code == 200:
        with open(fileOutput, "wb") as f:
            f.write(response.content)
        # display(SVG(filename=fileOutput)) only works in Jupyter notebooks
        print(f"SVG image saved as {fileOutput}")
    else:
        print("There was an error: " + json.loads(response.text)["message"])


def main():
    get_image("c1ccc(C)c(C)c1N", 1)


if __name__ == "__main__":
    main()
