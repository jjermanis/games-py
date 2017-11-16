import random
from common_input import input_int, input_letter
from common import game_loop


def optimal_move(left, right):
    """
    Optimal strategy is to end each move at a set of totals which cannot reach the victory condition...
    or a set of totals which cannot reach any other set which cannot reach the victory condition.
    """
    optimal_path = [(0, 0), (1, 2), (3, 5), (4, 7), (6, 10)]

    def result(x, y, is_x_left):
        return (x, y) if is_x_left else (y, x)

    if left <= right:
        a, b = left, right
        is_a_left = True
    else:
        a, b = right, left
        is_a_left = False

    for opt_a, opt_b in optimal_path:
        if b - a == opt_b - opt_a and a > opt_a:
            return a - opt_a, a - opt_a
        elif a == opt_a and b > opt_b:
            return result(0, b - opt_b, is_a_left)
        elif b == opt_b and a > opt_a:
            return result(a - opt_a, 0, is_a_left)
        elif a == opt_b:
            return result(0, b - opt_a, is_a_left)
    # Opponent is on the optimal strategy.  Make a small random move.
    return result(1, 0, random.randint(1, 2) > 1)


def play_game():

    def is_win():
        return left == right == 0

    left = right = 10
    # Do first player prompt out of the main loop to enforce not allowing Both on first move.
    print(f"Left heap has {left}. Right heap has {right}.")
    player_move = input_letter("Will you take from Left or Right? ", "LR")
    while not is_win():
        if player_move == "L":
            max_count = left
        elif player_move == "R":
            max_count = right
        else:
            max_count = left if left < right else right
        player_count = input_int("How many? ", 1, max_count)
        if player_move == "L":
            left -= player_count
        elif player_move == "R":
            right -= player_count
        else:
            left -= player_count
            right -= player_count

        print(f"Left heap has {left}. Right heap has {right}.")
        if is_win():
            print("You win!")
            break
        left_move, right_move = optimal_move(left, right)
        print(f"Computer takes {left_move} from Left and {right_move} from Right.")
        left, right = left - left_move, right - right_move
        if is_win():
            print("Computer wins.")
            break
        print(f"Left heap has {left}. Right heap has {right}.")
        player_move = input_letter("Will you take from Left, Right, or Both? ", "LRB")


random.seed()
print("Welcome to the game of Two Heaps.  There are two heaps, Left and Right, with ten gems each.  The winner is")
print("the player who takes the last of the gem(s), from all 20 gems. On your turn, you can take as many gems as")
print("you want, from either pile. You CAN take from Both piles, but you need to take the exact same amount from")
print("both piles.")
print("Warning: I am a tough opponent.  I can be beaten (every time), but you have to play perfectly.  Good luck!")
print()
game_loop(play_game)
