#!/usr/bin/python3
'''
module for this task
'''


import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


with open("add_item.json", "a+") as myFile:
    data = sys.argv[1:]
    save_to_json_file(data, "add_item.json")
