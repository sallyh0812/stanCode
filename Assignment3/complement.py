"""
File: complement.py
Name: Sally 111613025
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks users for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def build_complement(dna):
    """
    :param dna: string, the original dna
    :return: trans, string, the complemented dna
    complement using the rule below
    original -> trans
    A -> T
    T -> A
    C -> G
    G -> C
    """
    trans = ""
    for ch in dna.upper():
        if ch == 'A':
            trans += 'T'
        elif ch == 'T':
            trans += 'A'
        elif ch == 'C':
            trans += 'G'
        elif ch == 'G':
            trans += 'C'
    return trans


def main():
    """
    User input original DNA, output the complement of the original DNA
    """
    n = input("Please give me a DNA strand and I'll find the complement: ")
    ans = build_complement(n)
    print(f"The complement of {n} is {ans}")


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    main()
