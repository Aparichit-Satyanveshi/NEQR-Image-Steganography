### Purpose

This directory contains a classical implementation of the paper [Quantum steganography based on reflected gray code for color images](https://journals.sagepub.com/doi/abs/10.3233/IDT-190034) . This includes preprocessing of 8 bit RGB Color images and 8 bit Grayscale Secret images, which is then broken in its 6 bit representation, which is in turn is embedded in the Colored Cover image to form Stegano-image using Paper's Algorithm .Later, this is decoded using the given process and reconstructed as 8 bit Grayscale image and compared with original one, which should give zero  error as we use a deterministic classical algorithm, with zero-noise model. 

The objective is to validate correctness, reversibility, and bit-level consistency before translating the logic to quantum circuits.

### Conceptual Working

1. Grayscale images are represented in binary form following NEQR principles
2. Pixel intensity is encoded using fixed-length binary registers
3. Pixel coordinates are handled explicitly
4. Secret image data is embedded into a cover image in a reversible manner
5. Extraction reconstructs the original secret image without prior knowledge of its dimensions
This implementation **does not rely on quantum hardware or simulators** ,
but all operations are constrained so that they can be mapped to quantum logic.

### Scope

- Encoding and decoding of grayscale images
- Bit-level embedding and extraction
- Reconstruction with zero information loss
- Metric-based validation (MSE, MAE, PSNR)





