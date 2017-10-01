# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
#deque.py


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def isPalindrome(s):
    myDeck = Deque()
    for ch in s:
        myDeck.addRear(ch)
    while myDeck.size() > 1:
        if myDeck.removeRear() != myDeck.removeFront():
            return False
    return True

text = input("Enter a palindrome: ").lower()

if isPalindrome(text):
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")
