#!/usr/bin/python3
'''
module contains "is_same_class" function
'''


def is_same_class(obj, a_class):
    '''
    function returns True if obj is a subclass of a_class
    otherwise return False
    '''
    return type(obj) is a_class
