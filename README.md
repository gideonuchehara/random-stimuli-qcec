# Random Stimuli Generation for the Verification of Quantum Circuits
Lukas Burgholzer, Richard Kueng, Robert Wille
August 30, 2023

The verification of quantum circuits is a crucial aspect in ensuring the correctness of quantum
algorithms and descriptions at various levels of abstraction. As quantum circuits grow in size and
complexity, the task of their verification becomes increasingly challenging. Traditional verification
methods that involve the comparison of entire unitary matrices become computationally expensive
and infeasible for larger circuits.

This report focuses on a recent study by Burgholzer et al. titled ”Random Stimuli Generation
for Quantum Circuits” which offers a novel approach to this problem. The study introduces a
method of using random stimuli to verify quantum circuits. It presents three schemes for quantum
stimuli generation that offer a trade-off between the error detection rate and efficiency. The paper
shows that even with a few randomly-chosen stimuli generated from the proposed schemes, high
error detection rates can be achieved for quantum circuits.

The goal of this report is to reproduce the results of this paper using Qiskit, a popular open-
source quantum computing framework, and to present a comprehensive experimental framework
for the task.

### Requirements and Dependencies
- Qiskit
- Numpy
- Pytest
- Matplotlib

### Instructions
- Install the requirements and dependencies listed above
- The experiments.ipynb contains the code for running the experiments and extracting relevant data

### File Implementations
- The doc folder contains the report for the reproduced result
- The experiments.ipynb file is the jupyter notebook that reproduces the paper
- The test folder contains files for test cases of some functions used in our implementation

## References

[1] L. Burgholzer, R. Kueng, and R. Wille, “Random stimuli generation for the verification of quantum circuits,” in Proceedings of the 26th Asia and South Pacific Design Automation Conference, 2021, pp. 767–772.


