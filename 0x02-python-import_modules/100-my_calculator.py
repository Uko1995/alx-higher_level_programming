#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    args = len(argv)
    if args <= 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    first = int(argv[1])
    second = int(argv[2])
    op = argv[2]
    if op == '+':
        result = add(first, second)
    elif op == '-':
        result = sub(first, second)
    elif op == '*':
        result = mul(first, second)
    elif op == '/':
        result = div(first, second)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(first, op, second, result))
