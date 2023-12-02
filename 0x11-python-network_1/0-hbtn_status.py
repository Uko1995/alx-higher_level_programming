#!/usr/bin/python3
'''
Python script that fetches https://alx-intranet.hbtn.io/status
'''

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as site:
        fetched = site.read()
        url = fetched.decode("utf-8")
        print("Body response:")
        print(f"\t- type: {type(fetched)}")
        print(f"\t- content: {fetched}")
        print(f"\t- utf8 content: {url}")
