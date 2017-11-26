# Ported from Basic Computer Games from David Ahl
# Original game was TBD

from common_input import input_int
from common import game_loop

GRAVITY = 5
MAX_BURN = 30
START_HEIGHT = 500
START_VELOCITY = 50
START_FUEL = 120


def get_burn(fuel):
    if fuel > 0:
        burn = input_int("? ", 0, MAX_BURN)
        burn = min(burn, fuel)
        if fuel == burn:
            print("*** FUEL EXHAUSTED ***")
    else:
        burn = 0
    return burn


def sqrt(x):
    return x**0.5


def play_game():

    # Starting flight parameters
    time = 0
    altitude = START_HEIGHT
    velocity = START_VELOCITY
    fuel = START_FUEL

    # Each iteration through the loop represents one second
    while altitude > 0:
        # TODO: make this look nicer
        print(f"T:{time}, A:{altitude}, V:{velocity}, F:{fuel}")
        burn = get_burn(fuel)
        fuel -= burn
        accel = GRAVITY - burn
        new_velocity = velocity + accel
        # Note: this logic checks the altitude at the end of the second.  It does NOT check if there is a
        # touchdown before then.  This bug carries over from the original game.
        new_altitude = altitude - (velocity + new_velocity) / 2
        if altitude > 0:
            time += 1
            velocity = new_velocity
            altitude = new_altitude

    # Touchdown.  Calculate landing time and velocity.
    # Calculate fraction of second for touchdown
    if accel == 0:
        # Constant velocity.  Simple linear equation.
        fraction = altitude / velocity
    else:
        # Use quadratic formula to calculate intercept
        fraction = (-velocity+sqrt(velocity*velocity+altitude*(2*accel)))/accel
    time += fraction
    velocity = velocity+accel*fraction
    print(f"Touchdown at {time} seconds.")
    print(f"Landing velocity {velocity} ft/sec.")


# TODO: show directions
game_loop(play_game)
