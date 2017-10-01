# Sydney Vernatter
# November 4, 2016
# Program Two Main
# Create a tic tac toe board
# Algorithm: Set up board. Ask players for their name. Ask a player for their move. Check whether move is valid.
# Replace empty string with their symbol. Switch players. Continue until someone wins or the game ends.
# Collaboration statement: John Cole; Professor Pence;

import MyFunctionsEC
import turtle


def main():
    turtle.setup(500, 500)
    window = turtle.Screen()
    window.title("Tic Tac Toe")
    window.bgpic("square.gif")
    MyFunctionsEC.drawBoard(turtle)

    board = ["", "", "", "", "", "", "", "", ""]
    locations = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    gameOver = False
    print("This program will allow two players to play the game of tic-tac-toe")
    print("Player 1 has 'X' and player 2 has 'O'.")
    playerOne = input("Enter the name of player 1: ")
    playerTwo = input("Enter the name of player 2: ")
    print("Enter your mark using the board positions shown below.")

    MyFunctionsEC.displayBoard(locations)

    player = playerOne
    playerSymbol = "X"
    symbol = playerSymbol
    playerOnePic = "playerone_x.gif"
    playerTwoPic = "playertwo_o.gif"
    window.register_shape(playerOnePic)
    window.register_shape(playerTwoPic)
    window.register_shape("tiegame.gif")
    window.register_shape("winner.gif")
    playerPic = playerOnePic


    while gameOver is False:
        move = MyFunctionsEC.getMove(board, locations, player)
        board[int(move)-1] = playerSymbol
        MyFunctionsEC.stampPiece(turtle, playerPic, move, window)
        MyFunctionsEC.displayBoard(board)
        player_win = MyFunctionsEC.win(board, symbol)
        if player_win == True:
            gameOver = True
        if player_win == False:
            tie_game = MyFunctionsEC.tieGame(board)
            if tie_game == True:
                gameOver = True
        if player == playerOne:
            playerPic = playerTwoPic
            player = playerTwo
            playerSymbol = "O"
        else:
            playerPic = playerOnePic
            player = playerOne
            playerSymbol = "X"

    if gameOver is True:
        if tie_game is True:
            print("Tie game! Thanks for playing")
            tiegame = turtle.getturtle()
            tiegame.shape("tiegame.gif")
            tiegame.showturtle()
            turtle.done()

        else:
            print("Thanks for playing!", player, "you win!")
            wingame = turtle.getturtle()
            wingame.shape("winner.gif")
            wingame.showturtle()
            turtle.done()
        
main()
