def controlled_embed_gray_lsb(
    qc, controls,
    b_hi, b_lo,
    secret, target,
    anc
):

    qc.mcx(controls + [b_hi],   anc)
    qc.mcx(controls + [b_lo],   anc)
    qc.mcx(controls + [secret], anc)

    qc.mcx(controls + [anc], target)

    qc.mcx(controls + [secret], anc)
    qc.mcx(controls + [b_lo],   anc)
    qc.mcx(controls + [b_hi],   anc)

# Embedding using 6 anc-bits each for on secret bit
def controlled_full_pixel_gray_embedding(
    qc, controls,
    cover_q, secret_q,
    anc
):
    # s5,s4,s3 -> r1,b1,g1
    controlled_embed_gray_lsb(qc, controls, cover_q[5],  cover_q[6],  secret_q[0], cover_q[6],  anc[0])
    controlled_embed_gray_lsb(qc, controls, cover_q[13], cover_q[14], secret_q[1], cover_q[14], anc[1])
    controlled_embed_gray_lsb(qc, controls, cover_q[21], cover_q[22], secret_q[2], cover_q[22], anc[2])
    # s2,s1,s0 -> r0,b0,g0
    controlled_embed_gray_lsb(qc, controls, cover_q[6],  cover_q[7],  secret_q[3], cover_q[7],  anc[3])
    controlled_embed_gray_lsb(qc, controls, cover_q[14], cover_q[15], secret_q[4], cover_q[15], anc[4])
    controlled_embed_gray_lsb(qc, controls, cover_q[22], cover_q[23], secret_q[5], cover_q[23], anc[5])
