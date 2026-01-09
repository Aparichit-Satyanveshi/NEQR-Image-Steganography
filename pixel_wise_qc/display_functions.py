from qiskit import QuantumCircuit, QuantumRegister
from qiskit.visualization import circuit_drawer
from IPython.display import display

def display_large_circuit(qc, regs, name,fold=250):
    print(f"Below is given the {name}")
    shadow_regs = {}
    for name, reg in regs.items():
        shadow_regs[name] = QuantumRegister(len(reg), name)

    qc_shadow = QuantumCircuit(*shadow_regs.values())

    for inst, qargs, cargs in qc.data:
        new_qargs = []
        for q in qargs:
            idx = qc.qubits.index(q)
            new_qargs.append(qc_shadow.qubits[idx])
        qc_shadow.append(inst, new_qargs, cargs)


    fig = circuit_drawer(qc_shadow,output="mpl",fold=fold)
    width = max(30, len(qc_shadow.qubits) *1)
    height = max(10, qc_shadow.depth() * 1)
    fig.set_size_inches(width, height)
    display(fig)

  def display_and_compare_grayscale(original_img,reconstructed_img,show_diff=True):
    assert original_img.shape == reconstructed_img.shape
    orig = original_img.astype(int)
    recon = reconstructed_img.astype(int)
    diff = np.abs(orig - recon)
    # Metrics
    mae = np.mean(diff)
    mse = np.mean((orig - recon) ** 2)
    max_err = np.max(diff)

    if mse == 0:
        psnr = float("inf")
    else:
        psnr = 20 * math.log10(255.0 / math.sqrt(mse))

    print("Reconstruction Error Metrics are as follows :")
    print(f"Mean Absolute Error (MAE): {mae:.4f}")
    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"Max Pixel Error : {max_err}")
    print(f"PSNR (dB) : {psnr:.2f}")

    if show_diff:
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    else:
        fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].imshow(original_img, cmap="gray", vmin=0, vmax=255)
    axes[0].set_title("Original Grayscale Image")
    axes[0].axis("off")

    axes[1].imshow(reconstructed_img, cmap="gray", vmin=0, vmax=255)
    axes[1].set_title("Reconstructed Grayscale Image")
    axes[1].axis("off")

    if show_diff:
        axes[2].imshow(diff, cmap="hot")
        axes[2].set_title("Absolute Difference Image")
        axes[2].axis("off")

    plt.tight_layout()
    plt.show()

    return {"MAE": mae,"MSE": mse,"MAX_ERROR": max_err,"PSNR": psnr}
