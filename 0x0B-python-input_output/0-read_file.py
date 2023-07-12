#!/usr/bin/python3
'''
module for task 0
'''


def read_file(filename=""):
    '''
    function reads a txt file and prints it out to stdout
    '''
    with open(filename, encoding='utf-8') as myFile:
        line = myFile.read()
        print(line, end='')
