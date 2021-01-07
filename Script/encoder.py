import config
import numpy as np
from dct import DCT
from zigzag import zigzag
from math import cos, pi, sqrt

''' Only need to be calculated once during encoding and decoding  ''' 
def cal_block_coef():
    block_coef = np.zeros((8, 8), dtype=np.float32)
    for i in range(8):
        for j in range(8):
            a = sqrt(1.0 / 8.0) if i == 0 else sqrt(2.0 / 8.0)
            block_coef[i][j] = a * cos((j + 0.5) * pi * i / 8.0)

    return block_coef

def run_length_encoding(block_zigzag):
    rle_code = []
    number_of_zeros = 0
    for item in block_zigzag:
        if item == 0.0:
            number_of_zeros += 1
        elif item != 0 and number_of_zeros > 0:
            rle_code.append((number_of_zeros, item))
            number_of_zeros = 0
        else:
            rle_code.append((0, item))
    return rle_code

def encode(img):
    block_coef = cal_block_coef()
    dct_img = DCT(img, block_coef, config.mask)
    zigzag_code = []
    for i in range(0, config.height, 8):
        for j in range(0, config.width, 8):
            zigzag_code.append(zigzag(dct_img[i:i+8, j:j+8]))
    zigzag_code = np.array(zigzag_code, dtype=np.float32)

    rle_code = []
    for block_zigzag in zigzag_code:
        rle_code.append(run_length_encoding(block_zigzag))

    return block_coef, rle_code