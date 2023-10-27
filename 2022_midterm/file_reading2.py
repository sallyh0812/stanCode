"""
File: file_reading2.py
——————————————————————————————————
This program reads a file, parking.txt, and prints the alphabets that are unused. If
the license plate numbers in the parking lot include all the alphabets, you should
print “All alphabets are used”.
"""
FILENAME = "parking.txt"
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    with open(FILENAME, 'r') as f:
        unused = ALPHA
        for line in f:
            unused = check_use(line, unused)
        for i in range(len(unused)):
            if i == len(unused) - 1:
                print(unused[i], end="")
            else:
                print(unused[i], end=", ")


def check_use(s, now_unused):
    ans = ""
    for ch in now_unused:
        if s.find(ch) == -1:
            ans += ch
    return ans


if __name__ == '__main__':
    main()
