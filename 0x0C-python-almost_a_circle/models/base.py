#!/usr/bin/python3
'''
class Base
'''


import json


class Base:
    '''base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        class constructor
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        returns the JSON string representation of list_dictionaries
        '''
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        writes the JSON string representation of list_objs to a file
        '''
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as obj:
            save = cls.to_json_string([obj.to_dictionary()
                                       for obj in list_objs])
            obj.write(save)

    @staticmethod
    def from_json_string(json_string):
        '''
        returns the list of the JSON string representation json_string
        '''
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return list(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        '''
        returns an instance with all attributes already set

        '''
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)

        if obj:
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        '''
        returns a list of instances
        '''
        try:
            filename = cls.__name__ + ".json"
            with open(filename, "r", encoding="utf-8") as b:
                lsts = cls.from_json_string(b.read())
                instance = [cls.create(**i) for i in lsts]
                return instance
        except FileNotFoundError:
            return []
        except Exception:
            return []
