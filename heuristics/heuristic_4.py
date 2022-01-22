from math import floor


def heuristic5(BOARD):
    score = 0
    for power in reversed(range(0, 16)):
        i = floor(4 - ((power + 1) / 4))
        j = (4 - ((power + 1) % 4)) % 4 if (i % 2 == 0) else (((power) % 4))

        if(BOARD[i][j] != 0):
            score = score + ((4 ** power)*BOARD[i][j])
    return score
