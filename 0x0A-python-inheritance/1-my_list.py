#!/usr/bin/python3
'''
this module contains Mylist class
'''


class MyList(list):
    '''
    class Mylist inherits attributes from parent class list
    '''
    def print_sorted(self):
        '''
        function prints sorted list of object
        '''
        sorted_list = sorted(self)
        print(sorted_list)
