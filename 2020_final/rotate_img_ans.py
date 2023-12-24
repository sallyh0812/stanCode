from simpleimage import SimpleImage

def rotate_right(filename):
    """
    Input:
    filename (str): The image file name that needs to be rotated
    Returns:
    The rotated image of type SimpleImage
    """

    img = SimpleImage(filename)
    new_img = SimpleImage.blank(img.height, img.width)
    for y in range(img.height):
        for x in range(img.width):
            old_pixel = img.get_pixel(x, y)
            new_pixel = new_img.get_pixel(img.height - y - 1, x)
            new_pixel.red = old_pixel.red
            new_pixel.green = old_pixel.green
            new_pixel.blue = old_pixel.blue
    return new_img

def main():
    r_img = rotate_right('G0030278-500.jpg')
    r_img.show()
    
if __name__ =='__main__':
    main()