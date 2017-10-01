# Sydney Vernatter
# November 4, 2016
# Program Two Main
# Create a tic tac toe board
# Algorithm: Ask a player for their move. Check whether move is valid. Replace empty string
# with their symbol.Switch players. Continue until someone wins or the game ends. Ask if they
# want to play again
# Collaboration statement: John Cole; Professor Pence;

import MyFunctions


def main():
    board = ["", "", "", "", "", "", "", "", ""]
    locations = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    gameOver = False
    print("This program will allow two players to play the game of tic-tac-toe")
    print("Player 1 has 'X' and player 2 has 'O'.")
    playerOne = input("Enter the name of player 1: ")
    playerTwo = input("Enter the name of player 2: ")
    print("Enter your mark using the board positions shown below.")
    MyFunctions.displayBoard(locations)

    player = playerOne
    playerSymbol = "X"
    symbol = playerSymbol

    while gameOver is False:
        move = MyFunctions.getMove(board, locations, player)
        board[int(move)-1] = playerSymbol

        MyFunctions.displayBoard(board)
        player_win = MyFunctions.win(board, symbol)
        if player_win == True:
            gameOver = True
        if player_win == False:
            tie_game = MyFunctions.tieGame(board)
            if tie_game == True:
                gameOver = True
        if player == playerOne:
            player = playerTwo
            playerSymbol = "O"
        else:
            player = playerOne
            playerSymbol = "X"

    if gameOver is True:
        if tie_game is True:
            print("Tie game! Thanks for playing")
        else:
            print("Thanks for playing!", player, "you win!")
        
main()
