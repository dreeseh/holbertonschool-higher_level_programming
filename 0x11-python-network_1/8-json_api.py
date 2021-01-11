#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        dict_r = r.json()
        id = dict_r.get('id')
        name = dict_r.get('name')
        if len(dict_r) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(dict_r.get('id'), dict_r.get('name')))
    except:
        print("Not a valid JSON")
