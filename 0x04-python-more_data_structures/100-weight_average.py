#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        num, den = 0, 0
        for lst in my_list:
            num += lst[0] * lst[1]
            den += lst[1]
        result = num / den
    return result
