
def heuristic1(BOARD):
    return (
        (BOARD[0][0]) ** 3 +
        (BOARD[3][0]) ** 3 +
        (BOARD[0][3]) ** 3 +
        (BOARD[3][3]) ** 3 +
        (BOARD[0][1]) ** 2 +
        (BOARD[0][2]) ** 2 +
        (BOARD[1][0]) ** 2 +
        (BOARD[1][3]) ** 2 +
        (BOARD[2][0]) ** 2 +
        (BOARD[2][3]) ** 2 +
        (BOARD[3][1]) ** 2 +
        (BOARD[3][2]) ** 2 +
        (BOARD[1][1]) +
        (BOARD[1][2]) +
        (BOARD[2][1]) +
        (BOARD[2][2])
    )
