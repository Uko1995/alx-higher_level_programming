#!/usr/bin/python3
"""rectange class"""


class Rectangle:
    """makes rectangle object"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets width"""
        return self.__width

    @property
    def height(self):
        """gets height"""
        return self.__height

    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''
        gets area

        Returns: area of rectangle
        '''
        return self.__height * self.__width

    def perimeter(self):
        '''
        function returns perimeter of rectangle
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        '''
        gets string
        '''
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for i in range(self.__height):
            rectangle += "#" * self.__width + "\n"
        return rectangle.rstrip()

    def __repr__(self):
        '''
        return a string representation of the rectangle
        to be able to recreate a new instance
        '''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        '''
        prints a message when rectangle instance has been deleted
        '''
        print("Bye rectangle...")
