from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def algoritmoQuantico(alvo="11", shots=1000):
    # 1
    qc = QuantumCircuit(2, 2)
    # 2
    qc.h([0, 1])

    # 3
    for i, bit in enumerate(reversed(alvo)):
        if bit == '0':
            qc.x(i)
    qc.cz(0, 1)

    for i, bit in enumerate(reversed(alvo)):
        if bit == '0':
            qc.x(i)
    # 4
    qc.h([0, 1])
    qc.x([0, 1])
    qc.cz(0, 1)
    qc.x([0, 1])
    qc.h([0, 1])

    # 5
    qc.measure([0, 1], [0, 1])

    # 6
    simulator = AerSimulator()
    compiled = transpile(qc, simulator)

    result = simulator.run(
        compiled,
        shots=shots
    ).result()

    # 7
    counts = result.get_counts()
    print("Resultados:", counts)
    print("Shots executados:", shots)
    print("Iteracoes de Grover por shot: 1")
    print("Consultas ao oraculo por shot: 1")
    print("Alvo procurado:", alvo)

    return counts

def superposicaoUniforme(shots=1000):
    qc = QuantumCircuit(2, 2)
    qc.h([0, 1])
    qc.measure([0, 1], [0, 1])

    simulator = AerSimulator()
    compiled = transpile(qc, simulator)

    result = simulator.run(
        compiled,
        shots=shots
    ).result()

    counts = result.get_counts()
    print("Resultados (superposicao uniforme):", counts)
    print("Shots executados:", shots)

    return counts
