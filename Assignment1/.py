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
    TODO: fill the whole line, pick up beepers from the two end, until only one left
    """

    while front_is_clear():
        move()
        turn_left()
        if front_is_clear():
            move()
            if front_is_clear():
                move()
                turn_right()
        else:
            turn_around()
            move_to_end()


def fill_beeper():
    """
    fill the whole line with deeper
    """
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


# def move_on_beeper():
#     while on_beeper():
#         if front_is_clear():
#             move()
#     turn_around()


def move_backwards():
    """
    move backwards
    """
    turn_around()
    move()
    turn_around()


def move_to_end():
    """
    move to the end and facing the center
    """
    while front_is_clear():
        move()
    turn_around()


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
