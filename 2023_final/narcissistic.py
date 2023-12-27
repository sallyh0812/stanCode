def narcissistic_checker(number: int) -> bool:
    power = 0
    while number // 10 ** power != 0:
        power += 1
    checker = 0
    for i in range(power):
        checker += (number // (10 ** i) % 10) ** power
    if checker == number:
        return True
    return False


def main():
    print(narcissistic_checker(153))
    print(narcissistic_checker(11))


if __name__ == "__main__":
    main()
