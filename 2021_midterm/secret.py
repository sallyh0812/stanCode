def secret(s):
    ans = 0
    temp = "0"
    for ch in s:
        if ch.isdigit():
            temp += ch
        else:
            ans += int(temp)
            temp = "0"
    ans += int(temp)
    return ans


def main():
    a = secret('s11tan22Code')
    b = secret('1234a210')
    print(a)
    print(b)


if __name__ == '__main__':
    main()
