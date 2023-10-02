#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found
in the header of the response
'''

import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    email = argv[2]
    val = {"email": email}
    data = urllib.parse.urlencode(val).encode("ascii")
    name = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(name) as site:
        response = site.read().decode("utf-8")
        print(response)
