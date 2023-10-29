# The constant holds the filepath of the file to be processed
FILEPATH = 'romeojuliet.txt'


def get_num_tokens():
    """
    : return num_tokens: int, the total number of tokens in FILEPATH
    """
    num_token = 0
    with open(FILEPATH, 'r') as f:
        for line in f:
            token_line = 0
            word = False
            for ch in line:
                if ch == " " or ch == "\n":
                    if word:
                        token_line += 1
                        word = False
                else:
                    word = True
            num_token += token_line
    return num_token


def main():
    print(get_num_tokens())


if __name__ == "__main__":
    main()
