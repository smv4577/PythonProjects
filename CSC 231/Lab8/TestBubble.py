import random
import time
from Labs.Lab8.SortingAlgorithms import *
from Labs.Lab8.CountingSort import *
from Labs.Lab8.MergeSort import *

n = 10
print("n \t CountSort \t BubbleSort2 \t MergeSort")
for n in range(100, 1001, 50):
    myList = []
    for i in range(n):
        myList.append(random.randint(0, 100))

    myList2 = myList.copy()
    myList3 = myList.copy()

    start = time.clock()
    countSort(myList, 100)
    end = time.clock()

    start2 = time.clock()
    bubbleSort2(myList2)
    end2 = time.clock()

    start3 = time.clock()
    mergeSort(myList3)
    end3 = time.clock()

    print(n, "\t", end-start, "\t", end2-start2, "\t", end3-start3)
