#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for lst in matrix:
            for num in lst:
                print("{:d}".format(num), end=" " if lst.index(num) < len(lst) - 1 else "")
                if num is not lst[len(lst) - 1]:
                    print(" ", end="")
            print()
