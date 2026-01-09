from collections import defaultdict
def counts_to_6bit_blocks(counts, ky, kx):
    buckets = defaultdict(lambda: defaultdict(int))

    for bitstring, freq in counts.items():
        bits = bitstring.replace(" ", "")
        y_bits = bits[:ky]                 # y MSB -> LSB
        x_bits = bits[ky:ky + kx]          # x MSB -> LSB
        s_bits = bits[ky+kx+30:ky+kx+36]   # s5 s4 s3 s2 s1 s0

        y = int(y_bits, 2)
        x = int(x_bits, 2)
        s = tuple(int(b) for b in s_bits)

        buckets[(y, x)][s] += freq

    # choose dominant secret per (y,x)
    secret_blocks = {}
    for (y, x), s_dict in buckets.items():
        secret_blocks[(y, x)] = list(max(s_dict.items(), key=lambda kv: kv[1])[0])
    return secret_blocks

def collect_secret_6bit_blocks(secret_blocks,Hq, Wq,Hs, Ws):
    total_secret_bits = 8 * Hs * Ws
    needed_blocks = (total_secret_bits + 5) // 6 

    ordered_blocks = []
    for y in range(Hq):
        for x in range(Wq):
            if (y, x) in secret_blocks:
                ordered_blocks.append(secret_blocks[(y, x)])
            else:
                ordered_blocks.append([0]*6)

            if len(ordered_blocks) == needed_blocks:
                return ordered_blocks

    return ordered_blocks

def blocks_to_bitstream(blocks_6bit):
    bitstream = []
    for blk in blocks_6bit:
        bitstream.extend(blk)
    return bitstream

def bitstream_to_pixels(bitstream, Hs, Ws):
    total_pixels = Hs * Ws
    pixels = []
    bitstream = bitstream[:8*total_pixels]  
    for i in range(0, 8 * total_pixels, 8):
        byte = bitstream[i:i+8]
        value = 0
        for b in byte:
            value = (value << 1) | b
        pixels.append(value)
        # OR use
        # pixels.append(int("".join(map(str, byte)), 2))
    return np.array(pixels, dtype=np.uint8).reshape(Hs, Ws)

def reconstruct_secret_grayscale(counts,ky, kx ,Hq, Wq,Hs,Ws):
    # Making 6bit blocks
    secret_blocks = counts_to_6bit_blocks(counts, ky, kx)
    # collect only required 6-bit blocks
    blocks_6bit = collect_secret_6bit_blocks(secret_blocks, Hq, Wq, Hs, Ws)
    bitstream = blocks_to_bitstream(blocks_6bit)
    # REMOVE PADDED ZEROS 
    total_bits_needed = Hs * Ws * 8
    bitstream = bitstream[:total_bits_needed]
    assert len(bitstream) % 8 == 0
    # Back from bitstream to grayscale image
    img_rec = bitstream_to_pixels(bitstream, Hs, Ws)
    return img_rec





