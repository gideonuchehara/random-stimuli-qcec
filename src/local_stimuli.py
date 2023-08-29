from qiskit import QuantumCircuit
from qiskit.circuit.library import XGate, HGate, SGate, IGate
import copy
import numpy as np

def local_stimuli(G: QuantumCircuit):
    """Applies a random gate from the set {I, X, H, XH, HS, XHS} to each qubit."""
    circuit = copy.deepcopy(G)
    stimuli = QuantumCircuit(circuit.num_qubits)
    
    def I_gates(q):
        stimuli.i(q)
        
    def X_gates(q):
        stimuli.x(q)
        
    def H_gates(q):
        stimuli.h(q)
        
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
    
    gates_list = [lambda q: I_gates(q), lambda q: X_gates(q),lambda q: H_gates(q), 
                  lambda q: XH_gates(q), lambda q: HS_gates(q),lambda q: XHS_gates(q)]

    for qubit in range(stimuli.num_qubits):
        np.random.choice(gates_list)(qubit)
        
    stimuli.barrier()

    return stimuli.compose(circuit)
