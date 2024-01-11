#!/usr/bin/python3

"""Defines append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each
    line containing a specific string.

    Args:
        filename (str):.
        search_string (str):.
        new_string (str):.
    """
    mod_text = ""
    with open(filename) as f:
        for line in f:
            mod_text += line
            if search_string in line:
                mod_text += new_string
    with open(filename, "w") as wf:
        wf.write(mod_text)
