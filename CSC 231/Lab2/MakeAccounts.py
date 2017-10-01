import random
from BankAccount import *

"""
Create some random bank accounts.
"""

outfile = open("accounts.txt", "w")

firstNameFile = open("FirstNames.txt", "r")
firstNames = []
for line in firstNameFile:
    firstNames.append(line.strip())

lastNameFile = open("LastNames.txt", "r")
lastNames = []
for line in lastNameFile:
    lastNames.append(line.strip())

for i in range(100):
    r1 = random.randint(0, len(firstNames) - 1)
    first = firstNames[r1]
    r2 = random.randint(0, len(lastNames) - 1)
    last = lastNames[r2]
    acct = BankAccount(first, last, random.randint(1, 10000))
    interest = acct.calculateInterest()
    print("The interest is: ", interest)
    print(acct)
    outfile.write(str(acct) + "\n")

print("Done!")
