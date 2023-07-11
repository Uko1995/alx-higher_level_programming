#!/usr/bin/python3
'''
module for task 8
'''


class BaseGeometry:
    '''
    empty class
    '''
    def area(self):
        '''
        function raises exception
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        function checks if value is an integer and is greater than 0
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''
    rectangle class inherits from BaseGeometry class
    '''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
