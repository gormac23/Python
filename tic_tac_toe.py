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
        marker = input("Player1: Select 'X' or 'O' ... ").upper()
    
    # assign x or o to player 1 or player 2    
    player1 = marker
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    print("\nPlayer1 is {} and \nPlayer2 is {} \n".format(player1,player2))

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
    return board[pos] == ""


def full_board(board):
    for pos in range(1,10):
        if space_check(board,pos):
            return False
        
    return True


def player_choice(board):
    display_board(board)
    pos = 0
    # Test postion to be 1-9
    while pos not in range(1,10) or not space_check(board,pos):
        pos = int(input("Pick a postion (1-9) ... "))

    return pos


def replay():
    replay = ""

    while replay != "y":
        replay = input("Do you want to play again? [y/n]").lower()

    return replay == "y"





def main():
    print("\n{0}\nWelcome to Tic Tac Toe!\n{0}\n".format("= "*12))

    while True:
        board = ["#","","","","","","","","",""]
        
        # Ask player which marker they want and decides who to go first
        p1_marker, p2_marker = player_input()

        current_player = choose_first()
        print("{} goes first\n".format(current_player))

        # if current_player == "Player1":
        #     marker == markers[0]
        # else:
        #     # Player 2
        #     marker == markers[1]

        # Ready to play?
        play_game = input("Are you ready to play? [y/n]\n").lower()
        if play_game == "y":
            game = True
        else:
            game = False


    #### GAME PLAY ####
        while game:

            if current_player == "Player1":

                # Shows the 3x3 grid
                display_board(board)
                pos = player_choice(board)
                place_marker(board, p1_marker, pos)

                # Check if they won
                if win_check(board, p1_marker):
                    display_board(board)
                    print("PLAYER1 HAS WON!")
                    game = False
                else:
                # Check if its a tie
                    if full_board(board):
                        display_board(board)
                        print("TIE GAME!")
                        game = False
                    else:
                        current_player = "Player2"

            else:

                # Shows the 3x3 grid
                display_board(board)
                pos = player_choice(board)
                place_marker(board, p2_marker, pos)

                # Check if they won
                if win_check(board, p2_marker):
                    display_board(board)
                    print("PLAYER2 HAS WON!")
                    game = False
                else:
                # Check if its a tie
                    if full_board(board):
                        display_board(board)
                        print("TIE GAME!")
                        game = False
                    else:
                        current_player = "Player1"

        if replay():
            main()
        else:
            print("Thank you for playing!")
            break
            

        
    
    


if __name__ == '__main__':
    main()