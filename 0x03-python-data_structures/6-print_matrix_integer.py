#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for num in lst:
            print("{}".format(num), end=" ")
        print()
