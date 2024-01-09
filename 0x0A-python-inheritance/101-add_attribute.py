#!/usr/bin/python3

def add_attribute(obj, attr, val):
    """adds a new attribute to an object if it’s possible.

    Args:
        obj (object): given object to add new attribute.
        attr (str): attribute to add.
        val (any): value of attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
