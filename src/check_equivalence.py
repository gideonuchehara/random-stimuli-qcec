from qiskit import execute, Aer
from collections import Counter
from qiskit.quantum_info.analysis import hellinger_fidelity
import copy
import numpy as np

def are_circuits_equivalent(circuit1, circuit2, shots=1000):
    """Check if two quantum circuits are equivalent by comparing their measurement probabilities.

    Args:
        circuit1 (QuantumCircuit): The first quantum circuit.
        circuit2 (QuantumCircuit): The second quantum circuit.
        shots (int): The number of shots to use for the quantum simulation.

    Returns:
        bool: True if the circuits are equivalent, False otherwise.
    """
    simulator = Aer.get_backend('qasm_simulator')

    job1 = execute(circuit1, simulator, shots=shots)
    counts1 = job1.result().get_counts()

    job2 = execute(circuit2, simulator, shots=shots)
    counts2 = job2.result().get_counts()

    # Normalize the counts to probabilities
    counts1 = {k: v / shots for k, v in counts1.items()}
    counts2 = {k: v / shots for k, v in counts2.items()}

    # Fill in missing keys with zero counts
    counts1 = Counter(counts1)
    counts2 = Counter(counts2)
    counts1 += Counter({k: 0 for k in counts2.keys() if k not in counts1})
    counts2 += Counter({k: 0 for k in counts1.keys() if k not in counts2})
    
    counts1_keys = sorted(counts1)
    counts2_keys = sorted(counts2)
    
    new_counts1 = {key:counts1[key] for key in counts1_keys}
    new_counts2 = {key:counts2[key] for key in counts2_keys}
    
    counts1_array = np.array(list(new_counts1.values()))
    counts2_array = np.array(list(new_counts2.values()))
    
    # check fidelity with Helinger_fidelity    
    fidelity = hellinger_fidelity(new_counts1, new_counts2)

    # Check if the fidelity is close to 1
    return np.abs(1 - fidelity) < 0.1 # at least 90% fidelity is acceptable
