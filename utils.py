import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt 

def save(file_name,image):
    """save image
    
    Args:
        file_name(str): save image file name
        image(list): list of images to be saved
    """
    image = np.array(image).astype(np.uint8)
    plt.imsave(file_name, image)
    