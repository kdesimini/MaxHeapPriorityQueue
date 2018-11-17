# MaxHeapPriorityQueue
A python implementation of a max heap based priority queue. To run this, use terminal/cmd to navigate to the folder where the script lives. Then, execute

```shell
python3 Main.py
```
This will run the Main test class on the MaxHeapPriorityQueue class. You can trash the Main.py file and just utilize the MaxHeapPriorityQueue class if you want of course. Enjoy :)

```python
a = [5, 7, 9, 1, 3, 13, 21, 43, 2, 42, 12, 8, 77, 65, 23]
print(str(a) + " - Starting List\n")

mh = MaxHeapPriorityQueue.buildMaxHeap(a)
print(str(mh) + " - Max Heap\n\n")

print("Now lets extract the max value")
maxV = MaxHeapPriorityQueue.extractMax(mh)
print(str(maxV) + " - Extracted max value ")
print(str(mh) + " - Max heap after extraction\n\n")

print("Now lets increase index 4 to 100 and then call build max heap again")
print(MaxHeapPriorityQueue.heapIncreaseKey(mh, 4, 100))
MaxHeapPriorityQueue.buildMaxHeap(mh)
print(str(mh) + " - Max heap after index 4 was changed and heap was restored\n\n")

print("Now lets increase index 9 to 1")
print(MaxHeapPriorityQueue.heapIncreaseKey(mh, 9, 1))
print("This error occurs because the key is smaller than current key\n\n")

print("We will now insert 26 into the heap")
MaxHeapPriorityQueue.maxHeapInsert(mh, 26)
print(str(mh) + "\n\n\n")
```

# Output

```
[5, 7, 9, 1, 3, 13, 21, 43, 2, 42, 12, 8, 77, 65, 23] - Starting List

[77, 43, 65, 7, 42, 13, 23, 1, 2, 3, 12, 8, 9, 21, 5] - Max Heap


Now lets extract the max value
77 - Extracted max value
[65, 43, 23, 7, 42, 13, 21, 1, 2, 3, 12, 8, 9, 5] - Max heap after extraction


Now lets increase index 4 to 100 and then call build max heap again
[65, 43, 23, 7, 100, 13, 21, 1, 2, 3, 12, 8, 9, 5]
[100, 65, 23, 7, 43, 13, 21, 1, 2, 3, 12, 8, 9, 5] - Max heap after index 4 was changed and heap was restored


Now lets increase index 9 to 1
error: new key is smaller than current key
This error occurs because the key is smaller than current key


We will now insert 26 into the heap
[100, 65, 26, 7, 43, 13, 23, 1, 2, 3, 12, 8, 9, 5, 21]
```
