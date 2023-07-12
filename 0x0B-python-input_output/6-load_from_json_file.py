#!/usr/bin/python3
'''
module for this task
'''


def load_from_json_file(filename):
    '''
    creates an object from a json file
    '''
    import json

    with open(filename, 'r', encoding='utf-8') as my:
        data = json.load(my)
    return data
