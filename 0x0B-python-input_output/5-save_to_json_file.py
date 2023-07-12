#!/usr/bin/python3
'''
module for this task
'''


def save_to_json_file(my_obj, filename):
    '''
    writes an object into a text file
    '''
    import json

    with open(filename, 'w', encoding='utf-8') as myFile:
        return myFile.write(json.dumps(my_obj))
