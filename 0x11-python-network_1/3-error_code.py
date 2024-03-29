#!/usr/bin/python3
"""script takes in a URL, sends a request to the URL and
    displays the body of the response
    (decoded in utf-8)
"""

import sys
import urllib.request
from urllib.error import HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(f"{html.decode('utf-8')}")
    except urllib.error.HTTPError as err:
        print(f"Error code: {err.code}")
