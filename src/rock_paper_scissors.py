""" A script for playing Rock, Paper, Scissors with Computer """
import random
def get_user_choice():
    '''
    Prompts the user to enter their choice of Rock, Paper, or Scissors.
    Converts the input to lowercase to ensure case insensitivity.
    Returns the user's choice if it's valid; otherwise, prompts again.
    '''
    choice = input("Enter Rock, Paper, or Scissors: ").lower()
    if choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice, please try again.")
        return get_user_choice()
    return choice


def get_computer_choice():
    """
    Randomly selects and returns the computer's choice of Rock, Paper, or Scissors.
    """
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user_choice, computer_choice):
    """
    Determines the winner based on the user's choice and the computer's choice.
    Returns a string indicating whether the user wins, loses, or ties.
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"


def play_game():
    """
    Runs the Rock-Paper-Scissors game.
    Gets the user's and computer's choices, determines the winner, and prints the result.
    """
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)


# Start the game
play_game()
