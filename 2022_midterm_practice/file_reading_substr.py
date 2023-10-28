"""
File: file_reading_substr.py
—————————————————————————————————
This program reads in a file ”substring.txt” and processes each line.
The first digit indicates the first index and the second digit indicates the
second index for the substring.
However, if the index is incorrect, ”Illegal format” will be printed on Console.
"""


def main():
    with open("substring.txt", 'r') as f:
        for line in f:
            print(my_substr(line))


def my_substr(line):
    """
    : param line: str, a line read from the file ”substring.txt”.
    : return ans: str, sub-string of index line[0] to line[1].
     If the index is incorrect, s equals to ”Illegal format”.
    """
    start = int(line[0]) + 2
    end = int(line[1]) + 2
    # There is a "\n" at the end
    if start >= end or end > (len(line) - 1):
        return "Illegal format"
    else:
        return line[start:end]


if __name__ == '__main__':
    main()
