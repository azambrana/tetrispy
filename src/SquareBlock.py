from src.Position import Position


class SquareBlock:
    position = Position(0, 0)
    color = (0, 0, 0)
    size = 0

    def __init__(self, position=Position(0, 0), color=(0, 0, 0), size=1):
        self.position = position
        self.color = color
        self.size = size

    def __str__(self):
        return f"Block({self.position}, {self.color}, {self.size})"

    def __hash__(self):
        return hash((self.position, self.color, self.size))

    def move(self, direction):
        if direction == "left":
            self.position.col -= 1
        elif direction == "right":
            self.position.col += 1
        elif direction == "down":
            self.position.row += 1

    def draw(self, screen, pygame):
        round = (self.position.col * self.size + 1, self.position.row * self.size + 1, self.size - 2, self.size - 2)
        pygame.draw.rect(screen, self.color, round)
        pygame.draw.rect(screen, (255, 255, 255), round, 2)