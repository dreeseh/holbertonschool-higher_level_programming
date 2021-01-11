#!/usr/bin/python3
"""
takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""
import requests
from sys import argv


r = requests.get('https://api.github.com/repos/{}/{}/commits'
                 .format(argv[2], argv[1]))
commits = r.json()
for j in commits[:10]:
    print(j.get('sha'), end=': ')
    print(j.get('commit').get('author').get('name'))
