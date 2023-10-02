#!/usr/bin/python3
'''
Python script that fetches https://alx-intranet.hbtn.io/status
'''

import urllib.request
from sys import argv

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as site:
            fetched = site.read().decode("utf-8")
            print(fetched)
    except urllib.error.URLError as e:
        print(f"Status code: {e.code}")
