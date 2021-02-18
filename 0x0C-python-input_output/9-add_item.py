#!/usr/bin/python3
"""
Append every 2 arguments as key/value into a file containing a
object
"""
import json
import sys


load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
filename = 'add_item.json'

try:
    my_list = load_from_json_file(filename)
except Exception:
    my_list = []

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, filename)
