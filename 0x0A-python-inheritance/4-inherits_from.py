#!/usr/bin/python3
'''
module for task 4
'''


def inherits_from(obj, a_class):
    '''
    checks if obj is an instance of a_class
    '''
    return issubclass(type(obj), a_class) and type(obj) != a_class
