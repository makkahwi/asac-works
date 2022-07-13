import numpy as nump
import matplotlib.pyplot as plot


class ChessBoard:
    def __init__(self):
        self.board = nump.ones((8, 8, 3))
        self.colors = [(0, 0, 0), (0, 1, 1), (1, 0.2, 0), (1, 1, 1)]
        self.blue_column = 0
        self.blue_row = 0
        self.red_column = 0
        self.red_row = 0

        for x in range(8):
            for y in range(8):
                if x == 7 and y == 3:
                    self.board[x][y] = self.colors[2]
                if x % 2 != 0 and y % 2 == 0:
                    self.board[x][y] = self.colors[0]
                if x % 2 == 0 and y % 2 != 0:
                    if x == 0 and y == 3:
                        self.board[x][y] = self.colors[1]
                    else:
                        self.board[x][y] = self.colors[0]

    def add_blue(self, row, column):
        if row > 8 or row < 1 or column > 8 or column < 1:
            return "Given coordinates are out of range"
        else:
            self.blue_column = 3
            self.blue_row = 0
            self.board[row][column] = self.colors[1]

            if self.blue_column % 2 == 0 and self.blue_row % 2 != 0:
                self.board[blue_row][blue_column] = self.colors[0]
            elif self.blue_row % 2 == 0 and self.blue_column % 2 != 0:
                self.board[self.blue_row][self.blue_column] = self.colors[0]
            else:
                self.board[self.blue_row][self.blue_column] = self.colors[3]

            self.blue_column = row
            self.blue_row = column

    def add_red(self, row, column):
        if row > 8 or row < 1 or column > 8 or column < 1:
            return "Given coordinates are out of range"
        else:
            self.red_column = 3
            self.red_row = 7

            self.board[row][column] = self.colors[2]

            if self.red_column % 2 == 0 and self.red_row % 2 != 0:
                self.board[self.red_row][self.red_column] = self.colors[0]
            elif self.red_row % 2 == 0 and self.red_column % 2 != 0:
                self.board[self.red_row][self.red_column] = self.colors[0]
            else:
                self.board[self.red_row][self.red_column] = self.colors[3]

            self.red_column = row
            self.red_row = column

    def is_under_attack(self):
        if self.red_row == self.blue_row and self.red_column == self.blue_column:
            return True
        if self.red_row == self.blue_row:
            return True
        if self.red_column == self.blue_column:
            return True
        if abs(int(self.red_row) - int(self.blue_row)) == abs(
            int(self.red_column) - int(self.blue_column)
        ):
            return True
        return False

    def render(self):
        plot.imshow(self.board)
