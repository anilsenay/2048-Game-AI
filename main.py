from expectimax import maxChance, setHeuristic
from game_2048 import getBoard, initBoard, printCurrentStatus, move, isGameOver, testMove

initBoard()
printCurrentStatus()

setHeuristic(5)

while(not isGameOver()):
    currentBoard = getBoard()
    decision = maxChance(currentBoard, 3)
    move(decision)
    printCurrentStatus()
