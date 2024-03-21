import streamlit as st
import random

# Constants
NUM_PLAYERS = 4
NUM_PIECES = 4
NUM_CELLS = 56

# Initialize players and their pieces
players = [{'color': 'Red', 'pieces': [0] * NUM_PIECES},
           {'color': 'Green', 'pieces': [0] * NUM_PIECES},
           {'color': 'Blue', 'pieces': [0] * NUM_PIECES},
           {'color': 'Yellow', 'pieces': [0] * NUM_PIECES}]

# Initialize game variables
current_player = 0
dice_value = 0

# Roll the dice
def roll_dice():
    return random.randint(1, 6)

# Move a piece
def move_piece(player_idx, piece_idx, steps):
    players[player_idx]['pieces'][piece_idx] += steps
    players[player_idx]['pieces'][piece_idx] %= NUM_CELLS

# Check if a piece can move
def can_move_piece(player_idx, piece_idx, steps):
    if players[player_idx]['pieces'][piece_idx] + steps >= NUM_CELLS:
        return False
    return True

# Main game loop
def main():
    global current_player, dice_value
    
    st.title("Ludo Game")

    # Roll the dice
    if st.button("Roll Dice"):
        dice_value = roll_dice()
        st.write(f"Player {players[current_player]['color']} rolled a {dice_value}")

        # Move a piece
        piece_to_move = st.selectbox(f"Select a piece to move:", range(NUM_PIECES))
        if can_move_piece(current_player, piece_to_move, dice_value):
            move_piece(current_player, piece_to_move, dice_value)
            st.write(f"Piece {piece_to_move} moved successfully!")

        # Switch to the next player
        current_player = (current_player + 1) % NUM_PLAYERS

    # Display the game state
    st.write("Current Game State:")
    for player in players:
        st.write(f"Player {player['color']}: {player['pieces']}")

if __name__ == "__main__":
    main()
