#!/usr/bin/python3
"""
takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""
from requests import get, auth
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits?per_page=10".format(
        owner, repo)
    r = get(url)
    for elem in r.json():
        arr_author = (elem.get('commit')).get('author')
        print("{}: {}".format(elem.get('sha'), arr_author.get('name')))
