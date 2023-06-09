#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    result = 0
    args = len(argv)
    if args <= 1:
        print(result)
    else:
        for arg in range(1, args):
            result += int(argv[arg])
        print(result)
