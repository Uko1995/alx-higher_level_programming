#!/usr!bin/python3
'''
module for task 100
'''


class MyInt(int):
    '''
    MyInt class inherits from Int
    '''
    def __eq__(self, number):
        return super().__ne__(number)

    def __ne__(self, number):
        return super().__eq__(number)
