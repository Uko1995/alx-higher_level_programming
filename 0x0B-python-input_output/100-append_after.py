#!/usr/bin/python3
'''
module for this task
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    function append new_string after search_string has been found
    '''
    with open(filename, "r", encoding="utf-8") as name:
        lines = name.readlines()

    with open(filename, "w", encoding="utf-8") as name:
        for line in lines:
            name.write(line)
            if search_string in line:
                name.write(new_string)
