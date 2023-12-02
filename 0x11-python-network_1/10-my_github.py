#!/usr/bin/python3
'''
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
'''

import requests
from sys import argv

if __name__ == "__main__":
    data = {"username": argv[1], "password": argv[2]}
    url = "https://api.github.com/auth"
    response = requests.get(url, data)
    ids = response.json().get('id')
    print(ids)
