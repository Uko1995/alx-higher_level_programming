#!/usr/bin/python3
'''
@author: Uko Uwatt

'''


class Rectangle:

    '''
    a class that defines a rectangle

    Attributes:
    empty
    '''
    def __init__(self, width=0, height=0):
        '''
        initailizes instances of the rectangle

        Attributes:
        width(int, optional): width of the rectangle
        height(int, optional): height of the rectangle
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''
        function retrieves width

        Return: width of the rectangle
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        function sets width

        Attributes:
        width: width of the rectangle

        Raises:
        ValueError: if width is less than 0
        TypeError: if width is not an integer
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''
        function checks height

        Return: the height of the rectangle
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        function sets height

        Atributes:
        height: height if the rectangle

        Raises:
        TypeError: if height is not an integer
        ValueError: if height is les than 0
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
