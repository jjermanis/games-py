import random

# The range of numbers to guess from
MIN = 1
MAX = 100


def user_guess():
    """
    :return: An int for the user's guess, between MIN and MAX (inclusive)
    """
    error_prompt = f"I'm looking for a number between {MIN} and {MAX}"
    while True:
        try:
            result = int(input("What's your guess? "))
            if result < MIN or result > MAX:
                print(error_prompt)
            else:
                return result
        except ValueError:
            print(error_prompt)


def play_game():
    """
    Plays one round of the guessing the game.  The user can guess as many times as needed to guess a
    number between MIN and MAX.
    """
    number = random.randint(MIN, MAX)
    guess = 0
    print(f"I am thinking of a number between {MIN} and {MAX}.")
    while number != guess:
        guess = user_guess()
        if number > guess:
            print("My number is higher than that.")
        elif number < guess:
            print("My number is less than that.")
    print("That's it - you got it!")


random.seed()
play_game()
while True:
    prompt = input("Would you like to play again? ")
    if prompt and prompt[0] == 'y':
        play_game()
    elif prompt and prompt[0] == 'n':
        break
    else:
        print("I didn't understand - please respond yes or no.")
print("Thank you for playing!")
