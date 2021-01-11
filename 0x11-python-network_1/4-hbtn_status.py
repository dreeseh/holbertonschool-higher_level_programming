#!/usr/bin/python3
"""
a Python script that fetches https://intranet.hbtn.io/status
"""
import requests


if __name__ == '__main__':
    r = requests.get('https://intranet.hbtn.io/status')
    info = r.text
    print("Body response:")
    print("\t- type: {}".format(type(info)))
    print("\t- content: {}".format(info))
