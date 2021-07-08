import PIL.Image as pilimg
import numpy as np
import math

from exception import ImageShapeError
from utils import save

def scale_up_image(image, scale_ratio):
    """scale up image by scale_ratio using bilinear interpolate
    
    Args:
        image(list): image before conversion
        scale_ratio(float): ratio to scale (ratio >= 1)
        
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
    
    scaled_h = int((h-1) * scale_ratio)
    scaled_w = int((w-1) * scale_ratio)

    res_image = [[[0] * c for _ in range(scaled_w)] for _ in range(scaled_h)]
    
    for i in range(c):
        for j in range(scaled_h):
            for k in range(scaled_w):
                
                re_h = j / scale_ratio
                re_w = k / scale_ratio
            
                re_w_ceil = math.ceil(re_w)
                re_w_floor = math.floor(re_w)
                re_h_ceil = math.ceil(re_h)
                re_h_floor = math.floor(re_h)
                
                term_w = re_w - re_w_floor
                term_h = re_h - re_h_floor
                
                pixel1 = image[re_h_floor][re_w_floor][i]
                pixel2 = image[re_h_floor][re_w_ceil][i]
                pixel3 = image[re_h_ceil][re_w_floor][i]
                pixel4 = image[re_h_ceil][re_w_ceil][i]
                
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
    scaled_image = scale_up_image(image, 0.7)
    save("scaled.jpg",scaled_image)