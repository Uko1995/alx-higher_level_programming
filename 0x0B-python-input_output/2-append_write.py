#!/usr/bin/python3
'''
module for task 2
'''


def append_write(filename="", text=""):
    '''
    appends text to a file
    '''
    with open(filename, 'a', encoding='utf-8') as myFile:
        return myFile.write(text)
