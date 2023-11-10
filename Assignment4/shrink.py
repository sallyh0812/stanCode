"""
File: shrink.py
Name: Sally 111613025
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filepath):
    """
    :param filepath: str,
    :return img: SimpleImage,
    """
    o_img = SimpleImage(filepath)
    n_img = SimpleImage.blank(o_img.width // 2, o_img.height // 2)
    for x in range(n_img.width):
        for y in range(n_img.height):
            n_pixel = n_img.get_pixel(x, y)
            r_sum = 0
            g_sum = 0
            b_sum = 0
            for i in range(x * 2, x * 2 + 2):
                for j in range(y * 2, y * 2 + 2):
                    o_pixel = o_img.get_pixel(i, j)
                    r_sum += o_pixel.red
                    g_sum += o_pixel.green
                    b_sum += o_pixel.blue
            n_pixel.red = r_sum // 4
            n_pixel.green = g_sum // 4
            n_pixel.blue = b_sum // 4
    return n_img


def main():
    """
    TODO:
    """
    original = SimpleImage("images/poppy.png")
    original.show
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


#  DO NOT EDIT THE CODE BELOW THIS LINE  #
if __name__ == '__main__':
    main()
