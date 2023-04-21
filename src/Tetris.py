import random

import pygame

from src.Position import Position
from src.LTetromino import LTetromino
from src.STetromino import STetromino
from src.TTetromino import TTetromino
from src.ITetromino import ITetromino
from src.JTetromino import JTetromino
from src.ZTetromino import ZTetromino
from src.OTetromino import OTetromino

from src.Playfield import Playfield

# Initialize Pygame
pygame.init()

# Setup board
total_rows = 20
total_columns = 10

# Set up the square
square_size = 40

# Set up the screen
size = (total_columns * square_size, total_rows * square_size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tetris Game')

# Set up the colors
WHITE = (255, 255, 255)
LIGHT_GREY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

playfield = Playfield(10, 20, square_size)

# Set up the timer
pygame.time.set_timer(pygame.USEREVENT, 800)

def capture_key_event(event):
    current_tetromino = playfield.get_current_tetromino()
    command = get_command(event)

    will_collide = predict_collition(current_tetromino.clone(), command)
    if not will_collide:
        control_tetromino(current_tetromino, command)

    if will_collide and command == "down":
        playfield.drop_current_tetromino()
        playfield.set_current_tetromino(compute_current_tetromino())

    if command != None:
        redraw_screen(screen, pygame)


def control_tetromino(tetromino, command):
    if command == None:
        return

    if command == "rotate":
        tetromino.rotate()
    else:
        tetromino.move(command)

def get_command(event):
    command = None
    if event.key == pygame.K_UP:
        command = "rotate"
    elif event.key == pygame.K_DOWN:
        command = "down"
    elif event.key == pygame.K_LEFT:
        command = "left"
    elif event.key == pygame.K_RIGHT:
        command = "right"

    return command

def predict_collition(tetromino, command):
    control_tetromino(tetromino, command)
    return playfield.check_collision(tetromino)

def compute_current_tetromino():
    random_number = random.randint(0, 6)
    if random_number == 0:
        return LTetromino(3, Position(-2, 3), square_size)
    elif random_number == 1:
        return OTetromino(2, Position(-2, 4), square_size)
    elif random_number == 2:
        return TTetromino(3, Position(-2, 4), square_size)
    elif random_number == 3:
        return ITetromino(4, Position(-2, 3), square_size)
    elif random_number == 4:
        return ZTetromino(3, Position(-2, 3), square_size)
    elif random_number == 5:
        return STetromino(3, Position(-2, 3), square_size)
    elif random_number == 6:
        return JTetromino(3, Position(-2, 3), square_size)

def move_tetromino(command):
    if command != "down":
        return

    current_tetromino = playfield.get_current_tetromino()

    will_collide = predict_collition(current_tetromino.clone(), command)

    if not will_collide:
        current_tetromino.move(command)
    elif command == "down":
        playfield.drop_current_tetromino()
        playfield.set_current_tetromino(compute_current_tetromino())


def redraw_screen(screen, pygame):
    tetromino = playfield.get_current_tetromino()
    screen.fill(LIGHT_GREY)
    playfield.draw(screen, pygame)
    tetromino.draw(screen, pygame)
    pygame.display.flip()


# Game loop
running = True

playfield.set_current_tetromino(compute_current_tetromino())

while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            capture_key_event(event)
        elif event.type == pygame.USEREVENT:
            move_tetromino("down")
            redraw_screen(screen, pygame)

# Quit Pygame
pygame.quit()
