import numpy as np

BOARD_r = np.array(['?', '?', "?"])
BOARD = np.vstack((BOARD_r, BOARD_r))
BOARD = np.vstack((BOARD, BOARD_r))

round = 0  # player 0 or 1
playerSymbols = ('O', 'X')


def checkBoard():
    for x in range(3):
        symbol = BOARD[x, 0]
        if symbol == '?':
            continue
        if all(i == symbol for i in BOARD[x]):
            return True
    for y in range(3):
        symbol = BOARD[0, y]
        if symbol == '?':
            continue
        if all(i == symbol for i in BOARD[:, y]):
            return True

    symbol = BOARD[0, 0]
    if symbol != "?" and BOARD[0, 0] == symbol and BOARD[1, 1] == symbol and BOARD[2, 2] == symbol:
        return True

    symbol = BOARD[0, 2]
    if symbol != "?" and BOARD[0, 2] == symbol and BOARD[1, 1] == symbol and BOARD[0, 2] == symbol:
        return True


def printBoard():
    print("□ - - - - - □")
    print("|", BOARD[0, 0], "|", BOARD[0, 1], "|", BOARD[0, 2], "|")
    print("□ - - - - - □")
    print("|", BOARD[1, 0], "|", BOARD[1, 1], "|", BOARD[1, 2], "|")
    print("□ - - - - - □")
    print("|", BOARD[2, 0], "|", BOARD[2, 1], "|", BOARD[2, 2], "|")
    print("□ - - - - - □")


printBoard()

while True:

    print("Give me the coordinates to put your symbol:")
    coords = input()
    Y = int(coords[0])
    X = int(coords[2])

    if BOARD[Y, X] == '?':
        BOARD[Y, X] = playerSymbols[round]

    printBoard()

    if checkBoard():
        print("Player", round, "wins!")
        break

    if round:
        round = 0
    else:
        round = 1
