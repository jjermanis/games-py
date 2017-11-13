import random
from common_input import input_int
from common import game_loop

# The range of numbers to guess from
MIN = 1
MAX = 100


def play_game():
    """
    Plays one round of the stars guessing game.  The user can guess as many times as needed to guess a
    number between MIN and MAX.  On each round, the user is shown stars depending on how close they are.
    The distance is based on a power of two: 7 stars for a guess 1 number away, 6 stars for 2 away, 5 stars
    for 3 away... and so on.
    """
    # TODO: implement move limit... 7 moves for 1 to 100
    number = random.randint(MIN, MAX)
    guess = 0
    print(f"I am thinking of a number between {MIN} and {MAX}.")
    while number != guess:
        guess = input_int("What's your guess? ", MIN, MAX)
        if number != guess:
            diff = abs(number - guess)
            star_count = 8
            while diff >= 1:
                diff //= 2
                star_count -= 1
            print(star_count * "*")
    print("That's it - you got it!")


random.seed()
print(f"This is the game of Stars.  I will think of a number between {MIN} and {MAX}, and ask you to guess. After you")
print("guess I will show you from 1 to 7 stars, depending on how close your guess was - 7 is very close, 1 is not")
print("close at all.  Good luck!")
game_loop(play_game)
