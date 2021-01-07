import cv2
import config
import numpy as np
from encoder import encode
from decoder import decode
np.set_printoptions(threshold=np.inf)

def main():
    img = cv2.imread(config.image, 0).astype(np.float32)

    block_coef, compressed_code = encode(img - 128)
    recon = decode(block_coef, compressed_code)
    recon += 128.0

    cv2.imshow("Img", recon)
    cv2.waitKey(0)
    cv2.imwrite("../Result/recon_1.jpg", recon)

if __name__ ==  '__main__':
    main()