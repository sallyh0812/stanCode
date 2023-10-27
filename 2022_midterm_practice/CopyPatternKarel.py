from karel.stanfordkarel import *

""" 
File: CopyPatternKarel.py 
—————————————————————————————————— 
Karel begins at (1, 1) and needs to copy all the beepers from Avenue 2-5 
to Avenue 7-10. The width of the world is fixed (10 Avenues), however, 
the height of the world is a random number bigger than or equal to 1. 
"""


def main():
    # Your Code Here
    move()
    while front_is_clear():
        for i in range(4):
            if on_beeper():
                move_to_b()
                put_beeper()
                move_to_a()
            move()
        move_back()
        if front_is_clear():
            move()
            turn_right()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


def move_to_a():
    turn_around()
    for i in range(5):
        move()
    turn_around()


def move_to_b():
    for i in range(5):
        move()


def move_back():
    turn_around()
    for i in range(4):
        move()
    turn_right()


if __name__ == '__main__':
    execute_karel_task(main)
