def controlled_embed_gray_lsb(qc, flag, b_hi, b_lo, secret, target, anc):
    # target ^= flag · (secret ⊕ (b_hi ⊕ b_lo)) = ((flag & secret)^(flag & anc)) 

    # anc = b_hi ⊕ b_lo = parity of Gray code (originally anc =|0>)
    qc.cx(b_hi, anc)
    qc.cx(b_lo, anc)

    # target ^= ((flag & secret)^(flag & anc)) is as follows :

    #1 target ^= (flag & secret)
    qc.mcx([flag, secret], target)
    #2 target ^= (flag & anc)
    qc.mcx([flag, anc], target)

    # uncompute anc
    qc.cx(b_lo, anc)
    qc.cx(b_hi, anc)


def controlled_full_pixel_gray_embedding(qc, cover_q, secret_q, flag, anc):
    # Embeds one secret pixel into one cover pixel iff flag == 1
  
    # for embedding s5,s4,s3 into r1,b1,g1
    controlled_embed_gray_lsb(qc, flag, cover_q[5],  cover_q[6],  secret_q[0], cover_q[6], anc)
    controlled_embed_gray_lsb(qc, flag, cover_q[13], cover_q[14], secret_q[1], cover_q[14], anc)
    controlled_embed_gray_lsb(qc, flag, cover_q[21], cover_q[22], secret_q[2], cover_q[22], anc)
    # for embedding s2,s1,s0 into r0,b0,g0
    controlled_embed_gray_lsb(qc, flag, cover_q[6],  cover_q[7],  secret_q[3], cover_q[7], anc)
    controlled_embed_gray_lsb(qc, flag, cover_q[14], cover_q[15], secret_q[4], cover_q[15], anc)
    controlled_embed_gray_lsb(qc, flag, cover_q[22], cover_q[23], secret_q[5], cover_q[23], anc)

