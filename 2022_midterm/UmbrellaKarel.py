from karel.stanfordkarel import *

"""
File: UmbrellaKarel.py
————————————————————————————
Karel uses beepers to construct an umbrella in its world. Karel will start from the
midpoint of street1 and back to the origin after its construction. The world may be
of any size, but you are allowed to assume that it is at least as tall as its wide, while
the number of its streets and avenues will be odd.
"""


def main():
    fill_column()
    turn_right()
    right_triangle()
    turn_around()
    fill_row()
    turn_right()
    right_triangle()
    turn_around()
    move_to_origin()


def fill_column():
    while front_is_clear():
        put_safe()
        move()
    put_safe()


def right_triangle():
    while front_is_clear():
        move()
        turn_right()
        move()
        put_safe()
        turn_left()


def put_safe():
    if not on_beeper():
        put_beeper()


def fill_row():
    while front_is_clear():
        put_safe()
        move()
    put_safe()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


def move_to_origin():
    while front_is_clear():
        move()
    turn_around()


if __name__ == '__main__':
    execute_karel_task(main)
