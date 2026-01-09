from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt

def load_gray_image(image_path):
    img = Image.open(image_path).convert("L")
    img_gray = np.array(img, dtype=np.uint8)
    return img_gray


def grayscale_to_8bit_binary(img_gray):
    H, W = img_gray.shape
    bin_img = [[None for _ in range(W)] for _ in range(H)]

    for i in range(H):
        for j in range(W):
            bin_img[i][j] = format(int(img_gray[i, j]), '08b')
    return bin_img


def flatten_binary_image(bin_img):
    bitstream = []

    for row in bin_img:
        for pixel_bin in row:
            bitstream.extend([int(b) for b in pixel_bin])
    return bitstream



def split_to_6bit_blocks(bitstream):
    padding = (6 - (__builtins__.len(bitstream) % 6)) % 6
    bitstream = bitstream + [0] * padding

    blocks_6bit = []
    for i in range(0, __builtins__.len(bitstream), 6):
        blocks_6bit.append(bitstream[i:i+6])
    return blocks_6bit



def reshape_blocks_to_2d(blocks_6bit, W_cover):
    M = len(blocks_6bit)
    H_needed = math.ceil(M / W_cover)

    padded_blocks = blocks_6bit + [[0]*6] * (H_needed * W_cover - M)

    blocks_2d = []
    for y in range(H_needed):
        row = padded_blocks[y*W_cover : (y+1)*W_cover]
        blocks_2d.append(row)

    return blocks_2d


def pad_2d_to_power_of_two(blocks_2d):
    H = len(blocks_2d)
    W = len(blocks_2d[0])

    H2 = 1 << math.ceil(math.log2(H))
    W2 = 1 << math.ceil(math.log2(W))

    zero_block = [0]*6
    # Pad rows
    for row in blocks_2d:
        row.extend([zero_block] * (W2 - W))
    # Pad columns
    for _ in range(H2 - H):
        blocks_2d.append([zero_block] * W2)
    return blocks_2d

def preprocess_grayscale_to_6bit_2d(image_path,l):
    img_gray = load_gray_image(image_path)
    bin_img = grayscale_to_8bit_binary(img_gray)
    bitstream = flatten_binary_image(bin_img)
    blocks_6bit = split_to_6bit_blocks(bitstream)
    blocks_2d=reshape_blocks_to_2d(blocks_6bit,l)
    img_gray_6= pad_2d_to_power_of_two(blocks_2d)
    return img_gray_6


def display_secret_before_decomposition(secret_path, title="Secret Image (Original)", save_path=None):
    
    img_gray = load_gray_image(secret_path)
    plt.figure(figsize=(4, 4))
    plt.imshow(img_gray, cmap="gray", vmin=0, vmax=255)
    plt.axis("off")
    plt.title(title)

    if save_path is not None:
        plt.savefig(save_path, bbox_inches="tight", dpi=300)

    plt.show()



def display_secret_after_decomposition(img_gray_6, title="Secret Image After Decomposition", save_path=None):
    # img_gray_6 : (H,W,6)
    # Each 6-bit block is bit of binary value b/w 0 to 63

    H = len(img_gray_6)
    W = len(img_gray_6[0])

    img = np.zeros((H, W), dtype=np.uint8)

    for i in range(H):
        for j in range(W):
            bits = img_gray_6[i][j]    
            value = int("".join(map(str, bits)), 2)
            img[i, j] = value               

    plt.figure(figsize=(4, 4))
    plt.imshow(img, cmap="gray", vmin=0, vmax=63)
    plt.axis("off")
    plt.title(title)

    if save_path is not None:
        plt.savefig(save_path, bbox_inches="tight", dpi=300)

    plt.show()

