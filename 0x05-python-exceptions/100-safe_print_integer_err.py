#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys

    try:
        print("{:d}\n".format(int(value)))
        return True
    except (ValueError, TypeError) as err:
        print("Exception: {} is not an integer".format(err), file=sys.stderr)
        return False
