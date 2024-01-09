#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """Checks to see if obj is an instance of a_class or a derived class

    Args:
        obj (object): Object to compare
        a_class (class): class to compare obj to
    Returns:
        True if the object is an instance of, or if
        the object is an instance of a class that inherited from,
        the specified class ; otherwise False.
    """
    return (isinstance(obj, a_class))
