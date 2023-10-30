def main():
    a = 8
    b = 2
    a = stancode(a / 4, (a + b) / a)
    if a == 2:
        print("Answer3: " + str(int(a + b)))
    print("Answer4: " + str(int(a - b)))


def stancode(b, a):
    temp = b
    print("Answer1: " + str(b))
    b = stanCode(a,b)
    a = stanCode(b,temp)
    print("Answer2: " + str(a))
    return a % 3


def stanCode(a, b):
    ans = a
    for i in range(3):
        ans *= b
    return ans


if __name__ == '__main__':
    main()
