from board import Board

"""The rank is the position where a board has won in relation to the others."""
rank = 0

'''List of casts'''
cast = [67, 31, 58, 8, 79, 18, 19, 45, 38, 13, 40, 62, 85, 10, 21, 96, 56, 55, 4, 36, 76, 42, 32, 34, 39,
        89, 6, 12, 24,
        57, 93, 47, 41, 52, 83, 61, 5, 37, 28, 15, 86, 23, 69, 92, 70, 27, 25, 53, 44, 80, 65, 22, 99, 43,
        66, 26, 11,
        72, 2, 98, 14, 82, 87, 20, 73, 46, 35, 7, 1, 84, 95, 74, 81, 63, 78, 94, 16, 60, 29, 97, 91, 30,
        17, 54, 68, 90,
        71, 88, 77, 9, 64, 50, 0, 49, 48, 75, 3, 59, 51, 33]

'''This function loads data from a file containing the bingo boards, formatted in 5x5 matrices, with a separating
empty line between boards. The lines of each board are a list of integers, the board is a list of lists. Every board 
becomes an object "board". Each board object is append to a list in the bingo object, which holds the enirety of the 
bingo boards.'''


def load_data():
    start = 0
    with open("boards", "r") as data:
        lines = [line.strip() for line in data.readlines() if line.strip()]
    while start < len(lines):
        k = []
        for i in range(start, start + 5):
            string_list = lines[i].split()
            k.append([int(x) for x in string_list])
        o = Board(k)
        bingo.boards.append(o)
        start += 5

'''The Bingo class has an attribute boards which holds the lists of all board objects'''

class Bingo:
    def __init__(self):
        self.boards = []


if __name__ == "__main__":
    bingo = Bingo() # The object is created
    load_data() # The data is loaded
    for c in cast: # The list of casts is traversed. The runtime is, at worst quadratic.
        for board in bingo.boards: # The cast is used on each bingo board.
            if board.win == 0: # The board is only considered if it hasn't won yet.
                board.check_fields(board, c)
                if board.win == 1: # If the board has won after the current run, it is printed with its properties
                    rank += 1
                    print("Winning number is: ", c, ", remaining values: ", board.board_value, "Rank: ", rank)
                    print("Winning value: ", c * board.board_value)
