#!/usr/bin/python3
"""module of load_file_from_json_file"""
import json


def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”
    """
    with open(filename, 'r') as f:
        return json.loads(f.read())
