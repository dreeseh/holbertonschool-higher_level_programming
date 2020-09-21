#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)

    except Exception as reeses_err:
        import sys
        print("Exception: {}".format(reeses_err), file=sys.stderr)
        return None
