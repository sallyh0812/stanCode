def code_tracing():
    sc = [1, 2, 3]
    if sc.pop() is 3.0:
        print('Answer1:', sc)
    else:
        print('Answer2:', sc)
    
    cs = ['hi']
    mystery(sc, cs)
    print('Answer3:', sc, cs)


def mystery(sc, cs):
    if len(cs):
        print('Answer5:', sc)
    else:
        print('Answer6:', sc)
    cs = sc


if __name__ == '__main__':
    code_tracing()
