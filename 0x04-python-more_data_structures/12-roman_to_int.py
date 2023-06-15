#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    else:
        result = 0
        n = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        roman = list(roman_string)
        for char in roman:
            for k, v in n.items():
                if char == k:
                    result += v
        return result
