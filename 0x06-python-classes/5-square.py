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
        """
        self.__size = size

    @property
    def size(self):
        '''
        function checks property

        Returns:
        the size of the square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        the function sets the size of the square

        Raises:
        TypeError: if value is not an integer
        ValueError: if value is less than 0
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''
        function calculates the area of the square

        Returns:
        the area of the square
        '''
        return self.__size ** 2

    def my_print(self):
        '''
        this function prints the size of the square to stdout with #
        '''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
