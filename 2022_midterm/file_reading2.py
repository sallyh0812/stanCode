"""
File: file_reading_substr.py
——————————————————————————————————
This program reads a file, parking.txt, and prints the alphabets that are unused. If
the license plate numbers in the parking lot include all the alphabets, you should
print “All alphabets are used”.
"""
FILENAME = "parking.txt"
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    unused = ALPHA
    with open(FILENAME, 'r') as f:
        for line in f:
            unused = check_use(line, unused)
        # All are used
        if len(unused) == 0:
            print("All alphabets are used")
        else:
            for i in range(len(unused) - 1):
                print(unused[i], end=", ")
            print(unused[-1])


def check_use(s, now_unused):
    ans = ""
    for ch in now_unused:
        if s.find(ch) == -1:
            ans += ch
    return ans


if __name__ == '__main__':
    main()
