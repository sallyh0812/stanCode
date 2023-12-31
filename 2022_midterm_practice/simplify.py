"""
File: simplify.py
———————————————————————————————
This program asks the user for inputs and removes consecutive occurrences.
We prompt "Please enter a string: " and wait for the user’s string input.
If the user entered "Aaarroonn", "Cleaned: Aaron" will be printed on screen.
If "quit" is entered, "Have a good one!" will be printed and terminate the program.
"""


def main():
    print("Welcome to stanCode String Cleaning Program!")
    while True:
        s = input("Please enter a string: ")
        if s == "quit":
            break
        ans = remove_duplicates(s)
        print("Cleaned: " + ans)
    print("Have a good one!")


def remove_duplicates(s):
    # avoid len = 0
    if len(s) < 2:
        return s
    cleaned = s[0]
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            cleaned += s[i]
    return cleaned


if __name__ == '__main__':
    main()
