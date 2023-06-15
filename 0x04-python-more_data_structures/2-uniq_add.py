#!/usr/bin/python3
def uniq_add(my_list=[]):
    sorted_list = set(my_list)
    result = 0
    for num in sorted_list:
        result += num
    return result
