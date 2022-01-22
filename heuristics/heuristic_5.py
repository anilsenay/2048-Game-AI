
def heuristic5(BOARD):
    scores = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        for j in range(4):
            for a in range(j + 1, 4):
                if(BOARD[i][a] == 0):
                    continue
                if(BOARD[i][j] == BOARD[i][a]):
                    scores[i][j] = scores[i][j] + 1
                    break

            for a in reversed(range(0, j)):
                if(BOARD[i][a] == 0):
                    continue
                if(BOARD[i][j] == BOARD[i][a]):
                    scores[i][j] = scores[i][j] + 1
                    break

            for a in range(i + 1, 4):
                if(BOARD[a][j] == 0):
                    continue
                if(BOARD[i][j] == BOARD[a][j]):
                    scores[i][j] = scores[i][j] + 1
                    break

            for a in reversed(range(0, i)):
                if(BOARD[a][j] == 0):
                    continue
                if(BOARD[i][j] == BOARD[a][j]):
                    scores[i][j] = scores[i][j] + 1
                    break

    totalScores = 0
    for i in range(4):
        for j in range(4):
            totalScores = totalScores + BOARD[i][j] ** scores[i][j]
    return totalScores
