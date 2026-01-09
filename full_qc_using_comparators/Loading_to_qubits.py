from qiskit import QuantumCircuit, QuantumRegister
import numpy as np

def build_base_qc_CI_SI(img_bin, img_gray_6):
    # FORMAT ->
    # img_bin  : list[list[list[str]]]  (H,H,3) each str is 8-bit
    # img_gray : list[list[list[int]]]  (H,H,6)
    # OUTPUT FORMAT : |y_c|x_c|cover_q|y_s|x_s|secret_q|si_rec|flag&anc>
    # Dimension verification
    H = len(img_bin)
    assert all(len(row) == H for row in img_bin)
    ky = kx = int(np.log2(H))
    assert 2**kx == H, "H must be power of 2"

    y_c = QuantumRegister(ky, "y_c")
    x_c = QuantumRegister(kx, "x_c")
    cover_q = QuantumRegister(24, "CI")

    y_s = QuantumRegister(ky, "y_s")
    x_s = QuantumRegister(kx, "x_s")
    secret_q = QuantumRegister(6, "SI")
    si_rec = QuantumRegister(6, "si_rec")
    flag     = QuantumRegister(1, "flag")
    anc_x    = QuantumRegister(kx, "anc_x")
    anc_y    = QuantumRegister(ky, "anc_y")
    flag_x   = QuantumRegister(1, "fx")
    flag_y   = QuantumRegister(1, "fy")
    anc_gray = QuantumRegister(1, "ag")

    qc = QuantumCircuit(
        y_c, x_c, cover_q,
        y_s, x_s, secret_q,
        si_rec,flag, 
        anc_x, anc_y, flag_x, flag_y, anc_gray
    )

    # Load |CI⟩ into qc from given format cover image
    qc.h(y_c)
    qc.h(x_c)

    for y in range(H):
        y_bits = format(y, f"0{ky}b")
        for x in range(H):
            x_bits = format(x, f"0{kx}b")

            for i, b in enumerate(y_bits):
                if b == "0":
                    qc.x(y_c[i])
            for i, b in enumerate(x_bits):
                if b == "0":
                    qc.x(x_c[i])

            controls = list(y_c) + list(x_c)

            for c in range(3):
                bits = img_bin[y][x][c]
                for b, bit in enumerate(bits):
                    if bit == "1":
                        qc.mcx(controls, cover_q[c*8 + b])

            for i, b in enumerate(x_bits):
                if b == "0":
                    qc.x(x_c[i])
            for i, b in enumerate(y_bits):
                if b == "0":
                    qc.x(y_c[i])

    # Load |SI⟩ into qc from given format decomposed secret image
    qc.h(y_s)
    qc.h(x_s)

    for y in range(H):
        y_bits = format(y, f"0{ky}b")
        for x in range(H):
            x_bits = format(x, f"0{kx}b")

            for i, b in enumerate(y_bits):
                if b == "0":
                    qc.x(y_s[i])
            for i, b in enumerate(x_bits):
                if b == "0":
                    qc.x(x_s[i])

            controls = list(y_s) + list(x_s)

            for i, bit in enumerate(img_gray_6[y][x]):
                if bit == 1:
                    qc.mcx(controls, secret_q[i])

            for i, b in enumerate(x_bits):
                if b == "0":
                    qc.x(x_s[i])
            for i, b in enumerate(y_bits):
                if b == "0":
                    qc.x(y_s[i])

    return qc, {
        "y_c": y_c, "x_c": x_c, "cover_q": cover_q,
        "y_s": y_s, "x_s": x_s, "secret_q": secret_q,
        "si_rec":si_rec,"flag": flag,
        "anc_x": anc_x, "anc_y": anc_y,
        "flag_x": flag_x, "flag_y": flag_y,
        "anc_gray": anc_gray
    }
