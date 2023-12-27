def narcissistic_checker(number: int) -> bool:
    sum = 0
    ans = number
    n = []
    while number:
        n.append(number % 10)
        number = number // 10
    # print(n)
    for i in range(len(n)):
        sum += n[i] ** len(n)
    if sum == ans:
        return True
    else:
        return False


def main():
    print(narcissistic_checker(153))
    print(narcissistic_checker(11))


if __name__ == "__main__":
    main()
