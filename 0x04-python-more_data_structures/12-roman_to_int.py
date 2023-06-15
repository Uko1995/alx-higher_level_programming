#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    else:
        result = 0
        prev_v = 0
        n = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        roman = list(roman_string)
        for char in roman[::-1]:
            v = n.get(char, 0)
            if v >= prev_v:
                result += v
            else:
                result -= v
            prev_v = v
        return result
