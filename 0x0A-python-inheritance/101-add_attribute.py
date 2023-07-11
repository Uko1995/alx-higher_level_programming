#!/usr/bin/python3
'''
module for task 101
'''


def add_attribute(obj, attribute_name, attribute_value):
    '''
    adds attribute if it is possible to be added
    '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute_name, attribute_value)
