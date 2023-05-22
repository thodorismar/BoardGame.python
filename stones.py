
import random

board = [
    " ", " ", " ",
    " ", " ", " ",
    " ", " ", " ", ]
player1 = "X"
player2 = "O"
gameRunning = True
boardPosition = {"A1": 0, "A2": 1, "A3": 2, "B1": 3, "B2": 4, "B3": 5, "C1": 6, "C2": 7, "C3": 8, }
players = {"X": "Player 1", "O": "Player 2"}

while True:

    def printBoard():
        print("  1  " + "  2  " + "  3  ")
        print("A " + str(board[0]) + " ---" + str(board[1]) + "--- " + str(board[2]))
        print("  |\   |   /|" "\n"
              "  | \  |  / |" "\n"
              "  |  \ | /  |  ")
        print("B " + str(board[3]) + " ---" + str(board[4]) + "--- " + str(board[5]))
        print("  |   /|\   |""\n"
              "  |  / | \  |""\n"
              "  | /  |  \ |")
        print("C " + str(board[6]) + " ---" + str(board[7]) + "--- " + str(board[8]))


    def checkHorizontal():
        if (board[0] == board[1] == board[2] and board[0] == "X") or (
                board[3] == board[4] == board[5] and board[3] == "X") or (
                board[6] == board[7] == board[8] and board[6] == "X"):
            return True
        if (board[0] == board[1] == board[2] and board[0] == "O") or (
                board[3] == board[4] == board[5] and board[3] == "O") or (
                board[6] == board[7] == board[8] and board[6] == "O"):
            return True
        return 0


    def checkRow():
        if (board[0] == board[3] == board[6] and board[0] == "X") or (
                board[1] == board[4] == board[7] and board[1] == "X") or (
                board[2] == board[5] == board[8] and board[2] == "X"):
            return True
        if (board[0] == board[3] == board[6] and board[0] == "O") or (
                board[1] == board[4] == board[7] and board[1] == "O") or (
                board[2] == board[5] == board[8] and board[2] == "O"):
            return True
        return 0


    def checkDiagonal():
        if (board[0] == board[4] == board[8] and board[0] == "X") or (
                board[2] == board[4] == board[6] and board[2] == "X"):
            return True
        if (board[0] == board[4] == board[8] and board[0] == "O") or (
                board[2] == board[4] == board[6] and board[2] == "O"):
            return True
        return 0


    def isWin():
        if checkDiagonal() or checkHorizontal() or checkRow() == 1:
            return True
        return 0


    def isItLegal(s1, s2):
        if boardPosition.get(s1) == 0 and (
                boardPosition.get(s2) == 1 or boardPosition.get(s2) == 3 or boardPosition.get(s2) == 4):
            return True
        if boardPosition.get(s1) == 1 and (
                boardPosition.get(s2) == 0 or boardPosition.get(s2) == 2 or boardPosition.get(s2) == 4):
            return True
        if boardPosition.get(s1) == 2 and (
                boardPosition.get(s2) == 1 or boardPosition.get(s2) == 4 or boardPosition.get(s2) == 5):
            return True
        if boardPosition.get(s1) == 3 and (
                boardPosition.get(s2) == 1 or boardPosition.get(s2) == 4 or boardPosition.get(s2) == 6):
            return True
        if boardPosition.get(s1) == 4:
            return True
        if boardPosition.get(s1) == 5 and (
                boardPosition.get(s2) == 4 or boardPosition.get(s2) == 2 or boardPosition.get(s2) == 8):
            return True
        if boardPosition.get(s1) == 6 and (
                boardPosition.get(s2) == 4 or boardPosition.get(s2) == 3 or boardPosition.get(s2) == 7):
            return True
        if boardPosition.get(s1) == 7 and (
                boardPosition.get(s2) == 4 or boardPosition.get(s2) == 6 or boardPosition.get(s2) == 8):
            return True
        if boardPosition.get(s1) == 8 and (
                boardPosition.get(s2) == 4 or boardPosition.get(s2) == 5 or boardPosition.get(s2) == 7):
            return True
        return 0

    # Choose who goes first

    # pinakas = [1,2]
    first = (random.randint(1, 2))
    # second = 0
    # if first == pinakas[0]:
    #    second = 2
    # else:
    #    second = 1

    if first == 1:
        current_player = player1
        other_player = player2

    else:
        current_player = player2
        other_player = player1

    print(str(players.get(current_player)) + " goes first")

    for j in range(2):
        for i in range(3):
            while 1:
                printBoard()
                choice = input(str(players.get(current_player)) + " peg no. " + str(
                    i + 1) + ". Enter the board position to put your peg. ")

                if (choice in boardPosition) and board[boardPosition.get(choice)] == " ":
                    board[boardPosition.get(choice)] = current_player
                    if isWin():
                        print("Invalid position. Cannot complete 3-in-a-row at this stage.")
                        board[boardPosition.get(choice)] = " "
                    else:
                        break
                elif choice not in boardPosition:
                    print("Invalid position. Not a board position. Please re-enter.")
                else:
                    print("Position taken by another peg. Please re-enter.")
        temp = current_player
        current_player = other_player
        other_player = temp

    while gameRunning:
        while True:
            printBoard()
            choice = input(str(players.get(current_player) + " enter your move:"))
            if len(choice) == 4:
                pinakas = []
                s1 = str(choice[0]) + str(choice[1])
                s2 = str(choice[2]) + str(choice[3])
                pinakas.append(s1)
                pinakas.append(s2)
                if s1 and s2 in boardPosition:
                    if board[boardPosition.get(s1)] != current_player:
                        print("Invalid move. Origin is not occupied by " + players.get(current_player)+"'s peg")
                    elif board[boardPosition.get(s2)] != " ":
                        print("Invalid move. Destination position is not empty. Please re-enter move.")
                    elif not isItLegal(s1, s2):
                        print(
                            "Invalid move. Destination position is not connected to origin position. Please re-enter "
                            "move.")
                    else:
                        board[boardPosition.get(s2)] = current_player
                        board[boardPosition.get(s1)] = " "
                        if isWin():
                            print(players.get(current_player) + " wins!")
                            gameRunning = False
                            break
                        else:
                            temp = current_player
                            current_player = other_player
                            other_player = temp
                        break
                else:
                    print("Invalid move. Enter correct origin and destination positions")
            else:
                print("Invalid move. Enter origin and destination positions in 4 characters, e.g., A2B1")

    epilogh = input(str("Type 'Y' to play again or 'Q' to quit."))
    if epilogh == "Y" or epilogh == "y":
        continue
    else:
        print("Thanks for playing! :)")
        break
