"""
File:prime_checker.py
——————————————————————————————————
This program reads a file, parking.txt, and calculates the number of vehicles in the
parking lot. The license plate numbers are as follows:
Cars: 4 digits and 2 letters; Motorcycle: 3 digits and 3 letters; Unknown: 4 digits and
3 letters; Taxi(count as cars): with a “*” at the end of license plate numbers
"""
FILENAME = "parking.txt"


def main():
    with open(FILENAME, 'r') as f:
        car = 0
        moto = 0
        unknown = 0
        for line in f:
            if is_car(line):
                car += 1
            elif is_moto(line):
                moto += 1
            else:
                unknown += 1
            # if line[-2] == "*":
            #     car += 1
            # elif len(line) == 8:  # including "\n"
            #     unknown += 1
            # else:
            #     if count_alpha(line) == 2:
            #         car += 1
            #     else:
            #         moto += 1
    print(f"Car: {car}\nMoto: {moto}\nUnknown: {unknown}")


def is_moto(s):
    a = count_digit(s)
    b = count_alpha(s)
    if a == 3 and b == 3:
        return True
    else:
        return False


def is_car(s):
    a = count_digit(s)
    b = count_alpha(s)
    if a == 4 and b == 2:
        return True
    
    # elif s.find("*") != -1:
    elif s[-2] == "*":  # because each line contains "\n" at the end
        return True
    else:
        return False


def count_digit(s):
    num = 0
    for ch in s:
        if ch.isdigit():
            num += 1
    return num


def count_alpha(s):
    alpha = 0
    for ch in s:
        if ch.isalpha():
            alpha += 1
    return alpha


if __name__ == '__main__':
    main()
