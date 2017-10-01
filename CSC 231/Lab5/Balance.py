# Sydney Vernatter
# January 31, 2017

from Labs.Lab5.Stack import *

text = input("Enter balanced parentheses: ")

myStack = Stack()
balanced = True
mismatch = False

for ch in text:
    if ch in "({[":
        myStack.push(ch)
    elif ch in ")}]":
        if myStack.isEmpty():
            balanced = False
            break
        left = myStack.pop()

        if left == "(" and not ch == ")":
            mismatch = True
            break
        elif left == "{" and not ch == "}":
            mismatch = True
            break
        elif left == "[" and not ch == "]":
            mismatch = True
            break

if mismatch:
    print("There were mismatched parentheses")
elif myStack.isEmpty() and balanced:
    print("Yes, they are balanced.")
else:
    print("No, they are not balanced.")
