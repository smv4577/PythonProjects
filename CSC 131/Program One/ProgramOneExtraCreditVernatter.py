import random

# Sydney Vernatter
# September 30, 2016
# Program One: Vault Breaker
# Collaboration: stackoverflow.com (9/19 at 11:27am) Talked to some people in CSC133 class about random unique numbers

# Algorithm: First the computer will pick a random 4 digit code. Then the user
# will attempt to guess the code. The computer will give you hints by putting
# an = for each digit in the correct spot, a < for every digit less than the
# digit in its place, and a > for every digit greater than the digit in its place.
# If the user gets it right, they won and the game will repeat with a new number

#  Vault Code

numbersList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(numbersList)
codeList = numbersList[0:4]
# code = random.randint(1000, 9999)
# numbersList = [int(char) for char in str(code)]

# Flag
done = False
while not done:

    print("Code: ", codeList)
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
        else:
            while guessList[0] != codeList[0]:
                if guessList[0] < codeList[0]:
                    clue += "<"
                elif guessList[0] > codeList[0]:
                    clue += ">"
                break
        if guessList[1] == codeList[1]:
            clue += "="
        else:
            while guessList[1] != codeList[1]:
                if guessList[1] < codeList[1]:
                    clue += "<"
                elif guessList[1] > codeList[1]:
                    clue += ">"
                break
        if guessList[2] == codeList[2]:
            clue += "="
        else:
            while guessList[2] != codeList[2]:
                if guessList[2] < codeList[2]:
                    clue += "<"
                elif guessList[2] > codeList[2]:
                    clue += ">"
                break
        if guessList[3] == codeList[3]:
            clue += "="
        else:
            while guessList[3] != codeList[3]:
                if guessList[3] < codeList[3]:
                    clue += "<"
                elif guessList[3] > codeList[3]:
                    clue += ">"
                break

        print("Nope your guess was", guess, "and your clue is:", clue)

    else:
        #play again?
        again = input("Congrats you broke the vault! Would you like to play again? (y/n): ").lower()
        while again not in ("y", "n"):
            again = input("Would you like to play again? (y/n): ").lower()
        if again == 'n':
            done = True
        print("Thanks for playing!")
