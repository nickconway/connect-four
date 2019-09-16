from imports import *

def main():
    print("Welcome to Connect 4!")
    keepPlaying = YES

    while keepPlaying != NO:
        # Initialize variables
        row = 0
        col = 0
        turn = 0
        board, maxTurn = makeBoard()
        print()

        p2Computer = isComputer()
        print()

        # Playing against a human
        if not p2Computer:
            while not isWinner(board, row, col) and \
            not fullBoard(turn, maxTurn):
                # To be valid, the column must be a number between 1 and the
                # amount of columns, and that column must not be full

                # get the player's move, update the board and print it
                board, row, col = makeMove(board, PLAYER1)

                print()

                turn += 1

                if not isWinner(board, row, col) and \
                not fullBoard(turn, maxTurn):
                    # To be valid, the column must be a number between 1 and
                    # the amount of columns, and that column must not be full

                    # get the player's move, update the board and print it
                    board, row, col = makeMove(board, PLAYER2)

                    print()

                    turn += 1

        # Playing against a computer
        elif p2Computer:
            while not isWinner(board, row, col) and \
            not fullBoard(turn, maxTurn):
                # To be valid, the column must be a number between 1 and the
                # amount of columns, and that column must not be full

                # get the player's move, update the board and print it
                board, row, col = makeMove(board, PLAYER1)

                print()

                turn += 1

                if not isWinner(board, row, col) and \
                not fullBoard(turn, maxTurn):
                    # To be valid, the column must be a number between 1 and
                    # the amount of columns, and that column must not be full

                    # get the player's move, update the board and print it
                    board, row, col = makeCompMove(board)

                    print()

                    turn += 1

        # Print the winner, or tie
        if isWinner(board, row, col):
            print(f"Player {isWinner(board, row, col)} won!")
        else:
            print("Tie!")

        print()

        keepPlaying = input("Do you want to keep playing (y or n)? ")
        while(keepPlaying != NO and keepPlaying != YES):
            print("Must enter y or n!")
            keepPlaying = input("Do you want to keep playing (y or n)? ")
        print()


main()
