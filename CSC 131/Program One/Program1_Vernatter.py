import random

# Sydney Vernatter
# September 30, 2016
# Program One: Vault Breaker origional 
# Collaboration: stackoverflow.com (9/19 at 11:27am) Talked to some people in CSC133 class about random
# unique numbers

# Algorithm: First the computer will pick a random 4 digit code. Then the user
# will attempt to guess the code. The computer will give you hints by putting
# an = for each digit in the correct spot, a < for every digit less than the
# digit in its place, and a > for every digit greater than the digit in its place.
# If the user gets it right, they won and the game will repeat with a new number

#  Vault Code
code = 1234
codeList = [int(char) for char in str(code)]
# Flag
done = False
while not done:

    # prints code
    print("Code: ", code)
    # User guess
    guess = input("Guess the four digit code: ")
    while len(guess) != 4:
        print("Please use a four digit number for the code.")
        guess = input("Guess the four digit code: ")
        break

    # User input converts to list
    guessList = [int(char) for char in str(guess)]  # stackOverflow

    # When the guess is not exactly the code
    if guessList != codeList:
        clue = " "
        if guessList[0] == codeList[0]:
            clue += "="
        if guessList[1] == codeList[1]:
            clue += "="
        if guessList[2] == codeList[2]:
            clue += "="
        if guessList[3] == codeList[3]:
            clue += "="

        if guessList[0] < codeList[0]:
            clue += "<"
        if guessList[1] < codeList[1]:
            clue += "<"
        if guessList[2] < codeList[2]:
            clue += "<"
        if guessList[3] < codeList[3]:
            clue += "<"

        if guessList[0] > codeList[0]:
            clue += ">"
        if guessList[1] > codeList[1]:
            clue += ">"
        if guessList[2] > codeList[2]:
            clue += ">"
        if guessList[3] > codeList[3]:
            clue += ">"

        print("Nope your guess was", guess, "and your clue is:", clue)

    else:
        #play again?
        again = input("Congrats you broke the vault! Would you like to play again? (y/n): ").lower()
        while again not in ("y", "n"):
            again = input("Would you like to play again? (y/n): ").lower()
        if again == 'n':
            done = True
        print("Thanks for playing!")
