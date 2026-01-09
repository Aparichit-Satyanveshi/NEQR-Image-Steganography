def master_function(color_path,secret_path,shots=1024,show_circuit=True):

    # Loading and display cover image
    img_rgb = load_color_image(color_path)
    img_bin = preprocess_cover_to_8bit(color_path)
    display_cover_image_binary(img_bin)

    # Loading and displaying Original and Decomposed secret image
    img_gray = load_gray_image(secret_path)
    display_secret_before_decomposition(secret_path)
    img_gray_6 = preprocess_grayscale_to_6bit_2d(secret_path,len(img_bin))
    display_secret_after_decomposition(img_gray_6)

    #Loading the values to QC
    qc ,regs = build_qc_full(img_bin,img_gray_6)
    # Displaying

    if show_circuit:
     display_large_circuit(qc, regs,"Whole Q-Circuit")
    qc.barrier()
    
    # Measuring the circuit
    counts = measure_secret_neqr_after(qc,regs,shots=shots)
    print("Counts  Position_bits  Cover_bits Secret_bits  Reconstructed_secret_bits Flags")
    for key,value in counts.items():
          print(f"{value}  {str(key)[:ky+kx]}  {str(key)[ky+kx:24+ky+kx]} {str(key)[24+ky+kx:ky+kx+30]}  {str(key)[ky+kx+30:36+ky+kx]} {str(key)[36+ky+kx:]}")
    # Histogram
    display_the_hist(counts)

    # Reconstruction of secret image
    img_rec = reconstruct_secret_grayscale(counts,
                                           ky=len(regs['y']),kx= len(regs['x']),
                                           Hs=img_gray.shape[0],Ws = img_gray.shape[1],
                                           Hq=img_rgb.shape[0],Wq=img_rgb.shape[1] )
    
    # Displaying and comparing the Original and Reconstruction Image
    metrics = display_and_compare_grayscale(img_gray,img_rec,show_diff=True) 
    print(metrics)



# For master function that has separate embedder and extractor used
def master_function_sep(color_path,secret_path,shots=1024,show_circuit=True):

    # Loading and display cover image
    img_rgb = load_color_image(color_path)
    img_bin = preprocess_cover_to_8bit(color_path)
    display_cover_image_binary(img_bin)

    # Loading and displaying Original and Decomposed secret image
    img_gray = load_gray_image(secret_path)
    display_secret_before_decomposition(secret_path)
    img_gray_6 = preprocess_grayscale_to_6bit_2d(secret_path,len(img_bin))
    display_secret_after_decomposition(img_gray_6)

    #Loading the values to QC
    qc ,regs = build_qc_base(img_bin,img_gray_6)
    # Displaying
    if show_circuit:
     display_large_circuit(qc, regs,"NEQR Q-Circuit")
    qc.barrier()

    qc,regs = embedder(qc,regs)
    if show_circuit:
     display_large_circuit(qc, regs,"Embedded Q-Circuit")
    qc.barrier()

    qc,regs = extractor(qc,regs)
    if show_circuit:
     display_large_circuit(qc, regs,"Extracted Q-Circuit")
    qc.barrier()

    ky=len(regs['y'])
    kx= len(regs['x'])
    # Measuring the circuit
    counts = measure_secret_neqr_after(qc,regs,shots=shots)
    print("Counts  Position_bits  Cover_bits Secret_bits  Reconstructed_secret_bits Flags")
    for key,value in counts.items():
          print(f"{value}  {str(key)[:ky+kx]}  {str(key)[ky+kx:24+ky+kx]} {str(key)[24+ky+kx:ky+kx+30]}  {str(key)[ky+kx+30:36+ky+kx]} {str(key)[36+ky+kx:]}")
    # Histogram
    display_the_hist(counts)

    # Reconstruction of secret image
    img_rec = reconstruct_secret_grayscale(counts,
                                           ky=len(regs['y']),kx= len(regs['x']),
                                           Hs=img_gray.shape[0],Ws = img_gray.shape[1],
                                           Hq=img_rgb.shape[0],Wq=img_rgb.shape[1] )
    
    # Displaying and comparing the Original and Reconstruction Image
    metrics = display_and_compare_grayscale(img_gray,img_rec,show_diff=True) 
    print(metrics)

