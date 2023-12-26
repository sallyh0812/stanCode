from simpleimage import SimpleImage


def kaleidoscope(filepath):
    img = SimpleImage(filepath)
    k_img = SimpleImage.blank(img.width * 2, img.height * 2)
    for x in range(img.width):
        for y in range(img.height):
            o_p = img.get_pixel(x, y)
            for i in [x, img.width*2 - x-1]:
                for j in [y, img.height*2 - y-1]:
                    n_p = k_img.get_pixel(i, j)
                    n_p.red = o_p.red
                    n_p.green = o_p.green
                    n_p.blue = o_p.blue
    return  k_img


def main():
    kaleidoscope('cat.jpg').show()


if __name__ == '__main__':
    main()
