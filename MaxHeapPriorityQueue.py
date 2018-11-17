
"""
Author: Keith DeSimini
Date: Nov 17 2018
"""


def maxHeapify(arr, n, i):
    """
    Given an array arr, perform the heapify function. To be used inside of
    helper function buildMaxHeap. The function will ensure the heap property
    is held for the current subtree, performing swaps when needed.


    :param arr: the array to be heapified
    :param n: the size of the array
    :param i: the largest value (root)
    :rtype arr: list
    :rtype n: int
    :rtype i: int
    """
    largest = i
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Heapify if swap occurred to verify integrity of heap.
        maxHeapify(arr, n, largest)


def buildMaxHeap(arr):
    """
    Given an array arr, this helper function will iterate backwards
    over the array and call heapify(arr, n, i) on it to build a max heap.
    This is done backwards to ensure than when an element floats through
    the tree, the consequential break of heap property can be fixed through
    a recursive call in heapify(arr, n, i)

    :param arr: the array to be heapified
    :rtype arr: list
    """
    n = len(arr)
    for i in range(n, -1, -1):  # Build the heap
        maxHeapify(arr, n, i)
    return arr


def getMaximum(arr):
    """
    Given an array arr, this will return the root of the heap.
    This is also the maximum value since it's a max-heap.

    :param arr: the array that holds the max value
    :rtype arr: int
    """

    return arr[0]


def extractMax(arr):
    """
    Given an array arr, this function will extract the max value
    from the list, rendering the list one element less. In this
    particular instance, we also call max heapify on the array
    to restore the heap property.

    :param arr: the array that holds the max value
    :rtype arr: int
    """

    arr_size = len(arr) - 1
    if arr_size < 1:
        return "error: out of range"
    max_value = arr[0]
    arr[0] = arr[arr_size]
    arr_size += -1
    for i in range(arr_size + 1, -1, -1):
        maxHeapify(arr, arr_size + 1, i)
    del arr[-1]
    return max_value


def heapIncreaseKey(arr, i, key):

    """
    Given an array arr, index i, and value key, this function will
    increase the value at the indicated index position. If the value
    is less than the current key, we return to keep the heap property(Not too
    sure about that actually. Will think about giving this to maxHeapify)

    :param arr: the array(actually a list) that holds the value to increase
    :param i: the index position of the value we want to increase.
    :param key: the value we will set for index i
    :rtype arr: list
    :rtype i: int
    :rtype key: int
    """

    if key < arr[i]: # page 164 for explanation on heap incraese key.
        return "error: new key is smaller than current key"
    arr[i] = key
    while (i > 1) and (key < arr[i]):
        arr[i], arr[key] = arr[key], arr[i]
        i = key
    return arr


def maxHeapInsert(arr, key):

    """
    Given a list arr and a key, this function will insert the key into the
    heap. The CRCS implementation of this does NOT make sure the list is
    still a heap after insertion. It was decided to call maxHeapify again here to
    generate the max heap with the new insertion.

    :param arr: the array(actually a list) that holds the value to insert
    :param key: the value we will insert into arr
    :rtype arr: list
    :rtype key: int
    """

    arr_size = len(arr)
    arr_size += 1
    arr.append(0)
    heapIncreaseKey(arr, arr_size - 1, key)
    for i in range(arr_size, -1, -1):
        maxHeapify(arr, arr_size, i)
