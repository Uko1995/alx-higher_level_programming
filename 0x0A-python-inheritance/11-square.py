#!/usr/bin/python3
'''
module for task 11
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
        '''
        initializing rectangle
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''
        returns the area of the rectangle
        '''

        return self.__width * self.__height

    def __print__(self):
        '''
        prints the rectangle information
        '''
        print("[Rectangle] {} / {}".format(self.__width, self.__height))

    def __str__(self):
        '''
        returns the rectangle information
        '''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)


class Square(Rectangle):
    '''
    square class inherits from Rectangle
    '''
    def __init__(self, size):
        '''
        initializes square
        '''
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        '''
        returns information about square
        '''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)

    def __print__(self):
        print("[Square] {}/{}".format(self.__size, self.__size))
