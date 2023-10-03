#!/usr/bin/env python3
'''
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
'''

import requests
from sys import argv

if __name__ == "__main_-":
    if len(argv) != 2:
        q = ""
    else:
        q = argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    response = requests.post(url, data)
    response_json = response.json()
    if len(response_json) == 0:
        print("No result")
    elif not response_json:
        print("Not a valid JSON")
    else:
        print(f"[{response_json['id']}] {response_json['name']}")
