# Sydney Vernatter
# November 4, 2016
# Program Two Functions
# Create a tic tac toe board
# Collaboration statement: codingmonkeys.com; stackoverflow.com;


def displayBoard(board):
    """
    :param board: A list that contains strings that represent the current state
    of the board
    :return: nothing

    Purpose: To display the current state of the board based on the list called
    board that holds the symbols for the board. Loops through the list board
    and for each element in board that does not have a player symbol we want
    to print out the '-' symbol to show that the spot is vacant, otherwise we
    will print out the 'X' or 'Y' that has been placed in the location on the
    board.
    """

    for i in range(len(board)):
        if board[i] == "":
            print("-", end = " ")
        else:
            print(board[i], end = " ")
        if i in (2, 5, 8):
            print()
    return None


def getMove(board, locations, player):
    """

    :param board: A list that contains strings that represent the current state
    of the board
    :param locations: A list that contains the strings that represent the original
    9 locations on the board
    :param player: A string which represents the player's name.
    :return: 1 value: the move selection from the user, which will be string literal

    Purpose: To ask the correct player to enter move and then return that move
    back to main. Also does error handling to make sure that the move is
    valid by checking to see if is in locations. If the user enters a valid
    location, you should then check to make sure that there isn't already
    a game piece in that location
    """

    move = input(player + ", enter your move: ")
    if move not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "X", "O"):
        print("Please enter a number 1-9")
        move = input(player + ", enter your move: ")
    return move


def win(board, symbol):
    """

    :param board: A list that contains strings that represent the current state
    of the board
    :param symbol: A string that represents the player's coordinating symbol
    ('X' or 'O') to check and see if that player won
    :return: One boolean value called player_win: True if the player one and
    False if not

    Purpose: To determine if the current player won with the move they just
    made. There are three ways a user can win: horizontal, vertical, and
    diagonal. You should handle all three cases and return a Boolean result
    at the end of the function.
    """

    player_win = False

    if board[0] == symbol and board[1] == symbol and board[2] == symbol:
        player_win = True
    if board[3] == symbol and board[4] == symbol and board[5] == symbol:
        player_win = True
    if board[6] == symbol and board[7] == symbol and board[8] == symbol:
        player_win = True
    if board[0] == symbol and board[3] == symbol and board[6] == symbol:
        player_win = True
    if board[1] == symbol and board[4] == symbol and board[7] == symbol:
        player_win = True
    if board[2] == symbol and board[5] == symbol and board[8] == symbol:
        player_win = True
    if board[0] == symbol and board[4] == symbol and board[8] == symbol:
        player_win = True
    if board[6] == symbol and board[4] == symbol and board[2] == symbol:
        player_win = True

    return player_win


def tieGame(board):
    """

    :param board: A list that contains strings that represent the current state
    of the board
    :return: One boolean value called tie_game: true if it is a tie and false
    if it is not

    Purpose: To determine if the game has ended in a tie. This function should
    look at every element in board and if any spot is still the empty then
    there are still moves left to make therefore tie_game is false,
    otherwise it is true because there are no more moves to make
    """

    tie_game = True
    for i in range(len(board)):
        if board[i] == "":
            tie_game = False


    return tie_game
