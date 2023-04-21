import math

class Position:
    row = 0
    col = 0

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def to_string(self):
        return f"({self.row},{self.col})"

    def __str__(self):
        return f"({self.row},{self.col})"

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.row, self.col))
