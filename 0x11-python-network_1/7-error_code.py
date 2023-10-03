#!/usr/bin/python3
'''
Python script that fetches https://alx-intranet.hbtn.io/status
'''

import requests
from sys import argv

if __name__ == "__main__":
    fetched = requests.get(argv[1])
    error_code = fetched.status_code
    if error.code >= 400:
            print(f"Error code: {e.code}")
