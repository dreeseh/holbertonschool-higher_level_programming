#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True

    except Exception as reeses_exception:
        sys.stderr.write("Exception: {}\n".format(reeses_exception))

        return False
