from qiskit import QuantumCircuit, transpile
from qiskit.extensions import UnitaryGate
from qiskit.quantum_info import random_unitary
from qiskit.circuit.library import XGate, HGate, SGate, IGate
import numpy as np
import copy

def classical_stimuli(G: QuantumCircuit):
    """Prepares the circuit in a random computational basis state."""
    circuit = copy.deepcopy(G)
    bitstring = np.random.choice([0, 1], circuit.num_qubits)  # Random bitstring
    stimuli = QuantumCircuit(circuit.num_qubits)
    for qubit, bit in enumerate(bitstring):
        if bit:
            stimuli.x(qubit)  # Apply an X gate if the bit in the bitstring is 1
    
    stimuli.barrier()
    return stimuli.compose(circuit)