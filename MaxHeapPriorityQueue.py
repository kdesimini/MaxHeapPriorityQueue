
"""
------------------------
Algorithms based on CRCS pseudocode
on a max heap priority queue.
------------------------
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

    O(n) with the validation of the heap property,
    O(1) if just returning the first element of the list.

    :param arr: the array that holds the max value
    :rtype arr: int
    """
    for n in range(1, len(arr)):
        if arr[n] > arr[0]:
            return "error: list must be a max heap."
    return arr[0]


def extractMax(arr):
    """
    Given an array arr, this function will extract the max value
    from the list, rendering the list with one less element. In this
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


def increaseKey(arr, i, key):
    """
    Given an array arr, index i, and value key, this function will
    increase the value at the indicated index position. If the value
    is less than the current key, we return to keep the heap property.
    Otherwise, we increase the key and call maxHeapify again to restore
    the heap property.

    :param arr: the array(actually a list) that holds the value to increase
    :param i: the index position of the value we want to increase.
    :param key: the value we will set for index i
    :rtype arr: list
    :rtype i: int
    :rtype key: int
    """
    arr_size = len(arr)
    if key < arr[i]: # page 164 for explanation on heap incraese key.
        return "error: new key is smaller than current key"
    arr[i] = key
    while (i > 1) and (key < arr[i]):
        arr[i], arr[key] = arr[key], arr[i]
        i = key
    for i in range(arr_size, -1, -1):
        maxHeapify(arr, arr_size, i)
    return arr


def insert(arr, key):
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
    increaseKey(arr, arr_size - 1, key)
    for i in range(arr_size, -1, -1):
        maxHeapify(arr, arr_size, i)
