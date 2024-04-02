#!/usr/bin/python3
"""Defines a method of finding lists peaks"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of unsorted integers.
    """
    n = len(list_of_integers)
    if n == 0:
        return None
    
    left = 0
    right = n - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # Check if mid is a peak
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # Peak is on the left side
            right = mid
        else:
            # Peak is on the right side
            left = mid + 1
    
    # Return the peak element
    return list_of_integers[left]

