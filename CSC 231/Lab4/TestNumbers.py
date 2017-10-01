# Sydney Vernatter
# January 24, 2017
import random
import time


def find(myList, target):
    for x in myList:
        if x == target:
            return True
    return False

n = 100
for n in range(50000, 1000000, 50000):
    numbers = []

    for i in range(n):
        num = random.randint(0, 2*n)
        numbers.append(num)

    start = time.clock()
    answer = find(numbers, -1)
    end = time.clock()

    print(n, "\t", end - start)
