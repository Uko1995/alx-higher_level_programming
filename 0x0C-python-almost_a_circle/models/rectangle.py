#!/usr/bin/python3
'''
class rectangle
'''

from models.base import Base


class Rectangle(Base):
    '''
    rectangle class that inherits from Base class
    '''

    def validate(self, name, value):
        '''
        validates the private attributes
        self.__width
        self.__height
        self.__x
        self.__y
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif (name == 'width' or name == 'height') and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif (name == 'x' or name ==  'y') and value < 0:
            raise ValueError("{} must be >= 0".format(name))

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
        self.validate("width", value)
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
        self.validate("height", value)
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
        self.validate("x", value)
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
        self.validate("y", value)
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        class constructor
        '''
        super().__init__(id)
        self.validate("width", width)
        self.__width = width
        self.validate("height", height)
        self.__height = height
        self.validate("x", x)
        self.__x = x
        self.validate("y", y)
        self.__y = y
