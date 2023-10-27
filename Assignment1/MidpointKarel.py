"""
File: MidpointKarel.py
Name: Sally 111613025
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    fill the whole line, pick up beepers from the two ends, until only one left
    By this way, we can determine the midpoint
    """
    fill_beeper()
    pick_end_beeper()
    place_mid_beeper()


def fill_beeper():
    """
    Pre: at the left end, facing east
    fill the whole line with beeper
    Post: at the right end, facing east
    """
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


def pick_end_beeper():
    """
    Pre: at the right end on the beeper
    Karel picks beeper from two ends (in turn), stops after picking up the last one
    Post: stop next to the midpoint (if not 1*1), not on beeper
    """
    while on_beeper():
        if front_is_clear():
            move()
            if not on_beeper():
                turn_around()
                move()
                pick_beeper()
                if front_is_clear():
                    move()
        else:
            pick_beeper()
            turn_around()
            if front_is_clear():
                move()


def place_mid_beeper():
    """
    Karel goes back to where the last beeper is (the midpoint), then stop and put beeper
    """
    # go back to midpoint
    turn_around()
    if front_is_clear():
        move()
    put_beeper()


def turn_around():
    """
    Karel turns left twice
    """
    turn_left()
    turn_left()


def turn_right():
    """
    Karel turns left three times
    """
    for i in range(3):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
