#!/usr/bin/env python3
# spaces not tabs
"""
    You're looking to move into a new apartment on specific street, and you're
    given a list of contiguous blocks on that street where each block contains an
    apartment that you could move into.

    You also have a list of requirements: a list of buildings that are important
    to you. For instance, you might value having a school and a gym near your
    apartment. The list of blocks that you have contains information at every
    block about all of the buildings that are present and absent at the block in
    question. For instance, for every block, you might know whether a school, a
    pool, an office, and a gym are present.

    You also have a list of requirements: a list of buildings that are important
    to you. For instance, you might value having a school and a gym near your
    apartment. The list of blocks that you have contains information at every
    block about all of the buildings that are present and absent at the block in
    question. For instance, for every block, you might know whether a school, a
    pool, an office, and a gym are present.

    Write a function that takes in a list of contiguous blocks on a specific
    street and a list of your required buildings and that returns the location
    (the index) of the block that's most optimal for you.

    If there are multiple most optimal blocks, your function can return the index
    of any one of them.
"""
def apartmentHunting(blocks, reqs):
    minDistFromBlocks = list(map(lambda req: getMinDist(blocks, req), reqs))
    maxDistAtBlocks = getMaxDistAtBlocks(blocks, minDistFromBlocks)
    return getIdAtMinValue(maxDistAtBlocks)

def getMinDist(blocks, req):
    minDist = [0 for blcok in blocks]
    closestReqId = float("inf")
    for i in range(len(blocks)):
        if blocks[i][req]:
            closestReqId = i
        minDist[i] = distBetween(i, closestReqId)
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closestReqId = i
        minDist[i] = min(minDist[i], distBetween(i, closestReqId))
    return minDist

def getMaxDistAtBlocks(blocks, minDistFromBlocks):
    maxDistAtBlocks = [0 for blcok in blocks]
    for i in range(len(blocks)):
        minDistAtBlock = list(map(lambda dist: dist[i], minDistFromBlocks))
        maxDistAtBlocks[i] = max(minDistAtBlock)
    return maxDistAtBlocks

def getIdAtMinValue(array):
    idAtMinValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idAtMinValue = i
    return idAtMinValue

def distBetween(a, b):
    return abs(a-b)