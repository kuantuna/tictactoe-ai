import sys
import enum
# Board will be an array with the length of nxn-1
# 0 -> Square is empty
# 1 -> There is X in the square
# 2 -> There is O in the square

class Letter(enum.Enum):
    Empty = 0
    X = 1
    O = 2


board = [-1,
         Letter.Empty.value, Letter.Empty.value, Letter.O.value,
         Letter.X.value, Letter.Empty.value, Letter.Empty.value,
         Letter.X.value, Letter.O.value, Letter.Empty.value]
dimension = 3  # Let's make it 3 for now (for simplicity)


def isValid(board):
    return (board.count(Letter.X.value) - board.count(Letter.O.value) == 1) or (
            board.count(Letter.X.value) - board.count(Letter.O.value) == 0)


def squareIsFree(index):
    return board[index] == Letter.Empty.value


def sideToPlay(board):
    return board.count(Letter.X.value) - board.count(Letter.O.value) == 0


def calculateDepth(board):
    return board.count(Letter.Empty.value)


# For 3x3
def gameOver(board):
    return ((board[7] == board[8] and board[8] == board[9] and board[7] != Letter.Empty.value) or
            (board[4] == board[5] and board[5] == board[6] and board[4] != Letter.Empty.value) or
            (board[1] == board[2] and board[2] == board[3] and board[1] != Letter.Empty.value) or
            (board[1] == board[4] and board[4] == board[7] and board[1] != Letter.Empty.value) or
            (board[2] == board[5] and board[5] == board[8] and board[2] != Letter.Empty.value) or
            (board[3] == board[6] and board[6] == board[9] and board[3] != Letter.Empty.value) or
            (board[1] == board[5] and board[5] == board[9] and board[1] != Letter.Empty.value) or
            (board[3] == board[5] and board[5] == board[7] and board[3] != Letter.Empty.value))


def getWinningSide(board):
    if ((board[7] == board[8] and board[8] == board[9] and board[7] == 1) or
            (board[4] == board[5] and board[5] == board[6] and board[4] == Letter.X.value) or
            (board[1] == board[2] and board[2] == board[3] and board[1] == Letter.X.value) or
            (board[1] == board[4] and board[4] == board[7] and board[1] == Letter.X.value) or
            (board[2] == board[5] and board[5] == board[8] and board[2] == Letter.X.value) or
            (board[3] == board[6] and board[6] == board[9] and board[3] == Letter.X.value) or
            (board[1] == board[5] and board[5] == board[9] and board[1] == Letter.X.value) or
            (board[3] == board[5] and board[5] == board[7] and board[3] == Letter.X.value)):
        return 1
    if ((board[7] == board[8] and board[8] == board[9] and board[7] == 2) or
            (board[4] == board[5] and board[5] == board[6] and board[4] == Letter.O.value) or
            (board[1] == board[2] and board[2] == board[3] and board[1] == Letter.O.value) or
            (board[1] == board[4] and board[4] == board[7] and board[1] == Letter.O.value) or
            (board[2] == board[5] and board[5] == board[8] and board[2] == Letter.O.value) or
            (board[3] == board[6] and board[6] == board[9] and board[3] == Letter.O.value) or
            (board[1] == board[5] and board[5] == board[9] and board[1] == Letter.O.value) or
            (board[3] == board[5] and board[5] == board[7] and board[3] == Letter.O.value)):
        return -1
    else:
        return 0


def getChildrenOfBoard(board):
    side = sideToPlay(board)
    children_board = []
    for index in range(len(board)):
        if squareIsFree(index):
            new_board = board[:]
            if side:
                new_board[index] = Letter.X.value
            else:
                new_board[index] = Letter.O.value
            children_board.append(new_board)
    return children_board


def evaluate(board, depth, is_xs_turn):
    if depth == 0 or gameOver(board):
        # -1 -> O wins   ///    0 -> draw     ///      1 -> X wins
        # return static evaluation of the position
        return getWinningSide(board)

    if is_xs_turn:
        maxEvaluation = -1
        for child_board in getChildrenOfBoard(board):
            evaluation = evaluate(child_board, depth - 1, False)
            maxEvaluation = max(maxEvaluation, evaluation)
        return maxEvaluation

    else:
        minEvaluation = 1
        for child_board in getChildrenOfBoard(board):
            evaluation = evaluate(child_board, depth - 1, True)
            minEvaluation = min(minEvaluation, evaluation)
        return minEvaluation


def main():
    if not isValid(board):
        print("Board is not valid!")
        sys.exit(0)

    if gameOver(board):
        print("Game is already over!")
        sys.exit(0)

    side = sideToPlay(board)  # boolean
    depth = calculateDepth(board)
    evaluation = evaluate(board, depth, side)
    if evaluation == 2:
        print("There is a problem dunno what :(")
        sys.exit(0)
    print("Evaluation of the position is", evaluation)


main()
