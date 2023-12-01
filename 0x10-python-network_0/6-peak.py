#!/usr/bin/python3
# function that finds a peak in a list of unsorted integers

def find_peak(list_of_integers):
    # function calculates the peak of a list of integers
    maximum = None
    if (list_of_integers is None) or (len(list_of_integers) == 0):
        maximum = None
    else:
        maximum = max(list_of_integers)
    return maximum
