import random

"""
File: count_runs.py
———————————————————————————————————
This program simulates a certain number of die-roll results and calculates
how many consecutive number (defined as runs) appears.
"""
# This constant controls the number of rolls
NUM_ROLLS = 15


def main():
    # random.seed(0)
    rolls = ""
    for i in range(NUM_ROLLS):
        a = random.randrange(1, 7)
        rolls += str(a)
        print(f"Rolls: {a}")
    print(f"Number of runs: {count_runs(rolls)}")


def count_runs(s):
    repeat = False
    run = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            if not repeat:
                run += 1
                repeat = True
        else:
            repeat = False
    return run


if __name__ == "__main__":
    main()
