#!/bin/bash
# a Bash script that sends a request to a URL passed as an argument,
curl -sLw "%{http_code}" "$1" -o /dev/null
