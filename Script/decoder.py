import config
import numpy as np
from idct import IDCT
from zigzag import inverse_zigzag

def rle_decoder(rle_code):
    irle_code = []
    for code in rle_code:
        tmp = []
        for nz, item in code:
            for _ in range(nz):
                tmp.append(0)
            tmp.append(item)
        if len(tmp) < 64:
            for _ in range(64 - len(tmp)):
                tmp.append(0)
        irle_code.append(np.array(tmp))
    irle_code = np.array(irle_code)

    return irle_code

def decode(block_coef, compressed_code):
    irle_code = rle_decoder(compressed_code)
    recon_dct = np.zeros((config.height, config.width), dtype=np.float32)
    for i in range(0, config.height, 8):
        for j in range(0, config.width, 8):
            index = (i//8)*(config.width//8)+(j//8)
            recon_dct[i:i+8, j:j+8] = inverse_zigzag(irle_code[index], 8, 8)
    recon = IDCT(recon_dct, block_coef, config.mask)

    return recon