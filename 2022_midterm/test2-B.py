def main():
    a = 1
    b = 1.0
    c = stancode(a + int(1.666), b)
    print('Answer1:' + str(a + 1))
    if c:
        print('Answer3:' + str(a))
    else:
        print('Answer4:' + str(b))


def stancode(a, b):
    a = b
    b = a
    c = stanCode(b)
    print('Answer5:' + str(c))
    return a == b


def stanCode(b):
    b += 1
    return b


if __name__ == '__main__':
    main()
