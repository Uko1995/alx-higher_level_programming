#!/usr/bin/python3
'''
class rectangle
'''

from models.base import Base


class Rectangle(Base):
    '''
    rectangle class that inherits from Base class
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        class constructor
        '''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''
        gets the width attribute
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        sets width
        '''
        self.__width = value

    @property
    def height(self):
        '''
        gets height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        sets height
        '''
        self.__height = value

    @property
    def x(self):
        '''
        gets x
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        sets x
        '''
        self.__x = value

    @property
    def y(self):
        '''
        gets y
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        sets y
        '''
        self.__y = value
