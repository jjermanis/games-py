#!/usr/bin/env python3
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
    # TODO: implement move limit... ceiling of lg(range)... 7 moves for 1-100
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


def main():
    random.seed()
    game_loop(play_game)


if __name__ == "__main__":
    main()
