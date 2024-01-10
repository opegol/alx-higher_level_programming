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

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""
        return self.__dict__
