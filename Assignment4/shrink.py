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
    :param filepath: str, the img in original size
    :return img: SimpleImage, the img half in size
    ----------------------------------------
    Set the value of 1*1 pixel by the avg of nearby 2*2 pixels
    """
    o_img = SimpleImage(filepath)
    
    # create a blank img with half the height and half the width of the o_img
    n_img = SimpleImage.blank(o_img.width // 2, o_img.height // 2)
    
    for x in range(n_img.width):
        for y in range(n_img.height):
            n_pixel = n_img.get_pixel(x, y)
            
            # initialize the variable for each pixel
            r_sum = 0
            g_sum = 0
            b_sum = 0
            
            # get the avg of 2*2 cube in o_img (2x, 2y), (2x, 2y+1), (2x+1, 2y), (2x+1, 2y+1)
            for i in range(x * 2, x * 2 + 2):
                for j in range(y * 2, y * 2 + 2):
                    o_pixel = o_img.get_pixel(i, j)
                    r_sum += o_pixel.red
                    g_sum += o_pixel.green
                    b_sum += o_pixel.blue
                    
            # set the avg to n_img (x,y)
            n_pixel.red = r_sum // 4
            n_pixel.green = g_sum // 4
            n_pixel.blue = b_sum // 4
            
    return n_img


def main():
    """
    Show the img in original size and the img after shrunk
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


#  DO NOT EDIT THE CODE BELOW THIS LINE  #
if __name__ == '__main__':
    main()
