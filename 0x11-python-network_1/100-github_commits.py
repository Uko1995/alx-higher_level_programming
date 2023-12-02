#!/usr/bin/python3
''' script takes 2 arguments and lists the last 10 commits in a repository '''

import requests
from sys import argv

if __name__ == "__main__":
    repo_name = argv[1]
    owner = argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo_name}/commits"
    response = requests.get(url)
    objects = response.json()
    for i, obj in enumerate(objects):
        print("{}: {}".format(obj.get('sha'),
                              obj.get('commit').get('author').get('name')))
        if i == 9:
            break
