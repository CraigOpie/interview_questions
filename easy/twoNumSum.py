#!/usr/bin/env python3
# spaces not tabs
"""
    Write a function -> takes a non-empty array of integers and an integer of target sum.
    If any two numbers match the target, then return them in an array (any order).
    Else, return an empty array.

    Example Return: [1, 11]
"""
def twoNumberSum(array, targetSum):
    """ 
        Description: Function takes a list of integers and finds summing pairs and returns
        the pairs in a list.
    
        Parameters:
            array - list of integers
            targetSum - integer

        Returns:
            sums - list of pairs 
    """
    # store the array in a set to speed up searching
    temp = set(num for num in array)

    # iterate through each number in the array and look for the summing pair in temp
    # return the pair if it exists
    for num in array:
        target = targetSum - num
        if target in temp and target is not num:
            return [num, target]

    # return an empty list if a pair does not exist
    return []
