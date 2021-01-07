import numpy as np

def IDCT(img, block_coef, mask):
    new_image = np.zeros_like(img).astype(np.float32)

    # Left->Right & Top->Bottom order
    for i in range(0, img.shape[0], 8):
        for j in range(0, img.shape[1], 8):
            new_image[i:i+8, j:j+8] = img[i:i+8, j:j+8] * mask
            new_image[i:i+8, j:j+8] = np.dot(np.dot(block_coef.transpose(), new_image[i:i+8, j:j+8]), block_coef)

    return new_image