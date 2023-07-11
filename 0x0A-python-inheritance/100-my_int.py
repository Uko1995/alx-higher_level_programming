#!/usr/bin/python3
'''
module for task 100
'''


class MyInt(int):
    '''
    MyInt class inherits from Int
    '''
    def __eq__(self, number):
        '''
        initailizes iniquality
        '''
        return super().__ne__(number)

    def __ne__(self, number):
        '''
        initializes equality
        '''
        return super().__eq__(number)
