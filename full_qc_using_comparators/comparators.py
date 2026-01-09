def equality_comparator(qc, reg_a, reg_b, flag, anc):
    # flag = 1 iff reg_a == reg_b
    # All ancilla are returned to |0>

    k = len(reg_a)
    # anc[i] = a[i]^b[i]
    for i in range(k):
        qc.cx(reg_a[i], anc[i])
        qc.cx(reg_b[i], anc[i])

    # flag = XNOR(anc)
    qc.x(anc)
    qc.mcx(list(anc), flag)
    qc.x(anc)

    # uncompute anc
    for i in reversed(range(k)):
        qc.cx(reg_b[i], anc[i])
        qc.cx(reg_a[i], anc[i])


def comparator_2d(
    qc,
    x_c, y_c,
    x_s, y_s,
    flag,
    anc_x, anc_y,
    flag_x, flag_y
):
    # flag = 1 iff (x_c == x_s) AND (y_c == y_s)
    # All ancilla and intermediate flags are uncomputed afterwards

    # x comparison
    equality_comparator(qc, x_c, x_s, flag_x[0], anc_x)

    # y comparison
    equality_comparator(qc, y_c, y_s, flag_y[0], anc_y)

    # AND the results
    qc.ccx(flag_x[0], flag_y[0], flag)

    # uncompute y comparison
    equality_comparator(qc, y_c, y_s, flag_y[0], anc_y)

    # uncompute x comparison
    equality_comparator(qc, x_c, x_s, flag_x[0], anc_x)
