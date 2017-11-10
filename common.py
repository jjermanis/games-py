from common_input import input_yes_no


def game_loop(game_func):
    while True:
        game_func()
        play_again = input_yes_no("Would you like to play again? ")
        if not play_again:
            break
    print("Thank you for playing!")
