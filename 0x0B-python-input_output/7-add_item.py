#!/usr/bin/python3

"""Adds all arguments to a Python list, and then save them to a file."""

import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    l_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    fname = "add_item.json"
    try:
        items = l_from_json_file(fname)
    except Exception:
        items = []
    for item in sys.argv[1:]:
        items.append(item)
    save_to_json_file(items, fname)
