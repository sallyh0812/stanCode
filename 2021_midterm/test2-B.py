def main():
    a = 6
    b = a / 3
    c = stan(a + b, b)
    if c:
        print("Answer1: " + str(c))
    else:
        print("Answer2: " + str(c))


def stan(p, q):
    p *= p
    q += 5
    q = p // q
    print("Answer3: " + str(q))
    if p - q > q:
        return code(p, q) == 65.0
    else:
        return code(q, p) == 65.0


def code(a, b):
    c = a % b
    print("Answer4 " + str(c))
    return str(c + a)


if __name__ == '__main__':
    main()
