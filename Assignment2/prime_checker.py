"""
File: prime_checker.py
Name: Sally 111613025
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number(-1).
"""
import math
QUIT = -1


def main():
	"""
	If n is divisible by at least one integer from 2 to sqrt(n) -> not prime
	Read the user's input until the user enter -1(the exit code)
	"""
	print("Welcome to the prime checker!")
	n = int(input("n: "))

	while n != -1:
		checkMax = int(math.sqrt(n))
		prime = True  # assume n is prime
		i = 2
		while i <= checkMax:
			if n % i == 0:  # n is divisible by i, which is in the range[2,sqrt(n)]
				prime = False
				break
			i += 1  # check next integer
		if prime:  # prime == True
			print(f"{n} is a prime number.")
		else:  # prime == False
			print(f"{n} is not a prime number.")
		n = int(input("n: "))  # ask for the next n

	print("Have a good one!")  # when n == exit code


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
