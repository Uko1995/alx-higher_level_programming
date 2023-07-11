#!/usr/bin/python3
'''
module for task 101
'''


def add_attribute(obj, attribute_name, attribute_value):
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute_name, attribute_value)
