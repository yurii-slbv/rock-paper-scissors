
"""Contains helper function for displaying game information."""

from data import game_state


# Displays the current score
def display_score():
    print(f"Score: Player {game_state['player_wins']} - " 
          f"Computer {game_state['computer_wins']}")