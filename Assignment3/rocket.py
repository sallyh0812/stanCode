"""
File: rocket.py
Name: Sally 111613025
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def head():
    """
    i=0: space*SIZE + '/'*1 + '\'*1 + space*SIZE
    i=1: space*(SIZE-1) + '/'*2 + '\'*2 + space*(SIZE-1)
    =>
    space*(SIZE-i) + '/'*(i+1) + '\'*(i+1) + space*(SIZE-i)
    """
    for i in range(SIZE):
        for j in range(SIZE - i):
            print(" ", end="")
        for k in range(i + 1):
            print("/", end="")
        for m in range(i + 1):
            print("\\", end="")
        for n in range(SIZE - i):
            print(" ", end="")
        print("")


def belt():
    """
    '+' + '='*SIZE*2 + '+'
    """
    print("+", end="")
    for i in range(SIZE * 2):
        print("=", end="")
    print("+")


def upper():
    """
    each line starts and ends with '|'
    i=0: '.'*(SIZE-1) + '/\'*1 + '.'*(SIZE-1)
    i=1: '.'*(SIZE-2) + '/\'*2 + '.'*(SIZE-2)
    =>
    '.'*(SIZE-1-i) + '/\'*(i+1) + '.'*(SIZE-1-i)
    """
    for i in range(SIZE):
        print("|", end="")
        for j in range(SIZE - 1 - i):
            print(".", end="")
        for k in range(i + 1):
            print("/", end="\\")  # '/\'
        for n in range(SIZE - 1 - i):
            print(".", end="")
        print("|")


def lower():
    """
    each line starts and ends with '|'
    i=0: '.'*(0) + '/\'*SIZE + '.'*(0)
    i=1: '.'*(1) + '/\'*(SIZE-1) + '.'*(1)
    =>
    '.'*(i) + '/\'*(SIZE-1) + '.'*(i)
    """
    for i in range(SIZE):
        print("|", end="")
        for j in range(i):
            print(".", end="")
        for k in range(SIZE - i):
            print("\\", end="/")
        for n in range(i):
            print(".", end="")
    print("|")


def main():
    """
    assemble the rocket
    head -> belt -> upper -> lower -> belt -> head
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
