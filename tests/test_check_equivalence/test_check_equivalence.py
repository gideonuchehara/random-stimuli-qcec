import os
import pytest
from qiskit import QuantumCircuit
from src.check_equivalence import *

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

# create the non-equivalent circuit lists by rotating the transpiled_circuit_list by one position
non_equivalent_circuit_list1 = original_circuit_list
non_equivalent_circuit_list2 = transpiled_circuit_list[1:] + transpiled_circuit_list[:1]

@pytest.mark.parametrize("circuit1,circuit2", zip(original_circuit_list, transpiled_circuit_list))
def test_equivalent_circuits(circuit1, circuit2):
    assert are_circuits_equivalent(circuit1, circuit2) == True

@pytest.mark.parametrize("circuit1,circuit2", zip(non_equivalent_circuit_list1, non_equivalent_circuit_list2))
def test_non_equivalent_circuits(circuit1, circuit2):
    assert are_circuits_equivalent(circuit1, circuit2) == False
