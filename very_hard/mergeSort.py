#!/usr/bin/env python3
# spaces not tabs
"""
    Write a function that takes in an array of integers and returns a sorted
    version of that array. Use the Merge Sort algorithm to sort the array.
"""
def mergeSort(array):
    if len(array) <= 1:
        return array
    auxArray = array[:]
    helper(array, 0, len(array) - 1, auxArray)
    return array

def helper(mainArray, startID, endID, auxArray):
    if startID == endID:
        return
    middleID = (startID + endID) // 2
    helper(auxArray, startID, middleID, mainArray)
    helper(auxArray, middleID + 1, endID, mainArray)
    merge_(mainArray, startID, middleID, endID, auxArray)

def merge_(mainArray, startID, middleID, endID, auxArray):
    k = startID
    i = startID
    j = middleID + 1
    while i <= middleID and j <= endID:
        if auxArray[i] <= auxArray[j]:
            mainArray[k] = auxArray[i]
            i += 1
        else:
            mainArray[k] = auxArray[j]
            j += 1
        k += 1
    while i <= middleID:
        mainArray[k] = auxArray[i]
        i += 1
        k += 1
    while j <= endID:
        mainArray[k] = auxArray[j]
        j += 1
        k += 1