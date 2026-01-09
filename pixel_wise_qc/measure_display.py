from qiskit import ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile

def measure_secret_neqr_after(qc, regs, shots=1024, method="matrix_product_state"):
    """
    Output format :
    | y_n...y_0| x_n....x_0| c_23 c_22 ..... c_0| s5 s4 s3 s2 s1 s0 | si_rec_5 ......si_rec_0| flags|
    """

    y = regs["y"]
    x = regs["x"]
    cover_q = regs['cover_q']
    secret_q = regs['secret_q']
    si_rec = regs['si_rec']
    flag= regs['flag']
    ky = len(y)
    kx = len(x)
    cl = ClassicalRegister(ky + kx +2*len(secret_q)+len(cover_q)+len(flag), "cl_neqr")
    qc.add_register(cl)

    idx = 0
    for q in reversed(flag):
        qc.measure(q, cl[idx])
        idx += 1
        
    for q in reversed(si_rec):
        qc.measure(q, cl[idx])
        idx += 1
        
    for q in reversed(secret_q):
        qc.measure(q, cl[idx])
        idx += 1
        
    for q in reversed(cover_q):
        qc.measure(q, cl[idx])
        idx += 1
      
    for q in reversed(x):
        qc.measure(q, cl[idx])
        idx += 1
      
    for q in reversed(y):
        qc.measure(q, cl[idx])
        idx += 1



    backend = AerSimulator(method=method)
    tqc = transpile(qc, backend, optimization_level=3)
    result = backend.run(tqc, shots=shots).result()

    return result.get_counts()


def display_the_hist(counts):
 if counts:
    total_shots = sum(counts.values())
    probabilities = {state: count / total_shots for state, count in counts.items()}

    # Plot probability histogram
    plt.figure(figsize=(30, 10))
    bars = plt.bar(probabilities.keys(), probabilities.values(), color='blue', alpha=0.7)

    for bar, prob in zip(bars, probabilities.values()):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{prob:.4f}', 
                 ha='center', va='bottom', fontsize=10, color='black', fontweight='bold')

    plt.title("Probability Histogram")
    plt.xlabel("Measured Quantum States")
    plt.ylabel("Probability")
    plt.xticks(rotation=90, fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
 else:
      print("No measurement data found for NEQR Encoded Image.")

