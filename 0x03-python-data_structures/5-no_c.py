#!/usr/bin/env python3
def no_c(my_string):
    new_string = ""
    if my_string:
        for letter in my_string:
            if letter not in "Cc":
                new_string += letter
    return new_string