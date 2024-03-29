#!/usr/bin/python3
"""script takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    pwd = sys.argv[2]
    a = HTTPBasicAuth(username, pwd)
    r = requests.get('https://api.github.com/user', auth=a)
    rj = r.json()
    print(rj["id"])
