#!/usr/bin/python3
"""script in a URL, sends a request to the URL and displays
    the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
