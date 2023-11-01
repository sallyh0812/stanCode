"""
File: shi_ba_la.py
—— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— ——
This program simulates a game called shi-ba-la.
The program first asks the user to input the number of players, and then shows
the randomly generated results of each players. All results shown on Console
should be valid.
"""
import random


def main():
    print('Welcome to stanCode shi-ba-la!')
    num_players = int(input("Number of players: "))
    for i in range(num_players):
        print(f"Player {i+1}: {rolls()}")
    print("Thanks for playing!")


def rolls():
    while True:
        ans = ""
        for i in range(4):
            ans += str(random.randrange(1, 7))
        if repeat_num(ans) == 2 or repeat_num(ans) == 4:
            return ans


def repeat_num(s):
    for i in range(len(s)):
        repeat = 0
        for j in range(len(s)):
            if s[j] == s[i]:
                repeat += 1
        if repeat >= 2:
            return repeat
    return repeat


if __name__ == '__main__':
    main()
