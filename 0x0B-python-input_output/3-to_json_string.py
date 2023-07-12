#!/usr/bin/python3
'''
module for this task
'''


def to_json_string(my_obj):
    '''
    returns the json representation of an object
    '''
    import json

    line = json.dumps(my_obj)
    return line
