#!/usr/bin/python3
'''
module for square class
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    square class that inherits from Rectangle class
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        class constructor
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
        prints fromatted string to stdout
        '''
        return "[Square] " + "(" + str(self.id) + ") " + str(self.x) + "/"\
            + str(self.y) + " - " + str(self.width)

    @property
    def get_size(self):
        '''
        gets the size attribute
        '''
        return self.width

    @size.setter
    def set_size(self, value):
        '''
        sets the size
        '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''
        assigns attributes:
        id
        size
        x
        y
        '''
        keys = ["id", "size", "x", "y"]
        i = 0
        if args is not None and len(args) != 0:
            for arg in args:
                setattr(self, keys[i], arg)
                i += 1

        elif kwargs is not None and len(kwargs) != 0:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''
        returns he dictionary representation of a square
        '''
        dic = {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
        return dic
