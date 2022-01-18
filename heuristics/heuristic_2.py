
def heuristic2(BOARD):
    sum = 0
    numberOfEmptySquares = 0
    for i in range(4):
        for j in range(4):
            if BOARD[i][j] == 0:
                numberOfEmptySquares = numberOfEmptySquares + 1
            else:
                sum = sum + BOARD[i][j] ** 2
    return sum + 4194304 * numberOfEmptySquares
