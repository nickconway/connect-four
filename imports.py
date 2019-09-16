import random

# Player marks
BLANK = "_"
PLAYER1 = "X"
PLAYER2 = "O"

# Column constants
MIN_VALUE = 5
MIN_COLUMN = 1

# Input constants
NO = "n"
YES = "y"


# prints out the current board
# Input: board
# Output: None
def printBoard(board):
    for row in board:
        row_ = 0
        count = 0
        for col in row:
            if count < len(board[row_]) - 1:
                print(col, end=" ")
            else:
                print(col)
            count += 1
        row_ += 1


# creates the initial unfilled board with the specified width and height
# Input: None
# Output: blank board with a width and height the user specified, the max
# number of turns
def makeBoard():
    board = []
    height = 0
    while height < MIN_VALUE:
        height = int(input("How many rows will the board have? "))
        if(height < MIN_VALUE):
            print("Rows must be greater than 5!")

    width = 0
    while width < MIN_VALUE:
        width = int(input("How many columns will the board have? "))
        if(width < MIN_VALUE):
            print("Columns must be greater than 5!")

    row = []
    for count in range(width):
        row.append("_")

    for count in range(height):
        board.append(row[:])

    maxTurns = width * height
    printBoard(board)

    return board, maxTurns


# asks the user if player 2 is ai or human
# Input: None
# Output: if player 2 is a computer (true or false)
def isComputer():
    # Get the answer from the player and validate
    answer = input("Is player 2 a computer (y or n)? ")
    while(answer != NO and answer != YES):
        print("Must enter y or n!")
        answer = input("Is player 2 a computer (y or n)? ")

    return True if answer == "y" else False


# gets the players move and updates the board put piece in, update the board
# Input: the board, the player mark
# Output: the new board, the place where the piece went
def makeMove(board, player):
    # Check if the column is full
    validMove = False
    while(not validMove):
        playerNum = 1 if player == PLAYER1 else 2
        rowFilled = False
        row = -1
        col = int(input(f"Player {playerNum}'s turn. What column do you want " +
                        f"to place your piece in (1 - {len(board[0])})? ")) - 1
        while(col < 0 or col >= len(board[0])):
            print()
            print("Invalid column. Try again!")
            print()
            col = int(input(f"Player {playerNum}'s turn. What column do you " +
                            f"want to place your piece in (1 - " + 
                            f"{len(board[0])})? ")) - 1
        print()

        while(not rowFilled):
            if(row < -(len(board))):
                print("That column is full! Try again.")
                rowFilled = True
                validMove = False
            elif(board[row][col] == BLANK):
                board[row][col] = player
                rowFilled = True
                validMove = True

            row -= 1

    row += 1

    printBoard(board)

    return board, row, col


# the computer first checks if there are any winning moves, then it checks if
# it can block player 1 at all, it then checks if it can place a piece next to
# an existing piece, and lastly, it places its piece in a random column if none
# of the above can be done
# Input: the board
# Output: new board
def makeCompMove(board):
    # Check if the column is full
    validMove = False
    while(not validMove):
        rowFilled = False
        row = -1
        col = random.randint(1, len(board) - 1)

        while(not rowFilled):
            if(row < -(len(board))):
                rowFilled = True
                validMove = False
            elif(board[row][col] == BLANK):
                board[row][col] = PLAYER2
                rowFilled = True
                validMove = True

            row -= 1

    row += 1

    printBoard(board)
    print(f"Computer placed a piece in column {col + 1}.")

    return board, row, col


# checks if there is a winner
# Input: board, where the last piece was placed
# Output: the winning player, or False if there is no winner
def isWinner(board, row, col):
    rowList = board[row]
    colList = []
    diagUpRow = []
    diagDownRow = []

    # Create list to check for vertical row
    for row_ in board:
        colList.append(row_[col])

    # Create lists to check for diagonal rows
    for index in range(-3, 4):
        rowToCheck = row + index
        colToCheck = col - index

        if(rowToCheck > -len(board) and \
        colToCheck < len(colList) and colToCheck > 0):
            diagUpRow.append(board[rowToCheck][colToCheck-1])

        rowToCheck = row + index
        colToCheck = col + index
        if(rowToCheck > -len(board) and \
        colToCheck < len(colList) and colToCheck > 0):
            diagDownRow.append(board[rowToCheck][colToCheck-1])

    # Horizontal 4 in a row
    for index in range(len(rowList) - 3):
        if(rowList[index] == rowList[index + 1] == 
        rowList[index + 2] == rowList[index + 3] != BLANK):
            return 1 if rowList[index] == PLAYER1 else 2

    # Vertical 4 in a row
    if(colList[row] == colList[row + 1] == 
    colList[row + 2] == colList[row + 3] != BLANK):
            return 1 if colList[row] == PLAYER1 else 2

    # Digonal 4 in a row
    for index in range(len(diagUpRow) - 3):
        if(diagUpRow[index] == diagUpRow[index + 1] == 
        diagUpRow[index + 2] == diagUpRow[index + 3] != BLANK):
            return 1 if diagUpRow[index] == PLAYER1 else 2

    for index in range(len(diagDownRow) - 3):
        if(diagDownRow[index] == diagDownRow[index + 1] == 
        diagDownRow[index + 2] == diagDownRow[index + 3] != BLANK):
            return 1 if diagDownRow[index] == PLAYER1 else 2


# checks if the board is completely full
# Input: the number of turns that have been made, the maximum number of turns
# Output: true or false
def fullBoard(turn, maxTurn):
    return True if turn == maxTurn else False