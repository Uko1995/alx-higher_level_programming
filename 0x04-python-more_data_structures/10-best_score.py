#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        biggest_score = max(a_dictionary.values())
        for key, value in a_dictionary.items():
            if value == biggest_score:
                return key
    else:
        return None
