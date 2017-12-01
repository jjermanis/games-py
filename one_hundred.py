#!/usr/bin/env python3
import random
from common_input import input_int
from common import game_loop


def optimal_move(total):
    """
    Optimal strategy is to end each move on 11x+1 (e.g. 12, 23, 34,...)
    :return: The optimal move given the current total
    """
    if (total-1) % 11 == 0:
        # Opponent is on the optimal path.  Try a random move.
        return random.randint(1, 10)
    else:
        # Stay on the optimal path
        return 11 - (total-1) % 11


def play_game():
    total = 0
    while total < 100:
        player_move = input_int("Your move? ", 1, 10)
        total += player_move
        print(f"Total is {total}.")
        if total >= 100:
            print("You win!")
            break
        cpu_move = optimal_move(total)
        total += cpu_move
        print(f"Computer plays {cpu_move}.  Total is {total}.")
        if total >= 100:
            print("Computer wins.")
            break


def main():
    random.seed()
    print("Welcome to the game of One Hundred.  You and I will play against each other.  On each turn, we can play any")
    print("number between 1 and 10, which is added to the Total.  The player who gets the Total to 100 or more points")
    print("wins.")
    print("Warning: I am a tough opponent.  I can be beaten (every time), but you have to play perfectly.  Good luck!")
    print()


if __name__ == "__main__":
    game_loop(play_game)
