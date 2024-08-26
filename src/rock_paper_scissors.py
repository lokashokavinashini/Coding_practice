""" A script for playing Rock, Paper, Scissors with Computer """


def get_user_choice():
    """To get user's choice"""
    user_choice = input("Which do you choose: Rock, Paper, Scissors?")
    return user_choice


def get_computer_choice():
    """To get computer's choice"""
    return None


def determine_winner(user_choice, computer_choice):
    """Determine who is the winner and display the result"""
    print(user_choice)
    print(computer_choice)
    return None


user_choice = get_user_choice()
computer_choice = get_computer_choice()
result = determine_winner(user_choice, computer_choice)
print("Winner is : ",result)
