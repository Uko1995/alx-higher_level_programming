#!/usr/bin/python3
'''
Python script that fetches https://alx-intranet.hbtn.io/status
'''

import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    if response.status_code > 399:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
