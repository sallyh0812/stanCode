def main():
    num1 = 4
    num2 = 3 + 2 * num1
    num3 = pumpkin(num2, num2, num1)
    print('First result: ' + str(num3))
    num1 = costume(num2, num3)
    print("Second result: " + str(num1))


def costume(mask, cape):
    a = mask + 9 / cape + 1
    mask = a * 2 / 4
    cape = (mask - 3) / 2
    return pumpkin(a, mask, cape)


def pumpkin(x, y, z):
    z += 3
    y = y + x - 9
    return y - z


if __name__ == '__main__':
    main()
