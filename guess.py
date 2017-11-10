import random
from common_input import input_int
from common import game_loop

# The range of numbers to guess from
MIN = 1
MAX = 100


def play_game():
    """
    Plays one round of the guessing game.  The user can guess as many times as needed to guess a
    number between MIN and MAX.
    """
    number = random.randint(MIN, MAX)
    guess = 0
    print(f"I am thinking of a number between {MIN} and {MAX}.")
    while number != guess:
        guess = input_int("What's your guess? ", MIN, MAX)
        if number > guess:
            print("My number is higher than that.")
        elif number < guess:
            print("My number is less than that.")
    print("That's it - you got it!")


random.seed()
game_loop(play_game)
