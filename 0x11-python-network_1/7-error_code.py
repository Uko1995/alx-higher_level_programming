#!/usr/bin/python3
'''
Python script that fetches https://alx-intranet.hbtn.io/status
'''

import requests
from sys import argv

if __name__ == "__main__":
    try:
        fetched = requests.get(argv[1])
        print(fetched)
    except urllib.error.HTTPError as e:
        if e.code >= 400:
            print(f"Error code: {e.code}")
