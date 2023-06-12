#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for lst in matrix:
            for num in lst:
                end_string = "" if (lst.index(num) == len(lst) - 1) else " "
                print("{:d}".format(num), end=end_string)
            print()
