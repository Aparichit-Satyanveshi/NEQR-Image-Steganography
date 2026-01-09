# Separate Embedder and Extractors 
def embedder(qc,regs):
    y = regs["y"]
    x = regs["x"]
    cover_q = regs['cover_q']
    secret_q = regs['secret_q']
    si_rec = regs['si_rec']
    flag= regs['flag']
    ky = len(y)
    kx = len(x)
    assert ky== kx
    H =  2**kx

    for y_val in range(H):
        y_bits = format(y_val, f"0{ky}b")
        for x_val in range(H):
            x_bits = format(x_val, f"0{kx}b")

            # activate |y_val, x_val>
            for i, b in enumerate(y_bits):
                if b == "0":
                    qc.x(y[i])
            for i, b in enumerate(x_bits):
                if b == "0":
                    qc.x(x[i])

            controls = list(y) + list(x)
            controlled_full_pixel_gray_embedding(
                qc, controls, cover_q, secret_q, flag
            )
            # uncompute address
            for i, b in enumerate(x_bits):
                if b == "0":
                    qc.x(x[i])
            for i, b in enumerate(y_bits):
                if b == "0":
                    qc.x(y[i])
    
    return qc, {
        "y": y,
        "x": x,
        "cover_q": cover_q,
        "secret_q": secret_q,
        "si_rec": si_rec,
        "flag": flag
    }

def extractor(qc,regs):
    y = regs["y"]
    x = regs["x"]
    cover_q = regs['cover_q']
    secret_q = regs['secret_q']
    si_rec = regs['si_rec']
    flag= regs['flag']
    ky = len(y)
    kx = len(x)
    assert ky== kx
    H =  2**kx

    for y_val in range(H):
        y_bits = format(y_val, f"0{ky}b")
        for x_val in range(H):
            x_bits = format(x_val, f"0{kx}b")

            # activate |y_val, x_val>
            for i, b in enumerate(y_bits):
                if b == "0":
                    qc.x(y[i])
            for i, b in enumerate(x_bits):
                if b == "0":
                    qc.x(x[i])

            controls = list(y) + list(x)
            controlled_full_pixel_gray_extraction(
                qc, controls, cover_q, si_rec
            )

            # uncompute address
            for i, b in enumerate(x_bits):
                if b == "0":
                    qc.x(x[i])
            for i, b in enumerate(y_bits):
                if b == "0":
                    qc.x(y[i])
    
    return qc, {
        "y": y,
        "x": x,
        "cover_q": cover_q,
        "secret_q": secret_q,
        "si_rec": si_rec,
        "flag": flag
    }
    
