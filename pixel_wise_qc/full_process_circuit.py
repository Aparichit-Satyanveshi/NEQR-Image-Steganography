from qiskit import QuantumCircuit, QuantumRegister
import numpy as np

def build_qc_full(img_bin, img_gray_6):

    H = len(img_bin)
    ky = kx = int(np.log2(H))
    assert 2**kx == H
  
    y = QuantumRegister(ky, "y")
    x = QuantumRegister(kx, "x")
    cover_q  = QuantumRegister(24, "CI")
    secret_q = QuantumRegister(6,  "SI")
    si_rec   = QuantumRegister(6,  "si_rec")
    flag= QuantumRegister(6,"flag")
    qc = QuantumCircuit(y, x, cover_q, secret_q, si_rec,flag)

    #superposition
    qc.h(y)
    qc.h(x)

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

            #Load CI
            for c in range(3):
                for b, bit in enumerate(img_bin[y_val][x_val][c]):
                    if bit == "1":
                        qc.mcx(controls, cover_q[c*8 + b])

            #Load SI
            for i, bit in enumerate(img_gray_6[y_val][x_val]):
                if bit == 1:
                    qc.mcx(controls, secret_q[i])

            #Embed
            controlled_full_pixel_gray_embedding(
                qc, controls, cover_q, secret_q, flag
            )
            # UNLoad SI (if needed)
            # for i, bit in enumerate(img_gray_6[y_val][x_val]):
            #     if bit == 1:
            #         qc.mcx(controls, secret_q[i])

            # Extract
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
