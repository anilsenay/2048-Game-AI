from expectimax import maxChance, setHeuristic
from game_2048 import getBoard, initBoard, printCurrentStatus, move, isGameOver, testMove

initBoard()
printCurrentStatus()

setHeuristic(4)

while(not isGameOver()):
    currentBoard = getBoard()
    decision = maxChance(currentBoard, 2)
    move(decision)
    printCurrentStatus()
