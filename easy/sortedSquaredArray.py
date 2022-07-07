#!/usr/bin/env python3
# spaces not tabs
"""
    Write a function that takes in a non-empty array of integers that are
    sorted in ascending order and returns a new array of the same length with
    the squares of the orignial integers also sorted in ascending order.
"""
def sortedSquaredArray(array):
    """
        Description:  Function takes a sorted ascending array and squares the
        values, then returns the new array sorted ascending.

        Parameters:
            array - list of integers sorted ascending

        Returns:
            array - list of integers (array squared) sorted ascending
    """
    # create empty list for return values
    squaredValues = []

    # iterate through array and square each value, then store the value in
    # squaredValues.
    for num in array:
        squaredValues.append(num*num)
    
    # sort the squaredValues
    squaredValues.sort()

    # return the new list
    return squaredValues