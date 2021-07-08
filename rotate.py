import PIL.Image as pilimg
import numpy as np
import math

from exception import ImageShapeError
from utils import save

def rotate(origin, point, angle):
    """rotate point by angle
    
    Args:
        origin(list): center point(x,y)
        point(list): point to rotate(x,y)
        aangle(float): angle to rotate 
        
    Returns:
        (float, float): transformed x, y point
    """
    angle = math.radians(angle)
    origin_x, origin_y = origin
    point_x, point_y = point
    
    term_x = point_x - origin_x
    term_y = point_y - origin_y
    
    res_x = origin_x + math.cos(angle) * term_x - math.sin(angle) * term_y
    res_y = origin_y + math.sin(angle) * term_x + math.cos(angle) * term_y
    
    return (res_x, res_y)

def rotate_image(image, angle):
    """rotate image by angle
    
    Args:
        image(list): image before conversion
        angle(float): angle to rotate
        
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
        raise ImageShapeError

    res_image = [[[0] * c for _ in range(w)] for _ in range(h)]
    
    origin_y = h // 2
    origin_x = w // 2
    
    for i in range(c):
        for j in range(h):
            for k in range(w):
                new_w, new_h = rotate([origin_x,origin_y], [k,j], angle)
                
                if new_w < 0 or new_w > w-1 or new_h < 0 or new_h > h-1:
                    continue
                
                new_w_ceil = math.ceil(new_w)
                new_w_floor = math.floor(new_w)
                new_h_ceil = math.ceil(new_h)
                new_h_floor = math.floor(new_h)
                
                term_w = new_w - new_w_floor
                term_h = new_h - new_h_floor
                
                pixel1 = image[new_h_floor][new_w_floor][i]
                pixel2 = image[new_h_floor][new_w_ceil][i]
                pixel3 = image[new_h_ceil][new_w_floor][i]
                pixel4 = image[new_h_ceil][new_w_ceil][i]
                
                res_image[j][k][i] = \
                    (pixel1 * (1- term_h) * (1- term_w)) + \
                    (pixel2 * (1 - term_h) * (term_w)) + \
                    (pixel3 * (term_h) * (1- term_w)) + \
                    (pixel4 * (term_h) * (term_w))
                
    return res_image


if __name__ == "__main__":
    image = pilimg.open("./example.jpg")
    pix = np.array(image)
    image = list(pix)
    rotate_image = rotate_image(image, 50.5)
    save("rotated.jpg",rotate_image)