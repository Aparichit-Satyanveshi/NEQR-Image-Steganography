def controlled_extract_gray_lsb(
    qc, controls,
    b_hi, b_lo,
    si_rec
):
    qc.mcx(controls + [b_hi],   si_rec)
    qc.mcx(controls + [b_lo],   si_rec)
  
# Extraction of each secret bit in one si_rec bit
def controlled_full_pixel_gray_extraction(
    qc, controls,
    cover_q, si_rec
):
    # s5,s4,s3 <- r1,b1,g1
    controlled_extract_gray_lsb(qc, controls, cover_q[5],  cover_q[6],   si_rec[0])
    controlled_extract_gray_lsb(qc, controls, cover_q[13], cover_q[14],  si_rec[1])
    controlled_extract_gray_lsb(qc, controls, cover_q[21], cover_q[22],  si_rec[2])
    # s2,s1,s0 <- r0,g0,b0
    controlled_extract_gray_lsb(qc, controls, cover_q[6],  cover_q[7],   si_rec[3])
    controlled_extract_gray_lsb(qc, controls, cover_q[14], cover_q[15],  si_rec[4])
    controlled_extract_gray_lsb(qc, controls, cover_q[22], cover_q[23],  si_rec[5])
