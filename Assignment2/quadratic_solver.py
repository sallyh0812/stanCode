"""
File: quadratic_solver.py
Name: Sally 111613025
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	User inputs a, b, c
	Determine how many roots the equation has by the discriminant
	Calculate the root
	"""
	print("stanCode Quadratic Solver!")
	a = int(input("Enter a: "))
	b = int(input("Enter b: "))
	c = int(input("Enter c: "))
	d = b*b - 4 * a * c  # discriminant

	if d > 0:  # 2 roots
		root1 = (-b + math.sqrt(d)) / (2*a)
		root2 = (-b - math.sqrt(d)) / (2*a)
		print(f"Two roots: {root1}, {root2}")
	elif d == 0:  # 1 root
		root = (-b + math.sqrt(d)) / (2*a)
		print(f"One root: {root}")
	else:  # d<0
		print("No real roots")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
