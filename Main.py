
"""
------------------------------------
Algorithms based on CRCS pseudocode
on a max heap priority queue.
------------------------------------
"""

import MaxHeapPriorityQueue
import unittest


class Main:
    a = [5, 7, 9, 1, 3, 13, 21, 43, 2, 42, 12, 8, 77, 65, 23]
    print(str(a) + " - Starting List\n")

    mh = MaxHeapPriorityQueue.buildMaxHeap(a)
    print(str(mh) + " - Max Heap\n\n")

    print("Now lets extract the max value")
    maxV = MaxHeapPriorityQueue.extractMax(mh)
    print(str(maxV) + " - Extracted max value ")
    print(str(mh) + " - Max heap after extraction\n\n")

    a = [5, 7, 9, 1, 3, 13, 21, 43, 2, 42, 12, 8, 77, 65, 23]
    mh = MaxHeapPriorityQueue.buildMaxHeap(a)

    print("Now lets increase index 4 to 100 and then call build max heap again")
    print(MaxHeapPriorityQueue.increaseKey(mh, 4, 100))
    MaxHeapPriorityQueue.buildMaxHeap(mh)
    print(str(mh) + " - Max heap after index 4 was changed and heap was restored\n\n")

    a = [5, 7, 9, 1, 3, 13, 21, 43, 2, 42, 12, 8, 77, 65, 23]
    mh = MaxHeapPriorityQueue.buildMaxHeap(a)

    print("Now lets increase index 9 to 1")
    print(MaxHeapPriorityQueue.increaseKey(mh, 9, 1))
    print("This error occurs because the key is smaller than current key\n\n")

    print("We will now insert 26 into the heap")
    MaxHeapPriorityQueue.insert(mh, 26)
    print(str(mh) + "\n\n\n")

    a = [21, 7, 9, 1, 3, 13, 21, 43, 2, 42, 12, 8, 77, 65, 23]
    print(a)
    print(MaxHeapPriorityQueue.getMaximum(a))
    print(a)



