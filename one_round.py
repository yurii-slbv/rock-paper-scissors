
"""Contains the main game logic and player/computer choice functions."""

import random
from data import choices


# Gets and validates the player's choice
def get_player_choice():
    player_choice = input("Choose rock, paper, or scissors: ").lower()

    while player_choice not in choices:
        print("Invalid choice. Try again.")
        player_choice = input("Choose rock, paper, or scissors: ").lower()

    return player_choice


# Returns a random choice for the computer
def get_computer_choice():
    return random.choice(choices)


# Determines the winner of the round
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"

    elif (player_choice == "rock" and computer_choice == "scissors"
        or player_choice == "paper" and computer_choice == "rock"
        or player_choice == "scissors" and computer_choice == "paper"):
        return "player"

    else:
        return "computer"