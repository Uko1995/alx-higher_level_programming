#!/usr/bin/python3
'''
Python script that fetches https://alx-intranet.hbtn.io/status
'''

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as site:
        fetched = site.read()
        url = fetched.decode("utf-8")
        try:
            print(fetched)
        except urllib.error.URLError as e:
            print(f"Status code: {e.code}")
