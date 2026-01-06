import random

choices = ["rock", "paper", "scissors"]

def play_game(user_choice):
    """Determine the winner of the game."""
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "Computer wins!"

    return {
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result
    }
