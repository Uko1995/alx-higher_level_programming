#!/usr/bin/python3
'''
module for task 1
'''


def write_file(filename="", text=""):
    '''
    reads a text in to a file
    '''
    with open(filename, 'w', encoding='utf-8') as myFile:
        line = myFile.write(text)
    return line
