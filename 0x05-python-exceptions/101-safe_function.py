#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        return fct(*args)

    except(ZeroDivisionError, ValueError, TypeError, IndexError) as reeses_error:
        print("Exceptions: {}".format(reeses_error), file=sys.stderr)
        return None
