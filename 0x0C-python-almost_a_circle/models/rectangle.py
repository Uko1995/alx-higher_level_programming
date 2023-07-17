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
        elif (name == 'x' or name == 'y') and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def get_width(self):
        '''
        gets the width attribute
        '''
        return self.__width

    @width.setter
    def set_width(self, value):
        '''
        sets width
        '''
        self.validate("width", value)
        self.__width = value

    @property
    def get_height(self):
        '''
        gets height
        '''
        return self.__height

    @height.setter
    def set_height(self, value):
        '''
        sets height
        '''
        self.validate("height", value)
        self.__height = value

    @property
    def get_x(self):
        '''
        gets x
        '''
        return self.__x

    @x.setter
    def set_x(self, value):
        '''
        sets x
        '''
        self.validate("x", value)
        self.__x = value

    @property
    def get_y(self):
        '''
        gets y
        '''
        return self.__y

    @y.setter
    def set_y(self, value):
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

    def area(self):
        '''
        returns the area of the rectangle
        '''
        return self.__width * self.__height

    def display(self):
        '''
        displays the rectangle using #
        '''
        for c in range(self.__y):
            print()
        for d in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        '''
         returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
         '''
        return "[Rectangle] " + "(" + str(self.id) + ")" + " " + str(self.__x) + "/"\
            + str(self.__y) + " - " + str(self.__width) + "/" + str(self.__height)

    def update(self, *args, **kwargs):
        '''
        assigns an argument to each attribute
        '''
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.__width = arg
                elif i == 2:
                    self.__height = arg
                elif i == 3:
                    self.__x = arg
                elif i == 4:
                    self.__y = arg

        elif kwargs is not None and len(kwargs) != 0:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def to_dictionary(self):
        '''
        returns the dictionary representation of a Rectangle
        '''
        dic = {"id": self.id, "width": self.__width, "height": self.__height,\
            "x": self.__x, "y": self.__y}
        return dic
