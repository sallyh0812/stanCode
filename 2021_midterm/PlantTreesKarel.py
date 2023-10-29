from karel.stanfordkarel import *

"""
File: PlantTreesKarel.py
——————————————————————————————————
Karel begins at (1, 1) and needs to grow all the beepers on Street 1 to the height
with respect to the number of Beepers. The width and the height of the world are
not fixed! Attention: Python variables are not allowed in this problem.
"""


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


def back_to_street1():
    turn_around()
    while front_is_clear():
        move()
    turn_left()


def plant_tree():
    while on_beeper():
        pick_beeper()
        if not on_beeper():
            put_beeper()
            break
        turn_left()
        while on_beeper():
            move()
        put_beeper()
        back_to_street1()
        


def main():
    while front_is_clear():
        plant_tree()
        move()
    plant_tree()


if __name__ == '__main__':
    execute_karel_task(main)
