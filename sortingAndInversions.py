import numpy as np
import math


def mergeSetsWithInversions(opSet):
    A = math.floor(len(opSet) / 2)
    B = len(opSet) - A
    a = np.copy(opSet[0:A])
    b = np.copy(opSet[A:len(opSet)])
    i = 0
    j = 0
    inversions = 0
    invTicker = 0

    while i < A and j < B:
        if a[i] <= b[j]:
            opSet[i + j] = a[i]
            i += 1
            inversions+=invTicker
        else:
            invTicker+=1
            opSet[i + j] = b[j]
            j += 1

    while j < B:
        opSet[i + j] = b[j]
        j += 1

    while i < A:
        opSet[i + j] = a[i]
        i += 1
        inversions += invTicker

    return inversions

def countInversions(opSet):
    if len(opSet) == 1:
        return 0
    elif len(opSet) == 2:
        if opSet[0] > opSet[1]:
            temp = opSet[0]
            opSet[0] = opSet[1]
            opSet[1] = temp
            return 1
        else:
            return 0
    else:
        leftInv = countInversions(opSet[0:math.floor(len(opSet) / 2)])
        rightInv = countInversions(opSet[math.floor(len(opSet) / 2): len(opSet)])
        return mergeSetsWithInversions(opSet)+leftInv+rightInv



def bubbleSort(opSet):
    A = len(opSet)
    i = 0
    redundant = False

    while i < len(opSet) - 1 and not redundant:

        redundant = True
        z = 0

        while z < A - 1:
            # make swaps
            if opSet[z] > opSet[z + 1]:
                temp = opSet[z]
                opSet[z] = opSet[z + 1]
                opSet[z + 1] = temp
                redundant = False
            z += 1

        A -= 1
        i += 1


def mergeSets(opSet):
    A = math.floor(len(opSet) / 2)
    B = len(opSet) - A
    a = np.copy(opSet[0:A])
    b = np.copy(opSet[A:len(opSet)])
    i = 0
    j = 0

    while i < A and j < B:
        if a[i] <= b[j]:
            opSet[i + j] = a[i]
            i += 1
        else:
            opSet[i + j] = b[j]
            j += 1

    while j < B:
        opSet[i + j] = b[j]
        j += 1

    while i < A:
        opSet[i + j] = a[i]
        i += 1


def mergeSort(opSet):
    if len(opSet) == 1:
        return
    elif len(opSet) == 2:
        if opSet[0] > opSet[1]:
            temp = opSet[0]
            opSet[0] = opSet[1]
            opSet[1] = temp
    else:
        mergeSort(opSet[0:math.floor(len(opSet) / 2)])
        mergeSort(opSet[math.floor(len(opSet) / 2): len(opSet)])
        mergeSets(opSet)


def findAddingToBest(opSet, searched):
    if len(opSet) < 2:
        return
    mergeSort(opSet)
    i = 0
    j = len(opSet) - 1
    while i != j:
        if opSet[i] + opSet[j] == searched:
            return True
        elif opSet[i] + opSet[j] > searched:
            j -= 1
        else:
            i += 1

    return False


def findAddingToRecursive(opSet, searched):  # made it myself. It's really fucked up an

    if len(opSet) == 2:
        return (opSet[0] + opSet[1]) == searched
    elif len(opSet) == 1:
        return opSet[0] == searched

    if findAddingToRecursive(opSet[0:math.floor(len(opSet) / 2)], searched) or findAddingToRecursive(
            opSet[math.floor(len(opSet) / 2):len(opSet)], searched):
        return True
    else:
        for i in range(math.floor(len(opSet) / 2)):
            for z in range(math.floor(len(opSet) / 2), len(opSet)):
                if opSet[i] + opSet[z] == searched:
                    return True
        return False


def findAddingTo(opSet, searched):
    controlList = []
    for i in range(len(opSet)):
        for z in range(len(controlList)):
            if opSet[i] == controlList[z]:
                return True
        controlList.append(searched - opSet[i])
    return False


def binarySearch(searchList, toSearch):  # pessimistic complexity of log n
    length = len(searchList)
    if length < 1:
        return -1

    topBound = length  # first not included element
    bottomBound = 0  # first included element

    while topBound - bottomBound > 0:  # while there are still some numbers
        midGuess = math.floor((topBound + bottomBound) / 2)  # take the middle one
        if searchList[midGuess] == toSearch:
            return midGuess
        elif searchList[midGuess] > toSearch:
            topBound = midGuess
        else:
            bottomBound = midGuess + 1

    return -1


def insertionSort(toSort, step=False):
    for eID in range(1, len(toSort)):  # we do not have to check the first one - it's sorted by the beginning
        toSwitch = eID - 1
        move = toSort[eID]
        while toSwitch >= 0 and toSort[toSwitch] > move:
            # we are looking for the "zeroth" element (if this one is the smallest) or the one which is smaller
            toSort[toSwitch + 1] = toSort[toSwitch]  # we are switching the neighbours
            toSwitch -= 1
        toSort[toSwitch + 1] = move  # we put our move just after the last right element.
        if step:
            print(eID, " = ", toSort)


def recursiveInsertionSort(toSort):
    # exit recursion conditional
    length = len(toSort)
    if length < 2:
        return

    recursiveInsertionSort(toSort[:length - 1])  # sort the previous elements

    # then put the n-th one into the before-part. Just like iteration-like version above

    toSwitch = length - 2
    move = toSort[length - 1]
    while toSwitch >= 0 and toSort[toSwitch] > move:
        toSort[toSwitch + 1] = toSort[toSwitch]
        toSwitch -= 1

    toSort[toSwitch + 1] = move



# bubbleSort(testArray)
# insertionSort(testArray, True)
# recursiveInsertionSort(testArray)
# res = binarySearch(testArray,0)
# print(res)
#print(findAddingToBest(testArray, 18))

