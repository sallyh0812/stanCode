"""
File: similarity.py
Name: Sally 111613025
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def accurate_best(long_s, short_s):
    """
    :param long_s: string, original DNA
    :param short_s: string, target DNA
    :return: ans, string, the fragment in long_s where it get the highest accurate score
    """
    max_correct = 0
    best_index = 0
    for i in range(len(long_s) - len(short_s) + 1):  # i: the start index for comparison
        correct = 0  # initialize the accurate score
        
        # count the accurate score for current start index
        for j in range(len(short_s)):
            if long_s[i + j] == short_s[j]:
                correct += 1
        
        # record the highest score and the start index when the highest score happens
        if correct >= max_correct:
            max_correct = correct
            best_index = i
    
    ans = long_s[best_index: best_index + len(short_s)]
    return ans


def main():
    """
    User input DNA and a to-match-sequence, output the fragment in DNA that matches the sequence best
    """
    dna = input("Please give me a DNA sequence to search: ").upper()
    compare = input("What DNA sequence would you like to match? ").upper()
    ans = accurate_best(dna, compare)
    print(f"The best match is {ans}")


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    main()
