from karel.stanfordkarel import *

"""
File: PyramidKarel_ans.py
————————————————————————————
Karel paints a pyramid (an isosceles triangle) on the world,
where the width is greater than or equal to the height.
The pyramid starts at one street below where Karel stands on
at the beginning of the program. """


def main():
    turn_right()
    safe_move()
    while front_is_clear():
        beeper_line()
        back_to_start()
        move_to_next()
    turn_left()
    if not on_beeper():
        put_beeper()


def beeper_line():
    while front_is_clear():
        put_beeper()
        move()
    if not on_beeper():
        put_beeper()


def back_to_start():
    turn_around()
    while on_beeper():
        move()


def move_to_next():
    turn_right()
    safe_move()
    turn_right()
    safe_move()
    safe_move()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


def safe_move():
    if front_is_clear():
        move()


if __name__ == '__main__':
    execute_karel_task(main)
