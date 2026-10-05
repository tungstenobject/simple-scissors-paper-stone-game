import random
import time

RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
CYAN = "\033[36m"
BEIGE = "\033[38;5;223m"
RESET = "\033[0m"

def print_animation(text):
    for char in text:
        print(char, end = "", flush = True)
        time.sleep(0.02)
    print()

def input_animation(text):
    for char in text:
        print(char, end = "", flush = True)
        time.sleep(0.02)
    return input()

def sps():

    moves = ["scissors", "paper", "stone"]
    beats = {"scissors": "paper", "paper": "stone", "stone": "scissors"}

    player_wins = 0
    computer_wins = 0
    draws = 0

    while True:

        player_choice = input_animation("Scissors, Paper or Stone: ").strip().lower()
        if player_choice not in moves:
            print(f"{RED}Please enter a valid move.{RESET}")
            print("")
            time.sleep(0.75)
            continue

        computer_choice = random.choice(moves)

        time.sleep(1)

        if player_choice == computer_choice:
            print_animation(f"{YELLOW}DRAW{RESET}")
            draws += 1

        elif computer_choice == beats[player_choice]:
            print_animation(f"{GREEN}PLAYER WINS{RESET}")
            player_wins += 1

        else:
            print_animation(f"{RED}COMPUTER WINS{RESET}")
            computer_wins += 1

        print_animation(f"You chose {BEIGE}{player_choice}{RESET}. Computer chose {BEIGE}{computer_choice}{RESET}.")
        
        time.sleep(1)

        post_game = input_animation(f"Press {CYAN}enter{RESET} to continue. To {RED}quit{RESET}, enter '{RED}q{RESET}'. ")
        print("")

        if post_game.strip().lower() == "q" or post_game.strip().lower() == "quit":
            break

    print_animation(f"{BEIGE}Thanks for playing. {RESET}")

    print("")
    print("")
    print_animation("Stats:")
    print("")
    print_animation(f"Player wins: {GREEN}{player_wins}{RESET}")
    print_animation(f"Computer wins: {RED}{computer_wins}{RESET}")
    print_animation(f"Draws: {YELLOW}{draws}{RESET}")
    print("")

    time.sleep(1)

print("")
print("==== SCISSORS PAPER STONE [cmd edition] ===")
print("")
input(f"Press {BEIGE}enter{RESET} to start\n")

sps()
