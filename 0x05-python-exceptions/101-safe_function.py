#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)

    except Exception as reeses_err:
        print("Exceptions: {}".format(reeses_err), file=sys.stderr)
        return None
