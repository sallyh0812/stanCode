"""
File: blur.py
Name: Sally 111613025
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return:
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            new_pixel = new_img.get_pixel(x, y)
            count = 0
            r_sum = 0
            b_sum = 0
            g_sum = 0
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < img.width and 0 <= j < img.height:
                        tmp_pixel = img.get_pixel(i, j)
                        count += 1
                        r_sum += tmp_pixel.red
                        b_sum += tmp_pixel.blue
                        g_sum += tmp_pixel.green
            
            new_pixel.red = r_sum // count
            new_pixel.blue = b_sum // count
            new_pixel.green = g_sum // count
    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    
    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


#  DO NOT EDIT THE CODE BELOW THIS LINE  #
if __name__ == '__main__':
    main()
