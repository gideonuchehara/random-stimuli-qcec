from qiskit import Aer, execute
from qiskit.quantum_info import Statevector
from qiskit.circuit.random import random_circuit
from qiskit.circuit.library import HGate, SGate, TGate, XGate, YGate, ZGate, CCXGate
from qiskit.circuit import QuantumCircuit, Measure
import numpy as np
import copy


def inject_error(G, error_type, num_errors=1):
    """Injects errors into the given quantum circuit.

    Args:
        circuit (QuantumCircuit): The quantum circuit to inject errors into.
        error_type (str): The type of error to inject. Options are 'remove', 'insert', 'toffoli_beginning', 'toffoli_end'.
        num_errors (int): The number of errors to inject.

    Returns:
        QuantumCircuit: The quantum circuit with injected errors.
    """
    circuit = copy.deepcopy(G)
    gate_dict = {'X': XGate(), 'Y': YGate(), 'Z': ZGate(), 'H': HGate(), 'S': SGate(), 'T': TGate()}
    
    if error_type == 'toffoli_beginning' or error_type == 'toffoli_end':
        num_errors = 10

    for _ in range(num_errors):
        if error_type == 'remove':
            if len(circuit.data) > 0:  # Check if there are gates to remove
                n = range(len(circuit.data))
                remove_idx = [idx for idx in n if not isinstance(circuit.data[idx].operation, Measure)]
                idx = np.random.choice(remove_idx)
                circuit.data.pop(idx)

        elif error_type == 'insert':
            gate = np.random.choice(list(gate_dict.keys()))
            idx = np.random.randint(len(circuit.data) + 1)
            qubit = np.random.choice(circuit.qubits)
            circuit.data.insert(idx, (gate_dict[gate], [qubit], []))

        elif error_type == 'toffoli_beginning':
            qubits = np.random.choice(range(circuit.num_qubits), size=3, replace=False)
            circuit.data.insert(0, (CCXGate(), [circuit.qubits[i] for i in qubits], []))

        elif error_type == 'toffoli_end':
            qubits = np.random.choice(range(circuit.num_qubits), size=3, replace=False)
            circuit.data.append((CCXGate(), [circuit.qubits[i] for i in qubits], []))

    return circuit
