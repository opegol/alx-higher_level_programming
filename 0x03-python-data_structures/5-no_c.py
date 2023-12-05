#!/usr/bin/env python3
def no_c(my_string):
    my_string
    new = [ch for ch in my_string if ch != 'C' and ch != 'c']
    return (''.join(new))
