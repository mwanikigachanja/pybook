import streamlit as st
import pygame
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up Pygame window
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ludo")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define player colors
PLAYER_COLORS = [RED, GREEN, BLUE, YELLOW]

# Constants for board layout
CELL_SIZE = 50
START_X = 100
START_Y = 100
HOME_X = 50
HOME_Y = 50

# Initialize variables
num_players = 2
players = []
current_player = 0
dice_value = 0

# Define classes
class Piece:
    def __init__(self, color):
        self.color = color
        self.position = -1  # -1 represents piece not on the board

    def move(self, steps):
        if self.position == -1:
            return 0
        self.position += steps
        if self.position > 55:
            self.position -= 56
        return self.position

class Player:
    def __init__(self, color):
        self.color = color
        self.pieces = [Piece(color) for _ in range(4)]
        self.home_positions = [(HOME_X, HOME_Y), (HOME_X + CELL_SIZE, HOME_Y), (HOME_X, HOME_Y + CELL_SIZE), (HOME_X + CELL_SIZE, HOME_Y + CELL_SIZE)]

# Create players
def create_players(num_players):
    global players
    players = [Player(PLAYER_COLORS[i]) for i in range(num_players)]

# Draw the board
def draw_board():
    # Draw the outer square
    pygame.draw.rect(screen, WHITE, (START_X, START_Y, 4 * CELL_SIZE, 4 * CELL_SIZE))

    # Draw the home areas
    for player in players:
        for i, position in enumerate(player.home_positions):
            pygame.draw.rect(screen, player.color, (position[0], position[1], CELL_SIZE, CELL_SIZE))
    
    # Draw the safe squares
    safe_positions = [(2 * CELL_SIZE + START_X, START_Y), (START_X, 2 * CELL_SIZE + START_Y), (5 * CELL_SIZE + START_X, 2 * CELL_SIZE + START_Y), (2 * CELL_SIZE + START_X, 5 * CELL_SIZE + START_Y)]
    for position in safe_positions:
        pygame.draw.rect(screen, WHITE, (position[0], position[1], CELL_SIZE, CELL_SIZE))

# Draw the pieces
def draw_pieces():
    for player in players:
        for piece in player.pieces:
            if piece.position != -1:
                x = START_X + (piece.position % 14) * CELL_SIZE
                y = START_Y + (piece.position // 14) * CELL_SIZE
                pygame.draw.circle(screen, piece.color, (x, y), 20)

# Roll the dice
def roll_dice():
    global dice_value
    dice_value = random.randint(1, 6)

# Check if there's a winner
def check_winner():
    for player in players:
        if all(piece.position == 55 for piece in player.pieces):
            return player.color
    return None

# Main game loop
def main():
    global current_player
    create_players(num_players)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
        
        screen.fill(WHITE)
        draw_board()
        draw_pieces()

        st.text("Player {}'s Turn".format(current_player + 1))

        roll_button = st.button("Roll Dice")
        if roll_button:
            roll_dice()
            st.text("Dice Value: {}".format(dice_value))
            current_player = (current_player + 1) % num_players

        winner = check_winner()
        if winner:
            st.text("Player {} wins!".format(PLAYER_COLORS.index(winner) + 1))
            pygame.quit()
            return

        pygame.display.flip()

if __name__ == "__main__":
    main()
