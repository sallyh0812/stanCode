"""
File: caesar.py
Name: Sally 111613025
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def decipher(code, move):
    """
    :param code: string, ciphered code
    :param move: int, the secret num
    :return: ans, string, deciphered code
    """
    ans = ""
    for ch in code:
        find_alpha = ALPHABET.find(ch)  # find the index for ch in ALPHABET
        if find_alpha != -1:
            # get the alphabet at [move] steps right, %26 to make sure the index is in the range of 0~25
            ans += ALPHABET[(find_alpha + move) % 26]
        else:  # if ch is not an alphabet, keep it
            ans += ch
    return ans


def main():
    """
    User input a secret num and a ciphered code, output the deciphered code
    """
    secret_num = int(input("Secret number: "))
    ciphered = input("What's the ciphered string?").upper()
    deciphered = decipher(ciphered, secret_num)

    print(f"The deciphered string is: {deciphered}")


# DO NOT EDIT THE CODE BELOW THIS LINE  #
if __name__ == '__main__':
    main()
