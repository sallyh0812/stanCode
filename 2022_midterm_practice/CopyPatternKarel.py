from karel.stanfordkarel import *

""" 
File: CopyPatternKarel.py 
—————————————————————————————————— 
Karel begins at (1, 1) and needs to copy all the beepers from Avenue 2-5 
to Avenue 7-10. The width of the world is fixed (10 Avenues), however, 
the height of the world is a random number bigger than or equal to 1. 
"""


def main():
    move()
    while left_is_clear():
        copy_street()
        back_to_avenue2()
        go_to_next_street()
    copy_street()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


def move_4():
    for i in range(4):
        move()


def move_5():
    for i in range(5):
        move()


def back_to_avenue2():
    turn_around()
    move_4()
    turn_around()


def copy_street():
    for i in range(4):
        if on_beeper():
            move_5()
            put_beeper()
            turn_around()
            move_5()
            turn_around()
        move()


def go_to_next_street():
    turn_left()
    move()
    turn_right()


if __name__ == '__main__':
    execute_karel_task(main)
