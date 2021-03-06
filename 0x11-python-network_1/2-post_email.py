#!/usr/bin/python3
"""
akes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response
"""
import urllib.request as request
import urllib.parse as parse
from sys import argv


if __name__ == "__main__":
    val = {'email': argv[2]}
    data = parse.urlencode(val).encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as r:
        print(r.read().decode('utf-8'))
