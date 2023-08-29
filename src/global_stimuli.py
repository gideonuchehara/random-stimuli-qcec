from qiskit import QuantumCircuit
from qiskit.circuit.library import CXGate, HGate, SGate
import random
import copy
import numpy as np

def global_stimuli(G: QuantumCircuit, num_layers: int = 2):
    """Generates global stimuli for a given quantum circuit.

    Args:
        G (QuantumCircuit): The quantum circuit for which to generate stimuli.
        num_layers (int): The number of gate layers in the stimuli.

    Returns:
        QuantumCircuit: The resulting quantum circuit after applying the stimuli.
    """
    # Copy the circuit
    circuit = copy.deepcopy(G)

    # Create a new circuit for the stimuli
    stimuli = QuantumCircuit(circuit.num_qubits)
    
    def I_gates(q):
        stimuli.i(q)
        
    def X_gates(q):
        stimuli.x(q)
        
    def H_gates(q):
        stimuli.h(q)
        
    def S_gates(q):
        stimuli.s(q)
        
    def XH_gates(q):
        stimuli.x(q)
        stimuli.h(q)
        
    def HS_gates(q):
        stimuli.h(q)
        stimuli.s(q)
        
    def XHS_gates(q):
        stimuli.x(q)
        stimuli.h(q)
        stimuli.s(q)
    
    gates = [lambda q: I_gates(q), lambda q: X_gates(q),lambda q: H_gates(q), lambda q: S_gates(q),
                  lambda q: XH_gates(q), lambda q: HS_gates(q),lambda q: XHS_gates(q), CXGate()]
    
    # randomly select the number of layers (l>1) based on the number of qubits in the circuit
    n = circuit.num_qubits
    if n > 2:
        num_layers = random.choice(range(2, n+1))

    for _ in range(num_layers):
        # Choose a random gate for each qubit
        for qubit in range(circuit.num_qubits):
            # gate = np.random.choice(gates)
            gate = random.choice(gates)

            # For single-qubit gates
            if not isinstance(gate, CXGate):
                gate(qubit)
            
            # For two-qubit gates (CNOT)
            else:
                control_qubit = qubit
                qubits_list = list(range(circuit.num_qubits))
                qubits_list.remove(control_qubit)
                target_qubit = np.random.choice(qubits_list)
                stimuli.append(gate, [control_qubit, target_qubit])
                
        stimuli.barrier()

    # Compose the stimuli with the original circuit
    combined_circuit = stimuli.compose(circuit)

    return combined_circuit
