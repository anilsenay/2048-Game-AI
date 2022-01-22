import copy
from random import randint
from typing import Literal


BOARD = None
SCORE = 0


def initBoard():
    global BOARD
    BOARD = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    # Add random two numbers
    placeRandomSquare(BOARD)
    placeRandomSquare(BOARD)


def placeRandomSquare(BOARD):
    emptySquares = []
    for i in range(0, 4):
        for j in range(0, 4):
            if(BOARD[i][j] == 0):
                emptySquares.append([i, j])

    if(len(emptySquares) == 0):
        return
    random = randint(0, len(emptySquares) - 1)
    i, j = emptySquares[random]

    squareChance = randint(1, 10)
    squareValue = 2 if squareChance < 10 else 4
    BOARD[i][j] = squareValue


def isGameOver():
    for i in range(0, 3):
        for j in range(0, 4):
            if((BOARD[i][j] == 0) or (BOARD[i+1][j] == 0) or BOARD[i][j] == BOARD[i+1][j]):
                return False
    for i in range(0, 4):
        for j in range(0, 3):
            if(BOARD[i][j] == BOARD[i][j+1] or (BOARD[i][j+1] == 0)):
                return False
    print("Game Over!")
    return True


def move(direction: Literal["UP", "DOWN", "LEFT", "RIGHT"]):
    global SCORE
    updatedSquares = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    if(direction == "UP"):
        # swipe and merge all squares to up
        for _ in range(3):
            for i in range(1, 4):
                for j in range(0, 4):
                    # ignore empty squares
                    if(BOARD[i][j] == 0):
                        continue

                    # swipe to up if upper square is empty
                    if(BOARD[i-1][j] == 0):
                        BOARD[i-1][j] = BOARD[i][j]
                        BOARD[i][j] = 0

                    # merge same values
                    if(not (BOARD[i-1][j] == 0) and BOARD[i-1][j] == BOARD[i][j] and updatedSquares[i-1][j] == 0 and updatedSquares[i][j] == 0):
                        BOARD[i-1][j] = BOARD[i-1][j] * 2
                        SCORE = SCORE + BOARD[i-1][j]
                        BOARD[i][j] = 0
                        updatedSquares[i-1][j] = 1
                        updatedSquares[i][j] = 1

    elif(direction == "DOWN"):
        # swipe and merge all squares to down
        for _ in range(3):
            for i in reversed(range(0, 3)):
                for j in range(0, 4):
                    # ignore empty squares
                    if(BOARD[i][j] == 0):
                        continue

                    # swipe to down if upper square is empty
                    if(BOARD[i+1][j] == 0):
                        BOARD[i+1][j] = BOARD[i][j]
                        BOARD[i][j] = 0

                    # merge same values
                    if(not (BOARD[i+1][j] == 0) and BOARD[i+1][j] == BOARD[i][j] and updatedSquares[i+1][j] == 0 and updatedSquares[i][j] == 0):
                        BOARD[i+1][j] = BOARD[i+1][j] * 2
                        SCORE = SCORE + BOARD[i+1][j]
                        BOARD[i][j] = 0
                        updatedSquares[i+1][j] = 1
                        updatedSquares[i][j] = 1

    elif(direction == "LEFT"):
        # swipe and merge all squares to left
        for _ in range(3):
            for i in range(1, 4):
                for j in range(0, 4):
                    # ignore empty squares
                    if(BOARD[j][i] == 0):
                        continue

                    # swipe to left if upper square is empty
                    if(BOARD[j][i-1] == 0):
                        BOARD[j][i-1] = BOARD[j][i]
                        BOARD[j][i] = 0

                    # merge same values
                    if(not (BOARD[j][i-1] == 0) and BOARD[j][i-1] == BOARD[j][i] and updatedSquares[j][i-1] == 0 and updatedSquares[j][i] == 0):
                        BOARD[j][i-1] = BOARD[j][i-1] * 2
                        SCORE = SCORE + BOARD[j][i-1]
                        BOARD[j][i] = 0
                        updatedSquares[j][i-1] = 1
                        updatedSquares[j][i] = 1

    elif(direction == "RIGHT"):
        # swipe and merge all squares to right
        for _ in range(3):
            for i in reversed(range(0, 3)):
                for j in range(0, 4):
                    # ignore empty squares
                    if(BOARD[j][i] == 0):
                        continue

                    # swipe to right if upper square is empty
                    if(BOARD[j][i+1] == 0):
                        BOARD[j][i+1] = BOARD[j][i]
                        BOARD[j][i] = 0

                    # merge same values
                    if(not (BOARD[j][i+1] == 0) and BOARD[j][i+1] == BOARD[j][i] and updatedSquares[j][i+1] == 0 and updatedSquares[j][i] == 0):
                        BOARD[j][i+1] = BOARD[j][i+1] * 2
                        SCORE = SCORE + BOARD[j][i+1]
                        BOARD[j][i] = 0
                        updatedSquares[j][i+1] = 1
                        updatedSquares[j][i] = 1

    placeRandomSquare(BOARD)
    print("SCORE: " + str(SCORE))


