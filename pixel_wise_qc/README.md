# PIXEL-WISE CIRCUITS
## USAGE OF EACH FILE IS GIVEN BELOW :

### `load_cover_image.py`
Loads and preprocesses the cover image used for embedding.
**Usage:**
* Reads the input cover image from disk
* Converts it to 8bit format
* Prepares pixel data for NEQR-style encoding
**Application:**
Acts as the entry point for cover image data, ensuring that the image is in a consistent and valid format before encoding into quantum or quantum-inspired registers.


### `load_transform_secret_image.py`
Loads and transforms the secret image into a binary representation suitable for embedding.
**Usage:**
* Reads the secret image
* Converts grayscale pixel values into 8-bit binary form
* Flattens the binary data into a stream
* Applies segmentation and padding as required to get 6-bit format
**Application:**
Provides the secret data in a structured binary format that can be embedded reversibly into the cover image representation.

### `neqr_ci_si.py`
Implements NEQR-model of the cover image and secret information.
**Usage:**
* Encodes pixel coordinates into binary registers
* Encodes grayscale intensities using computational basis states
* Establishes the logical NEQR representation used throughout the pipeline
**Application:**
Forms the conceptual core of the project by mapping classical image data into an NEQR-inspired representation compatible with quantum circuits.

### `embedder_circuit.py`
Defines the embedding logic for inserting secret information into the NEQR-encoded cover image.
**Usage:**
* Applies reversible, controlled operations to embed secret bits
* Uses ancilla/control logic to preserve reversibility
* Ensures that embedding does not corrupt unrelated pixel data
**Application:**
Implements the steganographic step of the pipeline while respecting quantum reversibility constraints.

### `extractor_circuit.py`
Defines the extraction logic to recover embedded secret information.
**Usage:**
* Applies inverse operations corresponding to the embedding process
* Retrieves secret bits from the encoded representation
* Maintains ancilla cleanup and logical reversibility
**Application:**
Ensures that embedded information can be reliably and losslessly extracted.


### `separate_circuits.py`
Manages the decomposition of the overall process into smaller, modular circuits.
**Usage:**
* Separates encoding, embedding, extraction, and cleanup into distinct circuits
* Facilitates debugging and reuse
* Allows selective execution of pipeline components
**Application:**
Improves clarity and maintainability of the quantum circuit design and supports incremental testing.


### `full_process_circuit.py`
Constructs and orchestrates the complete end-to-end circuit.
**Usage:**
* Integrates encoding, embedding, extraction, and cleanup stages
* Executes the full NEQR-inspired steganography pipeline
* Acts as the main driver for circuit-based execution
**Application:**
Represents the complete workflow, suitable for simulation or future execution on quantum hardware.


### `reconstruct_from_counts.py`
Reconstructs the secret image from measurement results or simulated counts.
**Usage:**
* Interprets measurement outcomes
* Reassembles binary streams into 8-bit grayscale pixel values
* Handles padding removal and image reshaping
**Application:**
Bridges the gap between circuit execution results and classical image reconstruction.

### `measure_display.py`
Handles measurement execution and visualization of results.
**Usage:**
* Executes measurements on quantum or simulated circuits
* Collects and formats measurement counts
* Displays reconstructed images or intermediate outputs
**Application:**
Provides interpretability and validation of circuit outputs.


### `display_functions.py`
Contains utility functions for visualization and debugging.
**Usage:**
* Displays images at various pipeline stages
* Visualizes differences between original and reconstructed images
* Supports result interpretation
**Application:**
Aids in qualitative validation and debugging.


### `master_functions.py`
Provides high-level orchestration utilities that coordinate multiple modules.
**Usage:**
* Calls image loading, encoding, embedding, extraction, and reconstruction functions
* Manages parameter passing and execution order
* Serves as a unified control interface
**Application:**
Simplifies usage by encapsulating the full pipeline into callable workflows.


## Summary
Each file is designed to perform a **single, well-defined role**, enabling:
* Clear separation of concerns
* Reversible and quantum-compatible logic
* Easy debugging and future extension to real quantum backends
Together, these modules implement a complete NEQR-inspired image steganography system from image loading to reconstruction.

