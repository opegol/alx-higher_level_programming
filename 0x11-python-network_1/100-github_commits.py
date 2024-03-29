#!/usr/bin/python3
"""script lists 10 commits (from the most recent to oldest)
    of the repository “rails” by the user “rails”
    using GitHub API
    Print all commits by: `<sha>: <author name>` (one by line).
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    r = requests.get(url)
    rj = r.json()
    try:
        for i in range(10):
            print(f"{rj[i]['sha']}: {rj[i]['commit']['author']['name']}")
    except IndexError:
        pass
