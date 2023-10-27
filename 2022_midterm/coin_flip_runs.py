"""
File: coin_flip_runs.py
-----------------------
This program should simulate coin flip(s) with the number of runs input by users. A
'run' is defined as consecutive results on either 'H' or 'T'. For example,
‘HHHHHTHTT' is regarded as a 2-run result. Your program should stop immediately
after your coin flip results reach the number of runs!
"""
import random


def main():
    # random.seed(0)
    print("Let's flip a coin!")
    n = int(input("Number of runs: "))
    rolls = ""
    while True:
        rolls += str(random.randrange(0, 2))  # .randint(0,1)
        if check_repeat(rolls) >= n:
            break
    
    print(num_to_th(rolls))


def check_repeat(s):
    now = ""
    repeat = 0
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            if s[i] != now:
                repeat += 1
                now = s[i]
        
        else:
            now = ""
    return repeat


def num_to_th(s):
    ans = ""
    for ch in s:
        if ch == '0':
            ans += 'T'
        else:
            ans += 'H'
    return ans


if __name__ == '__main__':
    main()
