"""
File: fire.py
Name: Sally 111613025
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filepath):
    """
    :param filepath:
    :return: img, fire highlighted, others parts grayed
    """
    img = SimpleImage(filepath)
    for pixel in img:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red > avg:
            pixel.red = 255
            pixel.blue = 0
            pixel.green = 0
        else:
            pixel.red = avg
            pixel.blue = avg
            pixel.green = avg
    return img


def main():
    """
    TODO:
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


#  DO NOT EDIT THE CODE BELOW THIS LINE  #
if __name__ == '__main__':
    main()
