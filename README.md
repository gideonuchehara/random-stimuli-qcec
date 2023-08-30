# random-stimuli-qcec

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
