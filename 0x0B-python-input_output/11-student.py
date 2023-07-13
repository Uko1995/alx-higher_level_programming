#!/usr/bin/python3
'''
module for this task
'''


class Student:
    '''
    student class with public instance attributes
    first_name
    last_name
    age
    '''
    def __init__(self, first_name, last_name, age):
        '''
        instantiating the object
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        retrieves a dictionary representation of a Student instance
        '''
        if attrs is None:
            return self.__dict__

        json_dict = {}
        for string in attrs:
            if hasattr(self, string):
                json_dict[string] = getattr(self, string)

        return json_dict

    def reload_from_json(self, json):
        '''
        replaces all attributes of the Student instance
        '''
        if (json):
            self.__dict__ = json
