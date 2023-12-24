def reference_mystery():
    a = [10, 20]
    b = 3
    c = 5
    mystery(a, b, c)
    print(str(a), b, c)
    a[1] += 1
    mystery(a, a[0], b)
    print(str(a), b, c)


def mystery(a, b, c):
    b = b + c
    for i in range(len(a)):
        a[i] += 1
    c = c + a[0]
    print(str(a), b, c)


if __name__ == '__main__':
    reference_mystery()
