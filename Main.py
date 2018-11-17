import MaxHeapPriorityQueue
import unittest


class Main:
    a = [5, 7, 9, 1, 3, 13, 21, 43, 2, 42, 12, 8, 77, 65, 23]

    mh = MaxHeapPriorityQueue.buildMaxHeap(a)
    # print(str(mh) + "max heap: ")
    maxV = MaxHeapPriorityQueue.extractMax(mh)
    print(str(maxV) + "Extracted max value: ")
    print(str(mh) + "heap after extraction: \n")

    # print(MaxHeapPriorityQueue.heapIncreaseKey(mh, 4, 100))
    # print(MaxHeapPriorityQueue.buildMaxHeap(mh))
    # print(mh)
    # print(SimpleDataStructure.heapIncreaseKey(mh, 7, 69))
    # print(SimpleDataStructure.heapIncreaseKey(mh, 9, 1))

    # print("\n")

    # MaxHeapPriorityQueue.maxHeapInsert(mh, 26)
    # print(mh)

    # a = [2, 3, 1, 6, 7]
    # MaxHeapPriorityQueue.maxHeapify(a, 5, 1)
    # MaxHeapPriorityQueue.maxHeapify(a, 5, 0)
    # print(a)


class Tests(unittest.TestCase):
    """
    ------------------------
    TEST maxHeapify
    ------------------------
    """

    def testmaxHeapify1(self):
        """Here, we have a sample dataset a.
        This dataset is running through 1
        procedure of maxHeapify to show that it's
        functioning correctly"""

        a = [2, 3, 1, 6, 7]
        MaxHeapPriorityQueue.maxHeapify(a, 5, 1)
        self.assertEqual([2, 7, 1, 6, 3], a)

    def testmaxHeapify2(self):
        a = [2, 3, 1, 6, 7]
        MaxHeapPriorityQueue.maxHeapify(a, 5, 1)
        MaxHeapPriorityQueue.maxHeapify(a, 5, 0)
        self.assertEqual([7, 6, 1, 2, 3], a)

    """
    ------------------------
    TEST buildMaxHeap
    
    ------------------------
    """

    def testBuildMaxHeapNormal(self):
        """This test will test for a complete max heap"""

        unorderedList = [5, 7, 9, 1, 3, 13, 21, 43, 2, 42, 12, 8, 77, 65, 23]
        maxHeap = [77, 43, 65, 7, 42, 13, 23, 1, 2, 3, 12, 8, 9, 21, 5]
        MaxHeapPriorityQueue.buildMaxHeap(unorderedList)
        self.assertEqual(maxHeap, unorderedList)

    def testBuildMaxHeapNormal2(self):
        """This test will test for a complete max heap"""

        unorderedList = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
        maxHeap = [90, 36, 26, 25, 19, 17, 1, 7, 3, 2]
        MaxHeapPriorityQueue.buildMaxHeap(unorderedList)
        self.assertEqual(maxHeap, unorderedList)

    def testBuildMaxHeapClassroomExercise(self):
        """This test will test for a complete max heap
        proven by the fact we used this example in class"""

        unorderedList = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        MaxHeapPriorityQueue.buildMaxHeap(unorderedList)
        answer = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        self.assertEqual(answer, unorderedList)

    def testBuildMaxHeapNotEqual(self):
        """The value 100 in the heap breaks the heap prop."""

        unorderedList = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
        notMaxHeap = [90, 100, 26, 25, 19, 17, 1, 7, 3, 2]
        MaxHeapPriorityQueue.buildMaxHeap(unorderedList)
        self.assertNotEqual(notMaxHeap, unorderedList)

    """
    
    ------------------------
    TEST Maximum
    ------------------------
    """

    def testGetMaximum(self):
        """This test will verify that it pulls the correct max value"""

        unorderedList = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
        MaxHeapPriorityQueue.buildMaxHeap(unorderedList)
        largestValue = 90
        maxValue = MaxHeapPriorityQueue.getMaximum(unorderedList)
        self.assertEqual(largestValue, maxValue)

    def testGetMaximumNotEqual(self):
        """The array is not a heap in this test
         so the first value is 2"""

        unorderedList = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
        largestValue = 90
        maxValue = MaxHeapPriorityQueue.getMaximum(unorderedList)
        self.assertNotEqual(largestValue, maxValue)

    """
    ------------------------
    TEST Extract Maximum
    ------------------------
    """

    def testHeapExtractMax(self):
        """This test will verify that the resulting array
        is equal to a correct array after the element has
        been extracted"""

        unorderedList = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
        mh = MaxHeapPriorityQueue.buildMaxHeap(unorderedList)
        MaxHeapPriorityQueue.extractMax(mh)
        expected = [36, 25, 26, 7, 19, 17, 1, 2, 3]
        self.assertEqual(expected, mh)

    def testHeapExtractMaxLargerList(self):
        """This test will verify that the resulting array
        is equal to a correct array after the element has
        been extracted"""

        unorderedList = [5, 7, 9, 1, 3, 13, 21, 43, 2, 42, 12, 8, 77, 65, 23]
        mh = MaxHeapPriorityQueue.buildMaxHeap(unorderedList)
        MaxHeapPriorityQueue.extractMax(mh)
        expected = [65, 43, 23, 7, 42, 13, 21, 1, 2, 3, 12, 8, 9, 5]
        self.assertEqual(expected, mh)

    """
    ------------------------
    TEST HeapIncreaseKey
    ------------------------
    """

    def testHeapIncreaseKey(self):
        """This test will verify that the resulting array
        is equal to a correct array after the element
        value has been increased."""

        unorderedList = [5, 7, 9, 1, 3, 13, 21, 43, 2, 42, 12, 8, 77, 65, 23]
        mh = MaxHeapPriorityQueue.buildMaxHeap(unorderedList)
        MaxHeapPriorityQueue.heapIncreaseKey(mh, 4, 100)
        expected = [77, 43, 65, 7, 100, 13, 23, 1, 2, 3, 12, 8, 9, 21, 5]
        self.assertEqual(expected, mh)

    """
    ------------------------
    TEST Insert
    ------------------------
    """

    def testMaxHeapInsert(self):
        """This test verifies that the key is
        inserted into the heap and then maxHeapify
        is called to ensure the heap property is held"""

        unorderedList = [5, 7, 9, 1, 3, 13, 21, 43, 2, 42, 12, 8, 77, 65, 23]
        mh = MaxHeapPriorityQueue.buildMaxHeap(unorderedList)
        MaxHeapPriorityQueue.maxHeapInsert(mh, 45)
        expected = [77, 45, 65, 43, 42, 13, 23, 7, 2, 3, 12, 8, 9, 21, 5, 1]
        self.assertEqual(expected, mh)


def main():
    unittest.main()


if __name__ == '__main__':
    main()