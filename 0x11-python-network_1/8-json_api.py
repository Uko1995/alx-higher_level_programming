#!/usr/bin/env python3
'''
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
'''

import requests
from sys import argv

if __name__ == "__main_-":
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    response = requests.post(url, data)
    response_json = response.json()
    try:
        if not response_json:
            print("No result")
        else:
            print(f"[{response_json.get('id')}] {response_json.get('name')}")

    except requests.exception:
        print("Not a valid JSON")
