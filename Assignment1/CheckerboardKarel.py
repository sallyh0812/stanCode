"""
File: CheckerboardKarel.py
Name: Sally 111613025
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1.
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
In this file, we use 0 represent empty while 1 represents beeper
"""

from karel.stanfordkarel import *


def main():
    """
    Karel determines whether current line should begins with 0 or 1
    based on the previous line, and fills lines one by one
    until approaching the upper boundary
    1: beeper 0: empty
    """

    fill_line_1()  # fill line start with 1
    while front_is_clear():  # check if Karel meets the upper boundary
        if on_beeper():  # next line start with 0
            move_to_next_line()
            fill_line_2()
        else:  # next line start with 1
            move_to_next_line()
            fill_line_1()


def fill_line_1():
    """
    Pre: at the left end of a line, facing East
    fill a line that begins with a beeper(1010101)
    Post: at the left end of a line, facing North, ready for the next line
    """
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    move_back()
    turn_left()


def fill_line_2():
    """
    Pre: at the left end of a line, facing East
    fill a line that begins with an empty place(010101)
    Post: at the left end of a line, facing North
    """
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()
    move_back()
    turn_left()


def move_to_next_line():
    """
    Pre: at the left end of the previous line, facing North
    Post: at the left end of a new line, facing East
    """
    move()
    turn_right()


def move_back():
    """
    Pre: at the right end of the line, facing East
    Post: back to the left end of the line, facing East
    """
    turn_around()
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
