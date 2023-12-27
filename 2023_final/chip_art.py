from simpleimage import SimpleImage


def chip_art(img: SimpleImage) -> SimpleImage:
    n_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            o_p = img.get_pixel(x, y)
            n_p = n_img.get_pixel(img.width - x - 1, img.height - y - 1)
            n_p.red = o_p.red
            n_p.green = o_p.green
            n_p.blue = o_p.blue
    return n_img


def main():
    img = SimpleImage('cat.jpg')
    chip_art(img).show()


if __name__ == '__main__':
    main()
