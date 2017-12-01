"""
Shared methods to help manage games.
"""
from common_input import input_yes_no


def game_loop(game_func):
    """
    Will play the specified once, then prompt the user if they want to play again after game_func is over.  Will
    continue to prompt as long as the user wants to play.
    :param game_func: Function for the game to play.
    :return: None
    """
    while True:
        game_func()
        play_again = input_yes_no("Would you like to play again? ")
        if not play_again:
            break
    print("Thank you for playing!")