def printCurrentStatus():
    for i in range(4):
        for j in range(4):
            print(BOARD[i][j], end="    ")
        print("\n")


def getBoard():
    return BOARD


def getScore():
    return SCORE


def testMove(direction: Literal["UP", "DOWN", "LEFT", "RIGHT"], boardArg):
    NEW_BOARD = copy.deepcopy(boardArg)
    NEW_SCORE = 0
    updatedSquares = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    updateCount = 0
    if(direction == "UP"):
        # swipe and merge all squares to up
        for _ in range(3):
            for i in range(1, 4):
                for j in range(0, 4):
                    # ignore empty squares
                    if(NEW_BOARD[i][j] == 0):
                        continue
                    updateCount = updateCount + 1
                    # swipe to up if upper square is empty
                    if(NEW_BOARD[i-1][j] == 0):
                        NEW_BOARD[i-1][j] = NEW_BOARD[i][j]
                        NEW_BOARD[i][j] = 0

                    # merge same values
                    if(not (NEW_BOARD[i-1][j] == 0) and NEW_BOARD[i-1][j] == NEW_BOARD[i][j] and updatedSquares[i-1][j] == 0 and updatedSquares[i][j] == 0):
                        NEW_BOARD[i-1][j] = NEW_BOARD[i-1][j] * 2
                        NEW_SCORE = NEW_SCORE + NEW_BOARD[i-1][j]
                        NEW_BOARD[i][j] = 0
                        updatedSquares[i-1][j] = 1
                        updatedSquares[i][j] = 1

    elif(direction == "DOWN"):
        # swipe and merge all squares to down
        for _ in range(3):
            for i in reversed(range(0, 3)):
                for j in range(0, 4):
                    # ignore empty squares
                    if(NEW_BOARD[i][j] == 0):
                        continue
                    updateCount = updateCount + 1
                    # swipe to down if upper square is empty
                    if(NEW_BOARD[i+1][j] == 0):
                        NEW_BOARD[i+1][j] = NEW_BOARD[i][j]
                        NEW_BOARD[i][j] = 0

                    # merge same values
                    if(not (NEW_BOARD[i+1][j] == 0) and NEW_BOARD[i+1][j] == NEW_BOARD[i][j] and updatedSquares[i+1][j] == 0 and updatedSquares[i][j] == 0):
                        NEW_BOARD[i+1][j] = NEW_BOARD[i+1][j] * 2
                        NEW_SCORE = NEW_SCORE + NEW_BOARD[i+1][j]
                        NEW_BOARD[i][j] = 0
                        updatedSquares[i+1][j] = 1
                        updatedSquares[i][j] = 1

    elif(direction == "LEFT"):
        # swipe and merge all squares to left
        for _ in range(3):
            for i in range(1, 4):
                for j in range(0, 4):
                    # ignore empty squares
                    if(NEW_BOARD[j][i] == 0):
                        continue
                    updateCount = updateCount + 1
                    # swipe to left if upper square is empty
                    if(NEW_BOARD[j][i-1] == 0):
                        NEW_BOARD[j][i-1] = NEW_BOARD[j][i]
                        NEW_BOARD[j][i] = 0

                    # merge same values
                    if(not (NEW_BOARD[j][i-1] == 0) and NEW_BOARD[j][i-1] == NEW_BOARD[j][i] and updatedSquares[j][i-1] == 0 and updatedSquares[j][i] == 0):
                        NEW_BOARD[j][i-1] = NEW_BOARD[j][i-1] * 2
                        NEW_SCORE = NEW_SCORE + NEW_BOARD[j][i-1]
                        NEW_BOARD[j][i] = 0
                        updatedSquares[j][i-1] = 1
                        updatedSquares[j][i] = 1

    elif(direction == "RIGHT"):
        # swipe and merge all squares to right
        for _ in range(3):
            for i in reversed(range(0, 3)):
                for j in range(0, 4):
                    # ignore empty squares
                    if(NEW_BOARD[j][i] == 0):
                        continue
                    updateCount = updateCount + 1
                    # swipe to right if upper square is empty
                    if(NEW_BOARD[j][i+1] == 0):
                        NEW_BOARD[j][i+1] = NEW_BOARD[j][i]
                        NEW_BOARD[j][i] = 0

                    # merge same values
                    if(not (NEW_BOARD[j][i+1] == 0) and NEW_BOARD[j][i+1] == NEW_BOARD[j][i] and updatedSquares[j][i+1] == 0 and updatedSquares[j][i] == 0):
                        NEW_BOARD[j][i+1] = NEW_BOARD[j][i+1] * 2
                        NEW_SCORE = NEW_SCORE + NEW_BOARD[j][i+1]
                        NEW_BOARD[j][i] = 0
                        updatedSquares[j][i+1] = 1
                        updatedSquares[j][i] = 1

    global SCORE
    NEW_SCORE = NEW_SCORE + SCORE

    if(updateCount == 0):
        return [None, -float('inf')]
    return [NEW_BOARD, NEW_SCORE]
