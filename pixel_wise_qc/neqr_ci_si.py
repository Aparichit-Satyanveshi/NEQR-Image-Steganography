def build_base_ci_si(img_bin,img_gray_6):
    # Creates output of form : |y|x>|CI>|SI>|anc>
    # Dimension Checking
    H = len(img_bin)
    assert all(len(row) == H for row in img_bin)
    ky = kx = int(np.log2(H))
    assert 2**kx == H, "H must be power of 2"

    y = QuantumRegister(ky, "y")
    x = QuantumRegister(kx, "x")
    cover_q = QuantumRegister(24, "CI")
    secret_q = QuantumRegister(6,"SI")
    anc    = QuantumRegister(ky+kx-2, "anc")

    qc = QuantumCircuit(
        y, x, cover_q,secret_q, anc
    )

    # Superposition making
    qc.h(y)
    qc.h(x)

    for y_val in range(H):
        y_bits = format(y_val, f"0{ky}b")
        for x_val in range(H):
            x_bits = format(x_val, f"0{kx}b")
            # Activation of Position |yx>
            for i, b in enumerate(y_bits):
                if b == "0":
                    qc.x(y[i])
            for i, b in enumerate(x_bits):
                if b == "0":
                    qc.x(x[i])

            controls = list(y) + list(x)
            # Loading color image
            for c in range(3):
                bits = img_bin[y_val][x_val][c]
                for b, bit in enumerate(bits):
                    if bit == "1":
                        qc.mcx(controls, cover_q[c*8 + b],anc)
           # Loading Grayscale values
            for i, bit in enumerate(img_gray_6[y_val][x_val]):
                if bit == 1:
                    qc.mcx(controls, secret_q[i],anc)
                  
            # Uncomputation 
            for i, b in enumerate(x_bits):
                if b == "0":
                    qc.x(x[i])
            for i, b in enumerate(y_bits):
                if b == "0":
                    qc.x(y[i])

    return qc, {
        "y": y, "x": x, "cover_q": cover_q,
        'secret_q':secret_q,anc : "anc"
    }
