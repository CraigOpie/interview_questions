#!/usr/bin/env python3
# spaces not tabs
"""
    Given two non-empty arrays of integers, write a function that determines
    whether the second array is a subsequence of the first one.

    A subsequence of an array is a set of numbers that aren't necessarily adjacent
    in the array but that are in the same order as they appear in the array. For
    instance, the numbers [1, 3, 4] form a subsequence in the array [1, 2, 3, 4], 
    and so do the numbers [2, 4].  Note that a single number in an array and the
    array itself are both valid subsequences of the array.
"""
def isValidSubsequence(array, sequence):
    """
        Description:  Function takes an array and a sequence of numbers and searches
        the array to see if the sequence appears as a subsequence.

        Parameters:
            array - list of integers
            sequence - list of integers

        Returns:
            true or false
    """
    # create iteration index tracker
    index_ = 0

    # iterate throught the array and search for each integer in the sequence using
    # an index to track the sequence value being searched.  returns true if the
    # search iterates through all of the sequence.
    for num in array:
        if index_ == len(sequence):
            return True
        if num == sequence[index_]:
            index_ += 1

    # returns false if the sequence was not fully iterated through
    return index_ == len(sequence)
