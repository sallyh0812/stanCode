import random


def main():
    print("Let's flip a coin!")
    n = int(input("Number of runs: "))
    repeat = False
    rolls = ""
    while n:
        if random.randint(0, 1) == 0:
            roll = 'T'
        else:
            roll = 'H'
        
        if len(rolls):
            current = rolls[-1]
            if roll == current:
                if not repeat:
                    repeat = True
                    n -= 1
            else:
                repeat = False
        rolls += roll
    print(rolls)


if __name__ == '__main__':
    main()
