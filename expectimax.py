from random import randint
from game_2048 import testMove
from heuristics.heuristic_1 import heuristic1
from heuristics.heuristic_2 import heuristic2
from heuristics.heuristic_3 import heuristic3
from heuristics.heuristic_4 import heuristic4
from heuristics.heuristic_5 import heuristic5

import copy

directions = ["UP", "DOWN", "LEFT", "RIGHT"]

heuristic = heuristic1


def setHeuristic(number):
    global heuristic
    if(number == 1):
        heuristic = heuristic1
    if(number == 2):
        heuristic = heuristic2
    if(number == 3):
        heuristic = heuristic3
    if(number == 4):
        heuristic = heuristic4
    if(number == 5):
        heuristic = heuristic5


def maxChance(state, ply=1):
    _, direction = max(state, ply)
    return direction


def max(state, ply=1):
    maxScore = -float('inf')
    selectedDirection = None
    for direction in directions:
        [newBoard, newScore] = testMove(direction, state)

        # prunning
        if(newBoard == None):
            continue

        resultChance = chance(newBoard, ply)

        if(resultChance > maxScore):
            maxScore = resultChance
            selectedDirection = direction
    if(selectedDirection == None):
        return [maxScore, directions[randint(0, 3)]]

    return [maxScore, selectedDirection]


def chance(state, ply):
    newPly = ply - 1
    LEAF = True if newPly == 0 else False
    totalChance = 0
    emptySquares = 0
    for i in range(4):
        for j in range(4):
            if(state[i][j] == 0):
                emptySquares = emptySquares + 1

    for i in range(4):
        for j in range(4):
            if(state[i][j] != 0):
                continue
            newBoard = copy.deepcopy(state)
            newBoard[i][j] = 2
            result = 0
            if(LEAF):
                result = heuristic(newBoard)
            else:
                result, _ = max(newBoard, newPly)

            totalChance = totalChance + result * 0.9 / emptySquares

            result = 0
            newBoard = copy.deepcopy(state)
            newBoard[i][j] = 4
            if(LEAF):
                result = heuristic(newBoard)
            else:
                result, _ = max(newBoard, newPly)

            totalChance = totalChance + result * 0.1 / emptySquares

    return totalChance
