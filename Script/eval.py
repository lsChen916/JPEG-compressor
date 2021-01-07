import cv2
import config
import numpy as np
from math import sqrt

def SNR():
    img = cv2.imread(config.image, 0).astype(np.float32)
    recon = cv2.imread(config.recon, 0).astype(np.float32)

    try:
        img.shape == recon.shape
    except Exception as e:
        print("The size of two images must be equal!")
    
    recon_sum_of_square = np.sum(np.power(recon.flatten(), 2))
    diff_sum_of_square = np.sum(np.power(img.flatten()-recon.flatten(), 2))
    print("SNR:  ", recon_sum_of_square / diff_sum_of_square)

def RMSE():
    img = cv2.imread(config.image, 0).astype(np.float32)
    recon = cv2.imread(config.recon, 0).astype(np.float32)

    try:
        img.shape == recon.shape
    except Exception as e:
        print("The size of two images must be equal!")
    
    diff_sum_of_square = np.sum(np.power(img.flatten()-recon.flatten(), 2))
    print("RMSE: ", sqrt(diff_sum_of_square / (config.height * config.width)))

SNR()
RMSE()