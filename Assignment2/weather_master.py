"""
File: weather_master.py
Name: Sally 111613025
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
QUIT = -1


def main():
	"""
	Read the user input until the input==QUIT
	Record the max and min input (if new > max then have max = new, if new < min then have min = new)
	Calculate the average of all the input (sum of input/the amount of input)
	"""
	print("stanCode \"Weather Master 4.0\"!")
	temp = int(input(f"Next Temperature: (or {QUIT} to quit)? "))

	if temp == QUIT:
		print("No temperatures were entered.")

	else:  # valid input
		# set initial value for variables
		coldDay = 0  # the amount of input less then 16
		sumTemp = 0  # sum of input
		count = 0  # the amount of input
		maxTemp = temp
		minTemp = temp

		while temp != QUIT:
			if temp < 16:
				coldDay += 1
			if temp > maxTemp:
				maxTemp = temp
			elif temp < minTemp:
				minTemp = temp
			sumTemp += temp
			count += 1
			temp = int(input(f"Next Temperature: (or {QUIT} to quit)? "))

		avgTemp = sumTemp / count
		print(f"Highest temperature = {maxTemp}")
		print(f"Lowest temperature = {minTemp}")
		print(f"Average = {avgTemp}")
		print(f"{coldDay} cold day(s)")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
