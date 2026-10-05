# Scissors Paper Stone

An extremely simple terminal-based scissors-paper-stone game made using Python, with coloured output and a typewriter animation for that old-school terminal feel. Made this to strengthen my python basics.

## Demo

```
==== SCISSORS PAPER STONE [cmd edition] ===

Press enter to start

Scissors, Paper or Stone: stone
PLAYER WINS
You chose stone. Computer chose scissors.
Press enter to continue. To quit, enter 'q'.

Scissors, Paper or Stone: scissors
DRAW
You chose scissors. Computer chose scissors.
Press enter to continue. To quit, enter 'q'.

Scissors, Paper or Stone: paper
DRAW
You chose paper. Computer chose paper.
Press enter to continue. To quit, enter 'q'.

Scissors, Paper or Stone: scissors
COMPUTER WINS
You chose scissors. Computer chose stone.
Press enter to continue. To quit, enter 'q'.

Scissors, Paper or Stone: banana
Please enter a valid move.

Scissors, Paper or Stone: stone
PLAYER WINS
You chose stone. Computer chose scissors.
Press enter to continue. To quit, enter 'q'.

Scissors, Paper or Stone: paper
DRAW
You chose paper. Computer chose paper.
Press enter to continue. To quit, enter 'q'. q

Thanks for playing.


Stats:

Player wins: 2
Computer wins: 1
Draws: 3

```

## Running it

Requires Python 3. No external packages.

```
python sps.py
```

## Features

- Input validation that accepts any casing or stray whitespace
- Display stats at the end of your session
- ANSI colour output (green win, red loss, yellow draw)
- Character-by-character print animation
- Quit any time with `q` or `quit`

## How it works

The win condition is a single dictionary lookup rather than a chain of
nine comparisons:

```python
beats = {"scissors": "paper", "paper": "stone", "stone": "scissors"}

if computer_choice == beats[player_choice]:
    # player wins
```

## Similar future project built on this

- LAN multiplayer over sockets, so two players on the same wifi can play
  against each other