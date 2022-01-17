from game_2048 import initBoard, printCurrentStatus, move, isGameOver

initBoard()
printCurrentStatus()

while(not isGameOver()):
    possibleAnswers = ["UP", "DOWN", "LEFT", "RIGHT"]
    answer = input(
        "Which move do you want to swipe? Type one of the 'up', 'down', 'left', 'right' : ")
    while(answer.upper() not in possibleAnswers):
        print("You typed a wrong direction. Please try again.")
        answer = input(
            "Which direction do you want to swipe? Type one of the 'up', 'down', 'left', 'right' : ")

    move(answer.upper())
    printCurrentStatus()
