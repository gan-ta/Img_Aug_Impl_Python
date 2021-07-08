import PIL.Image as pilimg
import numpy as np

import exception as ex
import utils as ut
    
def translation_left(image, pixel : int):
    """move the image to the left
    
    Args:
        image(list): image before conversion
        pixel(int): amount to move
        
    Returns:
        list: transformed image list
        
    Raises:
        ImageShapeError: not valid image shape
    """
    try:
        h = len(image)
        w = len(image[0])
        c = len(image[0][0])
    except:
        raise ex.ImageShapeError
    
    res_image = [[[0] * c for _ in range(w)] for _ in range(h)]
    
    for i in range(c):
        for j in range(h):
            for k in range(0, w-pixel):
                res_image[j][k][i] = image[j][k+pixel][i]
                
    return res_image

def translation_right(image,pixel):
    """move the image to the right
    
    Args:
        image(list): image before conversion
        pixel(int): amount to move
        
    Returns:
        list: transformed image list
        
    Raises:
        ImageShapeError: not valid image shape
    """
    try:
        h = len(image)
        w = len(image[0])
        c = len(image[0][0])
    except:
        raise ex.ImageShapeError
    
    res_image = [[[0] * c for _ in range(w)] for _ in range(h)]
    
    for i in range(c):
        for j in range(h):
            for k in range(w-1, pixel-1, -1):
                res_image[j][k][i] = image[j][k-pixel][i]
    
    return res_image

def translation_up(image, pixel):
    """move the image to the upward
    
    Args:
        image(list): image before conversion
        pixel(int): amount to move
        
    Returns:
        list: transformed image list
        
    Raises:
        ImageShapeError: not valid image shape
    """
    try:
        h = len(image)
        w = len(image[0])
        c = len(image[0][0])
    except:
        raise ex.ImageShapeError
    
    res_image = [[[0] * c for _ in range(w)] for _ in range(h)]
    
    for i in range(c):
        for k in range(w):
            for j in range(0, h-pixel):
                res_image[j][k][i] = image[j+pixel][k][i]
    return res_image
 
def translation_down(image, pixel):
    """move the image to the downward
    
    Args:
        image(list): image before conversion
        pixel(int): amount to move
        
    Returns:
        list: transformed image list
        
    Raises:
        ImageShapeError: not valid image shape
    """
    try:
        h = len(image)
        w = len(image[0])
        c = len(image[0][0])
    except:
        raise ex.ImageShapeError
    
    res_image = [[[0] * c for _ in range(w)] for _ in range(h)]
    
    for i in range(c):
        for k in range(w):
            for j in range(h-1, pixel - 1, -1):
                res_image[j][k][i] = image[j-pixel][k][i]
    return res_image

if __name__ == "__main__":
    image = pilimg.open("./example.jpg")
    pix = np.array(image)
    image = list(pix)
    left_translationed = translation_left(image, 100)
    right_translationed = translation_right(image, 100)
    up_translationed = translation_up(image, 100)
    down_translationed = translation_down(image, 100)
    ut.save("left_translationed.jpg", left_translationed)
    ut.save("right_translationed.jpg", right_translationed)
    ut.save("up_translationed.jpg", up_translationed)
    ut.save("down_translationed.jpg", down_translationed)
