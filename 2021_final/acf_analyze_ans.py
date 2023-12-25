from simpleimage import SimpleImage


def ratio(filename):
    """
    : param filename: str, the image file name that needs to be analyzed
    : return: float, the ratio of particle pixels to the whole image
    """
    # Your Code Here
    img = SimpleImage(filename)
    total = 0
    particle = 0
    for p in img:
        total += 1
        if p.red or p.green or p.blue:
            particle += 1

    return particle / total


def main():
    print(ratio('acf.jpg'))


if __name__ == '__main__':
    main()
