from simpleimage import SimpleImage


def rotate_right(filename):
    """
    Input:
    filename (str): The image file name that needs to be rotated
    Returns:
    The rotated image of type SimpleImage
    """
    
    img = SimpleImage(filename)
    rotated_img = SimpleImage.blank(img.height, img.width)
    for x in range(img.width):
        for y in range(img.height):
            o_pixel = img.get_pixel(x, y)
            n_pixel = rotated_img.get_pixel(rotated_img.width - y - 1, x)
            n_pixel.red = o_pixel.red
            n_pixel.green = o_pixel.green
            n_pixel.blue = o_pixel.blue
            
    return rotated_img


def main():
    r_img = rotate_right('G0030278-500.jpg')
    r_img.show()


if __name__ == '__main__':
    main()
