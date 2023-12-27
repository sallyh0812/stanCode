def code_tracing():
    a = "Let's Go Party"
    a = a.split()
    b = [10, 30, (30, 20), 'NYCU', 5.0]
    c = 25
    if b.pop(0) is 10.0:
        print('Answer1:', c + b.pop())
    else:
        print('Answer2:', c + b.pop())
    b.append('MSE')
    secret = mystery(a, b, c)
    if not secret:
        print('Answer5:', a[1:], c)
    else:
        print('Answer6:', a[1:], c)


def mystery(a: list, b: list, c: int) -> bool:
    if len(b) > 4:
        print('Answer3:', str(b.pop()) + 'Winter vacation is coming')
    else:
        print('Answer4:', str(b.pop()) + ' is the best')
    c = b.pop(0)
    a = b
    return 30 in a


if __name__ == '__main__':
    code_tracing()
