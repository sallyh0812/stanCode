"""
File: green_screen.py
Name: Sally 111613025
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, img that is to replace the green screen
    :param figure_img: SimpleImage, a picture with green screen to be removed
    :return figure_img: SimpleImage, after replacing green pixels with background_img
    """
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            f_pixel = figure_img.get_pixel(x, y)
            bigger = max(f_pixel.red, f_pixel.blue)
            if f_pixel.green > bigger * 2:
                b_pixel = background_img.get_pixel(x, y)
                f_pixel.red = b_pixel.red
                f_pixel.green = b_pixel.green
                f_pixel.blue = b_pixel.blue
    return figure_img


def main():
    """
    Read background img and figure img(with green screen),
    then show the figure img after processing green screen
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


#  DO NOT EDIT THE CODE BELOW THIS LINE  #
if __name__ == '__main__':
    main()