class Tests(unittest.TestCase):
    """
    ------------------------
    TEST maxHeapify
    ------------------------
    """

    def testmaxHeapify1(self):
        """Here, we have a sample unorderedlist.
        This list is running through 1
        procedure of maxHeapify to show that it's
        functioning correctly"""

        theList = [2, 3, 1, 6, 7]
        MaxHeapPriorityQueue.maxHeapify(theList, 5, 1)
        self.assertEqual([2, 7, 1, 6, 3], theList)

    def testmaxHeapify2(self):
        """Here the unordered list is getting
        maxheapified at 1 and then 0. """

        theList = [2, 3, 1, 6, 7]
        MaxHeapPriorityQueue.maxHeapify(theList, 5, 1)
        MaxHeapPriorityQueue.maxHeapify(theList, 5, 0)
        self.assertEqual([7, 6, 1, 2, 3], theList)

    """
    ------------------------
    TEST buildMaxHeap
    ------------------------
    """

    def testBuildMaxHeapNormal(self):
        """This test will test for a complete max heap"""

        theList = [5, 7, 9, 1, 3, 13, 21, 43, 2, 42, 12, 8, 77, 65, 23]
        maxHeap = [77, 43, 65, 7, 42, 13, 23, 1, 2, 3, 12, 8, 9, 21, 5]
        MaxHeapPriorityQueue.buildMaxHeap(theList)
        self.assertEqual(maxHeap, theList)

    def testBuildMaxHeapNormal2(self):
        """This test will test for a complete max heap"""

        theList = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
        maxHeap = [90, 36, 26, 25, 19, 17, 1, 7, 3, 2]
        MaxHeapPriorityQueue.buildMaxHeap(theList)
        self.assertEqual(maxHeap, theList)

    def testBuildMaxHeapClassroomExercise(self):
        """This test will test for a complete max heap
        proven by the fact we used this example in class"""

        theList = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        MaxHeapPriorityQueue.buildMaxHeap(theList)
        expected = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        self.assertEqual(expected, theList)

    def testBuildMaxHeapNotEqual(self):
        """The value 100 in the heap breaks the heap property"""

        theList = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
        notMaxHeap = [90, 100, 26, 25, 19, 17, 1, 7, 3, 2]
        MaxHeapPriorityQueue.buildMaxHeap(theList)
        self.assertNotEqual(notMaxHeap, theList)

    """
    ------------------------
    TEST Maximum
    ------------------------
    """

    def testGetMaximum(self):
        """This test will verify that it pulls the correct max value"""

        theList = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
        MaxHeapPriorityQueue.buildMaxHeap(theList)
        expected = 90
        maxValue = MaxHeapPriorityQueue.getMaximum(theList)
        self.assertEqual(expected, maxValue)

    def testGetMaximumNotEqual(self):
        """The array is not a heap in this test
         so the first value is 2"""

        theList = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
        expected = 90
        maxValue = MaxHeapPriorityQueue.getMaximum(theList)
        self.assertNotEqual(expected, maxValue)

    def tesIsArrayIntact(self):
        """Ensuring no values have been removed or changed
        from the list"""

        theList = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
        expected = [36, 26, 25, 19, 17, 1, 7, 3, 2]
        maxValue = MaxHeapPriorityQueue.getMaximum(theList)
        self.assertEqual(expected, theList)

    """
    ------------------------
    TEST Extract Maximum
    ------------------------
    """

    def testHeapExtractMax(self):
        """This test will verify that the resulting array
        is equal to a correct array after the element has
        been extracted"""

        theList = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
        MaxHeapPriorityQueue.buildMaxHeap(theList)
        MaxHeapPriorityQueue.extractMax(theList)
        expected = [36, 25, 26, 7, 19, 17, 1, 2, 3]
        self.assertEqual(expected, theList)

    def testHeapExtractMaxLargerList(self):
        """This test will verify that the resulting array
        is equal to a correct array after the element has
        been extracted"""

        theList = [5, 7, 9, 1, 3, 13, 21, 43, 2, 42, 12, 8, 77, 65, 23]
        MaxHeapPriorityQueue.buildMaxHeap(theList)
        MaxHeapPriorityQueue.extractMax(theList)
        expected = [65, 43, 23, 7, 42, 13, 21, 1, 2, 3, 12, 8, 9, 5]
        self.assertEqual(expected, theList)

    """
    ------------------------
    TEST HeapIncreaseKey
    ------------------------
    """

    def testHeapIncreaseKey(self):
        """This test will verify that the resulting array
        is not a max heap and it will fail. The resulting 100
         breaks the heap property."""

        theList = [5, 7, 9, 1, 3, 13, 21, 43, 2, 42, 12, 8, 77, 65, 23]
        MaxHeapPriorityQueue.buildMaxHeap(theList)
        MaxHeapPriorityQueue.increaseKey(theList, 4, 100)
        expected = [77, 43, 65, 7, 100, 13, 23, 1, 2, 3, 12, 8, 9, 21, 5]
        self.assertNotEqual(expected, theList)

    def testHeapIncreaseKeyHoldHeapProperty(self):
        """This test will verify that the resulting array
        is a max heap after a key is increased, thus maintaining
        the heap property."""

        theList = [5, 7, 9, 1, 3, 13, 21, 43, 2, 42, 12, 8, 77, 65, 23]
        MaxHeapPriorityQueue.buildMaxHeap(theList)
        MaxHeapPriorityQueue.increaseKey(theList, 4, 100)
        expected = [100, 77, 65, 7, 43, 13, 23, 1, 2, 3, 12, 8, 9, 21, 5]
        self.assertEqual(expected, theList)

    """
    ------------------------
    TEST Insert
    ------------------------
    """

    def testMaxHeapInsert(self):
        """This test verifies that the key is
        inserted into the heap and then maxHeapify
        is called to ensure the heap property is held"""

        theList = [5, 7, 9, 1, 3, 13, 21, 43, 2, 42, 12, 8, 77, 65, 23]
        MaxHeapPriorityQueue.buildMaxHeap(theList)
        MaxHeapPriorityQueue.insert(theList, 45)
        expected = [77, 45, 65, 43, 42, 13, 23, 7, 2, 3, 12, 8, 9, 21, 5, 1]
        self.assertEqual(expected, theList)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
