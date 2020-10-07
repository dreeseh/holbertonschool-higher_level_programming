#!/usr/bin/python3
"""
a script that adds all arguments to a
Python list, and then save them to a file:
"""
from sys import argv
from os import path


save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

filename = "add_item.json"

if path.isfile(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

for i in range(1, len(argv)):
    my_list.append(argv[i])

save_to_json_file(my_list, filename)
