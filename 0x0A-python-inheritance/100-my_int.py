#!/usr/bin/python3
"""defines Myint class"""

class Myint(int):
    """Myint class"""
    def __eq__(self, value):
        """eq method"""
        return self.real != value

    def __ne__(self, value):
        """ne method"""
        return self.real == value
