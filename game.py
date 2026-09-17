
"""Controls the full Rock, Paper, Scissors tournament flow."""

from data import game_state
from one_round import get_player_choice, get_computer_choice, determine_winner
from utils import display_score


# Starts a new tournament and runs it until one side wins three rounds
def start_game():

    # Reset game state before starting a new tournament
    game_state["current_round"] = 1
    game_state["player_wins"] = 0
    game_state["computer_wins"] = 0

    # Continue playing until either side reaches three wins
    while (game_state["player_wins"] < 3 and game_state["computer_wins"] < 3):

        print()
        print(f"Round {game_state['current_round']}")

        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        round_winner = determine_winner(player_choice, computer_choice)

        if round_winner == "draw":
            print("Draw!")

        elif round_winner == "player":
            print("You win this round!")
            game_state["player_wins"] += 1

        else:
            print("Computer wins this round!")
            game_state["computer_wins"] += 1

        display_score()

        game_state["current_round"] += 1


    if game_state["player_wins"] == 3:
        print()
        print("You win the tournament!")
    else:
        print()
        print("Computer wins the tournament!")