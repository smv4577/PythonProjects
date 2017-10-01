# Sydney Vernatter
# January 31, 2017
# Decimal to binary conversion

from Labs.Lab5.Stack import *

number = int(input("Enter an integer: "))
myStack = Stack()

while number != 0:
    rem = number % 2
    myStack.push(rem)
    number //= 2

while not myStack.isEmpty():
    print(myStack.pop(), end="")
