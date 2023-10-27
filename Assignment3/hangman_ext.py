"""
File: hangman_ext.py
Name: Sally 111613025
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def make_hint(ans, guess, old_h):
    """
    :param ans: str, the answer
    :param guess: char, the guess alphabet
    :param old_h: str, old hint
    :return: new_h, str, the updated hint
    Guess right -> add the correct alphabet into new_h
    Wrong -> keep the char in old_h (may be '-' or an alphabet that has been guessed before)
    """
    new_h = ""
    for j in range(len(ans)):
        if guess == ans[j]:
            new_h += ans[j]
        else:
            new_h += old_h[j]
    return new_h


def main():
    """
    Get a random answer, let user guess one character each time,
    until user gets all characters or has zero turns remained
    User has 7 turns at the beginning, each time he guesses wrong turns-=1.
    """
    ans = random_word()
    turns_left = N_TURNS
    
    # initialize hint_now
    hint_now = ""
    for i in range(len(ans)):
        hint_now += '-'
    
    while (turns_left > 0) and (hint_now != ans):
        print(f"The word looks like: {hint_now}")
        print(f"You have {turns_left} wrong guesses left.")
        hang(turns_left)
        guess = input("Your guess: ").upper()
        
        # ask for input again until a legal format
        while (not guess.isalpha()) or len(guess) != 1:
            print("Illegal format.")
            guess = input("Your guess: ").upper()
        
        # determine whether the user guess is correct or not
        if ans.find(guess) != -1:  # correct
            print("You are correct!")
            hint_now = make_hint(ans, guess, hint_now)
        else:
            print(f"There is no {guess.upper()}'s in the word.")
            turns_left -= 1
    
    # determine why the while loop break and show different result
    if hint_now == ans:
        print("You win!!")
        print(f"The answer is: {ans}")
        hang(turns_left)
    else:
        print("You are completely hung :(")
        hang(turns_left)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def hang(x):
    if x == 7:
        draw_0()
    elif x == 6:
        draw_1()
    elif x == 5:
        draw_2()
    elif x == 4:
        draw_3()
    elif x == 3:
        draw_4()
    elif x == 2:
        draw_5()
    elif x == 1:
        draw_6()
    else:
        draw_7()


def draw_0():
    print("""
      +---+
      |   |
          |
          |
          |
          |
    =========
    """)


def draw_1():
    print("""
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """)


def draw_2():
    print("""
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        """)


def draw_3():
    print("""
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        """)


def draw_4():
    print("""
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========
        """)


def draw_5():
    print("""
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
        =========
        """)

    
def draw_6():
    print("""
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========
        """)
 
   
def draw_7():
    print("""
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        =========
        """)


#  DO NOT EDIT THE CODE BELOW THIS LINE  #
if __name__ == '__main__':
    main()
