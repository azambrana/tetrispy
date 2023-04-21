from src.Position import Position


class Playfield:
    grid = [[]]
    block_size = 40
    current_tetromino = None
    hitbox = []

    def __init__(self, columns, rows, block_size=50):
        self.columns = columns
        self.rows = rows
        self.block_size = block_size
        self.grid = [[0 for i in range(columns)] for j in range(rows)]  # 0 = empty, 1 = occupied

    def check_collision(self, tetromino):
        set_hitbox = set(self.get_hitbox())
        set_tetromino_hitbox = set(tetromino.get_hitbox())
        has_collide = len(set_hitbox.intersection(set_tetromino_hitbox)) > 0

        return has_collide

    def check_full_rows(self, rows_to_check=[]):
        filled_rows = []
        for row in set(rows_to_check):
            total_blocks_in_row = 0
            for col in range(self.columns):
                if self.grid[row][col] == 0:
                    break
                else:
                    total_blocks_in_row += 1
            if total_blocks_in_row == self.columns:
                filled_rows.append(row)

        return filled_rows

    def check_if_row_filled(self, row):
        total_blocks_in_row = 0
        for col in range(self.columns):
            if self.grid[row][col] != 0:
                total_blocks_in_row += 1

        if total_blocks_in_row == self.columns:
            return True

        return False

    def remove_row(self, row):
        pass


    def remove_rows(self, rows):
        if len(rows) == 0:
            return

        offset = max(rows)
        # process the affected rows
        for i in range(len(set(rows))):
            for row in sorted(range(min(rows), offset + 1), reverse=True):
                is_row_filled = self.check_if_row_filled(row)
                if is_row_filled:
                    # remove row
                    for j in range(self.columns):
                        self.grid[row][j] = 0
                    # move rows down
                    for r in sorted(range(0, row), reverse=True):
                        for c in range(self.columns):
                            if self.grid[r][c] != 0:
                                self.grid[r][c].position.row += 1
                            self.grid[r + 1][c] = self.grid[r][c]


    def add_tetromino(self, tetromino):
        for row in tetromino.get_blocks():
            for block in row:
                if block != 0:
                    self.grid[block.position.row][block.position.col] = 1

    def draw(self, screen, pygame):
        self.draw_lines(pygame, screen)

        # draw filled blocks
        for row in range(self.rows):
            for col in range(self.columns):
                if self.grid[row][col] != 0:
                    self.grid[row][col].draw(screen, pygame)

    def draw_lines(self, pygame, screen):
        # draw lines horizontally and vertically
        for col in range(self.columns):
            pygame.draw.line(screen, (123, 123, 123), (col * self.block_size, 0),
                             (col * self.block_size, self.rows * self.block_size), 1)
        for row in range(self.rows):
            pygame.draw.line(screen, (123, 123, 123), (0, row * self.block_size),
                             (self.columns * self.block_size, row * self.block_size), 1)

    def set_current_tetromino(self, tetromino):
        self.current_tetromino = tetromino

    def get_current_tetromino(self):
        return self.current_tetromino

    def drop_current_tetromino(self):
        rows_to_check = []
        for block in self.current_tetromino.get_blocks():
            if block != 0:
                self.grid[block.position.row][block.position.col] = block
                rows_to_check.append(block.position.row)

        # print(self.check_full_rows(rows_to_check))
        rows_to_remove = self.check_full_rows(rows_to_check)
        self.remove_rows(rows_to_remove)

    def get_hitbox(self):
        self.hitbox = []
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i][j] != 0:
                    position = self.grid[i][j].position
                    self.hitbox.append(position)

        for i in range(self.rows + 1):
            self.hitbox.append(Position(i, -1))
            self.hitbox.append(Position(i, self.columns))

        for i in range(self.columns):
            self.hitbox.append(Position(self.rows, i))

        return self.hitbox

    def __str__(self):
        return f"Playfield({self.grid})"
