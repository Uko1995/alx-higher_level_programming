#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    args = len(argv)
    first = int(argv[1])
    second = int(argv[3])
    op = argv[2]
    if args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if op == '+':
        print("{} {} {} = {}".format(first, op, second, add(first, second)))
    elif op == '-':
        print("{} {} {} = {}".format(first, op, second, sub(first, second)))
    elif op == '*':
        print("{} {} {} = {})".format(first, op, second, mul(first, second)))
    elif op == '/':
        print("{} {} {} = {}".format(first, op, second, div(first, second)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
