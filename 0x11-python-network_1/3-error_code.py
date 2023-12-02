#!/usr/bin/python3
'''
Python script that fetches https://alx-intranet.hbtn.io/status
'''

import urllib.request
from sys import argv
import urllib.error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as site:
            fetched = site.read().decode("utf-8")
            print(fetched)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
