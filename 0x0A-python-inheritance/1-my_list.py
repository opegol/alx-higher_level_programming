#!/usr/bin/python3

"""MyList class definition inherits from List."""

class MyList(list):
    """ MyList class inherits from list."""
    
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))

