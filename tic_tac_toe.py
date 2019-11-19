import os
import random

def display_board(board):
    # clears board after each move
    # Makes the board look like it updates    
    os.system("clear")

    # Draw the 3x3 board
    print(" {0:^3}-{0:^3}-{0:^3}".format("---"))
    print(" {:^3}|{:^3}|{:^3}".format(board[7],board[8],board[9]))
    print(" {0:^3}|{0:^3}|{0:^3}".format("-"))
    print(" {:^3}|{:^3}|{:^3}".format(board[4],board[5],board[6]))
    print(" {0:^3}|{0:^3}|{0:^3}".format("-"))
    print(" {:^3}|{:^3}|{:^3}".format(board[1],board[2],board[3]))
    print(" {0:^3}-{0:^3}-{0:^3}".format("---"))
    print("\n")


def player_input():
    marker = ""
    # test the input to make sure either x or o    
    while marker != "X" and marker != "O":
        marker = input("Player 1: Select 'X' or 'O' ... ").upper()
    
    # assign x or o to player 1 or player 2    
    player1 = marker
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    # outputs a tuple
    return(player1,player2)


def place_marker(board, marker, pos):
    board[pos] = marker
    return board


def win_check(board, marker):
    win = False

    # All bottom row equal
    if board[1] == marker and board[2] == marker and board[3] == marker:
        win = True
    # All middle row equal
    elif  board[4] == marker and board[5] == marker and board[6] == marker:
        win = True
    # All top row equal
    elif  board[7] == marker and board[8] == marker and board[9] == marker:
        win = True

    # All left column equal
    elif  board[1] == marker and board[4] == marker and board[7] == marker:
        win = True
    # All middle column equal
    elif  board[2] == marker and board[5] == marker and board[8] == marker:
        win = True
    # All right colum equal
    elif  board[3] == marker and board[6] == marker and board[9] == marker:
        win = True

    # Diagonal 1,5,9
    elif  board[1] == marker and board[5] == marker and board[9] == marker:
        win = True
    # Diagonal 3,5,7
    elif  board[3] == marker and board[5] == marker and board[7] == marker:
        win = True
    else:
        win = False

    return win


def choose_first():
    first = random.randint(1,2)
    if first == 1:
        return "Player1"
    else:
        return "Player2"


def space_check(board, pos):
    if board[pos] == "":
        return True
    else:
        return False


def full_board(board):
    isFull = False
    for pos in board:
        if board[pos] != "":
            isFull = True
        else:
            isFull = False

    return isFull


def player_choice(board):
    pos = 0
    # Test postion to be 1-9
    while pos not in range(1,9):
        pos = input("Plick a postion (1-9) ... ")

    # Check to see if the valid position is free
    if space_check(board,pos):
        return pos




def replay():
    replay = ""

    while replay != "y" or replay != "n":
        replay = input("Do you want to play again? [y/n]").lower()

    if replay == "y":
        return True
    else:
        return False