from karel.stanfordkarel import *

"""
File: PyramidKarel.py
————————————————————————————
Karel paints a pyramid (an isosceles triangle) on the world,
where the width is greater than or equal to the height.
The pyramid starts at one street below where Karel stands on
at the beginning of the program. """


def main():
    put_side()
    while right_is_clear():
        go_to_previous_avenue()
        fill_avenue()


def fill_avenue():
    # facing north at street 1
    while not on_beeper():
        if front_is_clear():
            put_beeper()
            move()
    turn_around()
    while front_is_clear():
        move()
    # facing north at street 1


def put_side():
    # Karel at northwest corner facing east
    turn_right()
    while front_is_clear():
        move()
        put_beeper()
        turn_left()
        move()
        turn_right()
    # Karel at street 1, empty square, facing south


def go_to_previous_avenue():
    # facing south at street 1
    turn_right()
    move()
    turn_right()
    # facing north at street 1 at previous avenue


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


if __name__ == '__main__':
    execute_karel_task(main)
