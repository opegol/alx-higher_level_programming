#!/usr/bin/python3
def uniq_add(my_list=[]):
    n = list(set(my_list))
    sum = 0
    for i in n:
        sum += i
    return sum
