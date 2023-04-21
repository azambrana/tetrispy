from src.Position import Position
import copy

class Tetromino:
    blocks = [[]]
    pivot: Position

    def __init__(self, size, position=Position(0, 0)):
        self.size = size
        self.pivot = position
        self.blocks = [[0 for i in range(size)] for j in range(size)]
        self.update_positions_blocks(self.pivot)

    def rotate(self):
        self.blocks[:] = [list(row) for row in zip(*self.blocks[::-1])]
        self.update_positions_blocks(self.pivot)

    def move(self, direction):
        if direction == "left":
            self.pivot.col += -1
        elif direction == "right":
            self.pivot.col += 1
        elif direction == "down":
            self.pivot.row += 1

        self.update_positions_blocks(self.pivot)

    def get_blocks(self):
        result = []
        for row in self.blocks:
            for block in row:
                if block != 0:
                    result.append(block)

        return result

    def __str__(self):
        return f"{self.name()}Tetromino({self.blocks})"

    def update_positions_blocks(self, pivot):
        for row in range(self.size):
            for col in range(self.size):
                block = self.blocks[row][col]
                if block != 0:
                    block.position = Position(pivot.row + row, pivot.col + col)
                else:
                    self.blocks[row][col] = 0

    def draw(self, screen, pygame):
        for row in self.blocks:
            for block in row:
                if block != 0:
                    block.draw(screen, pygame)

    def get_hitbox(self):
        result = []
        self.update_positions_blocks(self.pivot)
        for row in self.blocks:
            for block in row:
                if block != 0:
                    result.append(block.position)
        return result

    def clone(self):
        return self.__clone__()

    def __clone__(self):
        # print(self.__class__.__name__)
        return copy.deepcopy(self)
