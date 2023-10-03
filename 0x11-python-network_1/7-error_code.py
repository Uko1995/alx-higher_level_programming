#!/usr/bin/python3
'''
Python script that fetches https://alx-intranet.hbtn.io/status
'''

import requests
from sys import argv

if __name__ == "__main__":
    try:
        response = requests.get(argv[1])
        print(response.text)
    except response.status_code as e:
        if e > 399:
            print(f"Error code: {e}")
