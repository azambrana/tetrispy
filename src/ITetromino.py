from src.Position import Position
from src.SquareBlock import SquareBlock
from src.Tetromino import Tetromino


class ITetromino(Tetromino):

    def __init__(self, size, pivot=Position(-2, 3), block_size=40):
        super().__init__(size, pivot)
        self.blocks[1][0] = SquareBlock(Position(1, 0), (0, 255, 0), block_size)
        self.blocks[1][1] = SquareBlock(Position(1, 1), (0, 255, 0), block_size)
        self.blocks[1][2] = SquareBlock(Position(1, 2), (0, 255, 0), block_size)
        self.blocks[1][3] = SquareBlock(Position(1, 3), (0, 255, 0), block_size)

        super().update_positions_blocks(pivot)

    def __eq__(self, other):
        return self.blocks == other.blocks

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.blocks)

    def name(self):
        return "L"