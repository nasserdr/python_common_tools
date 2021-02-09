#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as te:
        sys.stderr.write("Exception: ".format(te))
        return None
