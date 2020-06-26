# plays the game x amount fo times

# ----- GLOBAL VARIABLES -----

# board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# if game is still going#
game_still_going = True

# Who won? Or tie?
winner = None

# Whose turn it is
current_player = "x"


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


# play a game of tic-tac-toe
def play_game():
    display_board()  # displays initial board

    # while the game is still going
    while game_still_going:
        # handle a single turn of an arbitrary player
        handle_turn(current_player)
        # check is the game has ended
        check_if_game_over()
        # Flip to the other player
        flip_player()

        # The game has ended
    if winner == "x" or winner == "o":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# handle a single turn of an arbitrary player
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose  a position from 1 to 9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid Input. Choose  a position from 1 to 9: ")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("You can not go there, try again")
    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # set up globals
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    # get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    global game_still_going
    # check if any of the rows have the same value but nor dashes
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner (x or o)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    global game_still_going
    # check if any of the columns have the same value but nor dashes
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner (x or o)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    global game_still_going
    # check if any of the rows have the same value but nor dashes
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    # if
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # return the winner (x or o)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    # global variables we need
    global current_player
    # if current player was x, changes to o
    if current_player == "x":
        current_player = "o"
    # if current player wa so, changes to x
    elif current_player == "o":
        current_player = "x"
    return


play_game()

again = input("would you like to play again?")
if again == "yes":
    while again == "yes":
        # plays the game x amount fo times

        # ----- GLOBAL VARIABLES -----

        # board
        board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

        # if game is still going#
        game_still_going = True

        # Who won? Or tie?
        winner = None

        # Whose turn it is
        current_player = "x"


        def display_board():
            print(board[0] + "|" + board[1] + "|" + board[2])
            print(board[3] + "|" + board[4] + "|" + board[5])
            print(board[6] + "|" + board[7] + "|" + board[8])


        # play a game of tic-tac-toe
        def play_game():
            display_board()  # displays initial board

            # while the game is still going
            while game_still_going:
                # handle a single turn of an arbitrary player
                handle_turn(current_player)
                # check is the game has ended
                check_if_game_over()
                # Flip to the other player
                flip_player()

                # The game has ended
            if winner == "x" or winner == "o":
                print(winner + " won.")
            elif winner == None:
                print("Tie.")


        # handle a single turn of an arbitrary player
        def handle_turn(player):
            print(player + "'s turn.")
            position = input("Choose  a position from 1 to 9: ")
            valid = False
            while not valid:
                while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    position = input("Invalid Input. Choose  a position from 1 to 9: ")
                position = int(position) - 1
                if board[position] == "-":
                    valid = True
                else:
                    print("You can not go there, try again")
            board[position] = player
            display_board()


        def check_if_game_over():
            check_for_winner()
            check_if_tie()


        def check_for_winner():

            # set up globals
            global winner

            # check rows
            row_winner = check_rows()
            # check columns
            column_winner = check_columns()
            # check diagonals
            diagonal_winner = check_diagonals()

            # get the winner
            if row_winner:
                winner = row_winner
            elif column_winner:
                winner = column_winner
            elif diagonal_winner:
                winner = diagonal_winner
            else:
                winner = None
            return


        def check_rows():
            global game_still_going
            # check if any of the rows have the same value but nor dashes
            row_1 = board[0] == board[1] == board[2] != "-"
            row_2 = board[3] == board[4] == board[5] != "-"
            row_3 = board[6] == board[7] == board[8] != "-"
            # ifw
            if row_1 or row_2 or row_3:
                game_still_going = False
            # return the winner (x or o)
            if row_1:
                return board[0]
            elif row_2:
                return board[3]
            elif row_3:
                return board[6]
            return


        def check_columns():
            global game_still_going
            # check if any of the columns have the same value but nor dashes
            column_1 = board[0] == board[3] == board[6] != "-"
            column_2 = board[1] == board[4] == board[7] != "-"
            column_3 = board[2] == board[5] == board[8] != "-"
            # if
            if column_1 or column_2 or column_3:
                game_still_going = False
            # return the winner (x or o)
            if column_1:
                return board[0]
            elif column_2:
                return board[1]
            elif column_3:
                return board[2]
            return


        def check_diagonals():
            global game_still_going
            # check if any of the rows have the same value but nor dashes
            diagonal_1 = board[0] == board[4] == board[8] != "-"
            diagonal_2 = board[6] == board[4] == board[2] != "-"
            # if
            if diagonal_1 or diagonal_2:
                game_still_going = False
            # return the winner (x or o)
            if diagonal_1:
                return board[0]
            elif diagonal_2:
                return board[6]
            return


        def check_if_tie():
            global game_still_going
            if "-" not in board:
                game_still_going = False
            return


        def flip_player():
            # global variables we need
            global current_player
            # if current player was x, changes to o
            if current_player == "x":
                current_player = "o"
            # if current player wa so, changes to x
            elif current_player == "o":
                current_player = "x"
            return


        play_game()
        again = input("would you like to play again?")
        if again == "yes":
            print("Ok, here you go!")
        elif again == "no":
            print("Ok, see you next time")
        else:
            print("invalid input")
elif again == "no":
    print("Ok, see you next time")
else:
    print("invalid input")

file = open("tic-tac-toe score", "w")
file.write(winner, "\n")
file.close()
