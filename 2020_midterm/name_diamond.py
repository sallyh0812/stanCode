def name_diamond(name):
    """
    : param name: str, a string that will be printed in a “diamond” format.
    ——————————————————————————————————
    This function accepts a string as a parameter and prints it in a "diamond"
    format.
    """
    for i in range(len(name)):
        print(name[:i + 1])
    for i in range(1, len(name)):
        for j in range(i):
            print(" ", end="")
        print(name[i:])


def main():
    name = input("name: ")
    name_diamond(name)


if __name__ == '__main__':
    main()
