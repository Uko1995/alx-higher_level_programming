#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    args = len(argv)
    if args < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    first = int(argv[1])

    second = int(argv[3])

    if argv[2] == '+':
        result = add(first, second)
    elif argv[2] == '-':
        result = sub(first, second)
    elif argv[2] == '*':
        result = mul(first, second)
    elif argv[2] == '/':
        result = div(first, second)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(first, argv[2], second, result))
