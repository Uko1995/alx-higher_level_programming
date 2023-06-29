#!/usr/bin/python3

# -*- coding: utf-8 -*-
'''
@author: Uko Uwatt
'''


class Square:
    """Class Square that has attributes. Instantiation with size

    Attributes:
        size (int): The size of the square
    """

    def __init__(self, size=0):
        """The __init__ method for Square class

        Args:
            size: (:obj: 'int'): A private instance size

        Raises:
        TypeError: if size is not an integer
        ValueError: if size is less then 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        '''
        calculates the area of a square

        Returns:
        the area of the square
        '''
        return self.__size ** 2
