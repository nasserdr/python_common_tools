#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
In addition, it handles HTTPError exceptions to print
the HTTP Status Code, if an error occurs.
"""

from sys import argv
from urllib import request, error


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as req:
            print(req.read().decode("utf-8"))
    except error.HTTPError as ex:
        print("Error code: {}".format(ex.code))
