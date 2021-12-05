'''The winning_board function takes a single board and searches rows and columns for -1, which signifies that this
particular number has been cast. If a row or column consists entirely of -1's, it's a win and True is returned.'''


def winning_board(board):
    for row in board.board:
        for col in range(len(row)):
            if row[col] != -1:  # If the first number is not a -1, it can't be a win.
                break
            else:
                if col != len(row) - 1:
                    continue
                else:
                    return True
    for col in range(len(board.board)):
        for row in board.board:
            if row[col] != -1:  # if the first number in a row is not a -1, it can't be a win
                break
            else:
                if board.board.index(row) != len(row) - 1:
                    continue
                else:
                    return True
    return False


'''This is the definition for a single Bingo board. 
The sum of all fields of the board is calculated. 
Moreover, this function checks if the cast number is in the board. If that is the case, it is subtracted from
the board_value. Then it is checked if the board is a win.'''


class Board:
    def __init__(self, board):
        self.board = board  # The board: Its a list of lists
        self.board_value = 0  # The value of all numbers in the field
        self.win = 0  # Has already won or not. 0 by default.

    def check_fields(self, board, cast):
        if self.board_value == 0:
            row_sum = [sum(i) for i in zip(*board.board)]
            self.board_value = sum(row_sum)
        for row in board.board:
            if cast in row:
                self.board_value -= cast
                row[row.index(cast)] = -1
        if winning_board(board) is True:
            self.win = 1
            return True
        else:
            return False
