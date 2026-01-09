### File Responsibilities

- Image I/O modules:  loading_cover_image.ipynb,loading_secret_image.ipynb
Load, normalize, and validate grayscale images

- Binary conversion utilities : loading_secret_image.ipynb
Convert pixel values to fixed-length binary representations and back

- Embedding logic: Embedding_full.ipynb
Embed secret bitstreams into cover image representations

- Extraction logic : Extracting_full.ipynb
Recover embedded bitstreams from encoded data

- Reconstruction utilities : Reconstruct_secret.ipynb
Reassemble binary streams into valid grayscale images

- Evaluation utilities : Compare_metrics.ipynb
Compute MSE, MAE, and PSNR and visualize results

### Execution Flow

1. Load cover and secret images
2. Convert secret image to binary stream
3. Encode cover image in NEQR-style representation
4. Embed secret data
5. Extract embedded data
6. Reconstruct secret image
7. Display the reconstructed images
8. Evaluate reconstruction quality
