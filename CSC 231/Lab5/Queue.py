# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        s = ""
        for elements in self.items:
            s += elements + " "
        return s

myQueue = Queue()
myQueue.enqueue("Dog")
print(myQueue.size())
myQueue.enqueue("Elephant")
myQueue.enqueue("Cat")

print(myQueue)

myQueue.dequeue()
print(myQueue)
myQueue.dequeue()
print(myQueue)
myQueue.dequeue()
print(myQueue)
