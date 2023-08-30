import os
import pytest
from qiskit import QuantumCircuit
from src.check_equivalence import *
from src.inject_error import *

# load the original circuits
original_circuit_list = []
original_circuit_names = []
original_directory = "../circuits/original/"
for filename in sorted(os.listdir(original_directory)):
    if filename.endswith(".qasm"): 
        circ = QuantumCircuit.from_qasm_file(original_directory+filename)
        original_circuit_names.append(original_directory+filename)
        original_circuit_list.append(circ)

# load the transpiled circuits
transpiled_circuit_list = []
transpiled_circuit_names = []
transpiled_directory = "../circuits/transpiled/"
for filename in sorted(os.listdir(transpiled_directory)):
    if filename.endswith(".qasm"): 
        circ = QuantumCircuit.from_qasm_file(transpiled_directory+filename)
        transpiled_circuit_names.append(transpiled_directory+filename)
        transpiled_circuit_list.append(circ)

@pytest.mark.parametrize("circuit1, circuit2", zip(original_circuit_list, transpiled_circuit_list))
def test_inject_error(circuit1, circuit2):
    
    # take a circuit from transpiled_circuit_list and inject an error into the circuit 
    # error_circuit = inject_error(circuit2, 'insert')
    error_circuit = inject_error(circuit2, 'toffoli_beginning')
    
    # check if the error_circuit is not equivalent to the corresponding original circuit
    assert are_circuits_equivalent(circuit1, circuit2) == True and are_circuits_equivalent(circuit1, error_circuit) == False
