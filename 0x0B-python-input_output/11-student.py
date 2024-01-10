#!/usr/bin/python3

"""Definition of 'student' class"""


class Student:
    """Student Class."""
    def __init__(self, first_name, last_name, age):
        """Initializes new student instance.

        Args:
            first_name (str): first_name.
            last_name (str): last_name.
            age (int): age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved. Otherwise, all attributes
        must be retrieved.

        Args:
            attr: Attribute
        """
        if (isinstance(attrs, list) and
                all(type(item) is str for item in attrs)):
            pdict = {}
            for item in attrs:
                if hasattr(self, item):
                    pdict[item] = getattr(self, item)
            return pdict
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json: dictionary with which to replace attributes.
        """
        for (key, val) in json.items():
            setattr(self, key, val)
