#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    k = a_dictionary.keys()
    for i in sorted(list(k)):
        print("{}: {}".format(i, a_dictionary[i]))
