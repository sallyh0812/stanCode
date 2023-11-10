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
    :param filepath: str, the filepath of the img processed
    :return img: SimpleImage, fire highlighted, others parts grayed
    """
    img = SimpleImage(filepath)
    for pixel in img:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red > avg * HURDLE_FACTOR:  # if it's fire part
            pixel.red = 255
            pixel.blue = 0
            pixel.green = 0
        else:
            # gray other parts
            pixel.red = avg
            pixel.blue = avg
            pixel.green = avg
    return img


def main():
    """
    Show the original picture and the processed picture with fire highlighted, others parts grayed
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


#  DO NOT EDIT THE CODE BELOW THIS LINE  #
if __name__ == '__main__':
    main()
