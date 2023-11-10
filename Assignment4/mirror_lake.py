"""
File: mirror_lake.py
Name: Sally 111613025
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filepath):
    """
    :param filepath:
    :return:
    """
    img = SimpleImage(filepath)
    reflected = SimpleImage.blank(img.width, img.height * 2)
    for x in range(img.width):
        for y in range(img.height):
            o_pixel = img.get_pixel(x, y)
            r1_pixel = reflected.get_pixel(x, y)
            r2_pixel = reflected.get_pixel(x, reflected.height - 1 - y)
            
            r1_pixel.red = o_pixel.red
            r1_pixel.green = o_pixel.green
            r1_pixel.blue = o_pixel.blue
            
            r2_pixel.red = o_pixel.red
            r2_pixel.green = o_pixel.green
            r2_pixel.blue = o_pixel.blue
            
    return reflected


def main():
    """
    TODO:
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


#  DO NOT EDIT THE CODE BELOW THIS LINE  #
if __name__ == '__main__':
    main()
