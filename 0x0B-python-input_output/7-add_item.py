#!/usr/bin/python3
"""
Module to add all args to a Python list,
and then save to a file.
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    arg_list = load_from_json_file("add_item.json")
except:
    arg_list = []
for arg in range(1, len(argv)):
    arg_list.append(argv[arg])

save_to_json_file(arg_list, "add_item.json")
