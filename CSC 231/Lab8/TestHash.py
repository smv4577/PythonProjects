import random
import time
from Labs.Lab8.Hashtable import *

n = 10
for n in range(10000, 100001, 10000):
    start = time.clock()
    myTable = HashTable()
    for i in range(n):
        myTable.put(random.randint(0, 1000000), random.randint(0, 1000000))
    end = time.clock()


    start2 = time.clock()
    myDict = {}
    for i in range(n):
        myDict[random.randint(0, 1000000)] = random.randint(0, 1000000)
    end2 = time.clock()

    print(n, "\t", end - start, "\t", end2 - start2)