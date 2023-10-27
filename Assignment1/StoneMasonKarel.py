"""
File: StoneMasonKarel.py
Name: Sally 111613025
--------------------------------
Karel can build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Then end on the last avenue, 1st Street, facing east.
"""

from karel.stanfordkarel import *


def main():
    """
    fill the pillar, move 4 to the right for the next pillar, until right is not clear
    """

    while front_is_clear():
        fill_pillar()
        for i in range(4):
            move()
    fill_pillar()


def fill_pillar():
    """
    Pre: facing East, at the bottom
    Karel fills the pillar then returns to the start point
    Post: facing East, at the bottom
    """
    turn_left()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
            move()
        else:
            move()
    if not on_beeper():
        put_beeper()

    # move back
    turn_around()
    while front_is_clear():
        move()
    turn_left()


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
