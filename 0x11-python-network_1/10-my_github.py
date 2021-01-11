#!/usr/bin/python3
"""
takes your Github credentials (username and password)
and uses the Github API to display your id
"""
from requests import get, auth
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    r = get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(r.json().get('id'))
