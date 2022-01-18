def heuristic3(BOARD):
    max_value = max(calculateCorner(BOARD, 0, 0), calculateCorner(
        BOARD, 0, 3), calculateCorner(BOARD, 3, 0), calculateCorner(BOARD, 3, 3))
    return max_value


def calculateCorner(BOARD, x: int, y: int):
    sum = 0
    if x == 0 and y == 0:
        while (x != 4):
            while (y != 4):
                sum = sum + BOARD[x][y]**(7-(x+y))
                y = y + 1
            x = x + 1
    if x == 0 and y == 3:
        while (x != 4):
            while (y != -1):
                sum = sum + BOARD[x][y]**(7-(x+y))
                y = y - 1
            x = x + 1
    if x == 3 and y == 0:
        while (x != -1):
            while (y != 4):
                sum = sum + BOARD[x][y]**(7-(x+y))
                y = y + 1
            x = x - 1
    if x == 3 and y == 3:
        while (x != -1):
            while (y != -1):
                sum = sum + BOARD[x][y]**(7-(x+y))
                y = y - 1
            x = x - 1
    return sum
