"""
File: prime_checker.py
———————————————————————————————
This program asks our user for input and checks if the input is a
prime number or not. At the beginning, ”Run? ” is printed on Console
and waits the user to enter ’Y’ or ’N’ (”Illegal format.” for anything else)
If the user entered ’Y’, ”n: ” is printed on Console and waits the user to
enter an integer that is greater than 1 and checks if it is a prime number.
If the user entered ’N’, ”Have a good one!” is printed on Console
"""


def main():
    # Your Code Here
    while True:
        run = input("Run? ")
        if run == "N":
            break
        elif run == "Y":
            n = int(input("n: "))
            if is_prime(n):
                print(f"{n} is a prime number.")
            else:
                print(f"{n} is not a prime number.")
        else:
            print("Illegal format.")
    print("Have a good one!")


def is_prime(n):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    
    return prime


if __name__ == '__main__':
    main()
