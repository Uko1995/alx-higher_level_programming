#!/usr/bin/python3
'''
module for this task
'''


def from_json_string(my_str):
    '''
    returns an object represented by json
    '''
    import json

    line = json.loads(my_str)
    return line
