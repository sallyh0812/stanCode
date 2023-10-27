"""
File: CollectNewspaperKarel.py
Name: Sally 111613025
--------------------------------
Karel is at the North West of the house(4,3) facing East. Through this function Karel can walk to the door (3,5),
pick up the newspaper at Street 3, Avenue 6 (3,6) (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house, facing East.
"""

from karel.stanfordkarel import *


def main():
    """
    walk to the door (5,3), pick up the newspaper (6,3), return, put the newspaper
    """
    move_to_newspaper()
    go_home()


def move_to_newspaper():
    """
    Pre: Karel is at (4,3), facing East
    Post: Karel is at (3,6), facing East
    Karel follows the path (4,3) -> (3,5) -> (3,6)
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()


def go_home():
    """
    Pre: Karel is at (3,6), facing East
    Post: Karel is at (4,3), facing East
    Karel follows the path (3,6) -> (3,5) -> (4,3)
    """

    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_around()
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
