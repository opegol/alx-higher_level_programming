#!/usr/bin/python3
"""script takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    val = {'q': letter}
    r = requests.post('http://0.0.0.0:5000/search_user', json=val)
    try:
        rj = r.json()
        if rj == {}:
            print("No result")
        else:
            print(f"[{r['idi']}] {r['name']}")
    except (ValueError, requests.exceptions.JSONDecodeError):
        print('Not a valid JSON')
