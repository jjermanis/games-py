# Ported from Basic Computer Games by David Ahl

from common_input import input_int
from common import game_loop

GRAVITY = 5
MAX_BURN = 30
START_ALTITUDE = 500
START_VELOCITY = 50
START_FUEL = 120
GOOD_LANDING = 4


def show_instructions():
    print(f"")
    print(f"You are landing on the moon and have taken over manual control on final approach.")
    print(f"You are at an altitude of {START_ALTITUDE} feet, and are descending at {START_VELOCITY} feet/sec.")
    print(f"Acceleration due to gravity is {GRAVITY} feet/sec/sec.  You have {START_FUEL} units of fuel.")
    print(f"")
    print(f"You will be prompted every second for how much fuel to burn for that second.  One")
    print(f"unit of fuel per second provides upward acceleration of 1 ft/sec/sec.  The maximum burn ")
    print(f"rate per second is {MAX_BURN} units.  Your craft has been engineered to land safely at up to")
    print(f"{GOOD_LANDING} feet per second.")
    print(f"")
    print(f"On each turn, you will see the current time, altitude, velocity, remaining fuel, and")
    print(f"a graphical altitude indicator.  Best of luck!")
    print(f"")


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


def show_status(time, altitude, velocity, fuel):
    spacer = START_ALTITUDE // 80
    template = "T:{0:>3}  A:{1:>6.1f}  V:{2:>5.1f}  F:{3:>4}   I{4}*"
    disp = template.format(time, altitude, velocity, fuel, "-" * (int(altitude) // spacer))
    print(disp)


def show_landing_report(time, velocity):
    print("Touchdown at {0:.3f} seconds.".format(time))
    print("Landing velocity {0:.2f} ft/sec.".format(velocity))

    if velocity <= GOOD_LANDING * 0.25:
        print("Amazing landing!  The craft is in perfect shape.")
    elif velocity <= GOOD_LANDING:
        print("Good landing - proceed to lunar surface.")
    elif velocity <= GOOD_LANDING * 2:
        print("The craft is damaged.  Mission abort - return to orbit.")
    elif velocity <= GOOD_LANDING * 4:
        print("The craft is severly damaged.  Sorry - craft cannot return to orbit.")
    else:
        print("The craft broke up on impact.  Next of kin notified.")


def play_game():

    # Starting flight parameters
    time = 0
    altitude = START_ALTITUDE
    velocity = START_VELOCITY
    fuel = START_FUEL
    accel = 0

    # Each iteration through the loop represents one second
    while altitude > 0:
        show_status(time, altitude, velocity, fuel)
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
    show_landing_report(time, velocity)


if __name__ == "__main__":
    show_instructions()
    game_loop(play_game)
