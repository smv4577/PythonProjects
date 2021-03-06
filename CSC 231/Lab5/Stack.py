# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

# s = Stack()
# print(s)
# print(s.isEmpty())
# print("Length: ", s.size())
# s.push("dog")
# print(s.isEmpty())
# print("Length: ", s.size())
# t = s.peek()
# print("Top of stack: ", t)
# x = s.pop()
# print("x: ", x)
# print("Length: ", s.size())

