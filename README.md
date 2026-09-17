# Rock, Paper, Scissors Tournament

A simple terminal-based Rock, Paper, Scissors tournament built in Python as part of the Ironhack Data Analytics Bootcamp.

## Game Objective

The player competes against the computer in a Rock, Paper, Scissors tournament.

The first side to win three rounds wins the tournament.

## Game Rules

- Rock beats scissors
- Scissors beats paper
- Paper beats rock
- If both sides choose the same option, the round is a draw
- The game continues until either the player or the computer reaches three wins

## Features

- Player input validation
- Random computer choices
- Score tracking
- Round tracking
- Win and lose conditions
- Automatic game state reset
- Modular Python structure

## Project Structure

```text
Rock, Paper, Scissors/
│
├── main.ipynb
├── mvp+.ipynb
├── data.py
├── one_round.py
├── game.py
├── utils.py
├── README.md
└── .gitignore
```

### main.ipynb

Main notebook used to import and start the game.

### data.py

Stores the available choices and the current game state.

### one_round.py

Contains the logic for one round:

- Gets and validates the player's choice
- Generates the computer's choice
- Determines the winner of the round

### game.py

Controls the complete tournament flow.

It resets the game state, runs the rounds, updates the score, and displays the tournament winner.

### utils.py

Contains helper functions used to display game information.

### mvp+.ipynb

Stores an earlier MVP version of the project before the code was separated into Python modules.

## Game State

The game state is stored in a dictionary:

```python
game_state = {
    "current_round": 1,
    "player_wins": 0,
    "computer_wins": 0
}
```

The dictionary is updated throughout the tournament.

## Input Validation

The player can enter:

```text
rock
paper
scissors
```

The input is cleaned using:

```python
.strip().lower()
```

Invalid inputs are rejected and the player is asked to try again.

## How to Run

Open `main.ipynb` and run the cells.

The notebook imports the main game function:

```python
from game import start_game
```

Then starts the tournament:

```python
start_game()
```

## Python Concepts Used

This project demonstrates:

- Lists
- Dictionaries
- Functions
- `if / elif / else`
- `while` loops
- Modules and imports
- Input validation
- Random selection
- Game state management
- Docstrings and comments

## Project Status

The game is fully playable from start to finish and includes the required functionality for the Rock, Paper, Scissors Tournament project.