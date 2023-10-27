"""
File: hailstone.py
Name: Sally 111613025
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    n is odd -> n=3*n+1
    n is even -> n=n//2
    until n==1
    """
    print("This program computes Hailstone sequences.\n")
    n = int(input("Enter a number: "))
    step = 0
    while n != 1:
        if n % 2 == 1:
            print(f"{n} is odd, so I make 3n+1: {n * 3 + 1}")
            n = n * 3 + 1
            step += 1  # count the step
        else:
            print(f"{n} is even, so I take half: {n // 2}")
            n = n // 2
            step += 1
    print(f"It took {step} steps to reach 1.")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
