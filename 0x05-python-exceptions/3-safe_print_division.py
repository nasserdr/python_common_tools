#!/usr/bin/python
def safe_print_division(a, b):
    try:
        result = a/b
    except (ZeroDivisionError, UnboundLocalError):
        result = None
    finally:
        print('Inside result: {}'.format(result))
        return result
