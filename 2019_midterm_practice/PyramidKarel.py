from karel.stanfordkarel import *

"""
File: PyramidKarel.py
————————————————————————————
Karel paints a pyramid (an isosceles triangle) on the world,
where the width is greater than or equal to the height.
The pyramid starts at one street below where Karel stands on
at the beginning of the program. """


def main():
    turn_right()
    while front_is_clear():
        fill_avenue()
        turn_right()
        move()
        turn_right()
        move()


def fill_avenue():
    # facing south at the top
    while front_is_clear():
        move()
        put_beeper()
    turn_around()
    while on_beeper():
        move()
    # facing north at the top


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


if __name__ == '__main__':
    execute_karel_task(main)
