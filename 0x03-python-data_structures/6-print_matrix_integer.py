#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for lst in matrix:
            for num in lst:
                print("{:d}".format(num), end=" ")
            print()
