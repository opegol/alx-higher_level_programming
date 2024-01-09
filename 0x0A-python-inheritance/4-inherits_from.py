#!/usr/bin/python3

def inherits_from(obj, a_class):
    """Checks to see if obj is an instance of a_class or a derived class

    Args:
        obj (object): Object to compare
        a_class (class): class to compare obj to
    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ; otherwise False.
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
