from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def algoritmoQuantico():
    # 1. Criar circuito com 2 qubits e 2 bits classicos
    qc = QuantumCircuit(2, 2);

    # 2. Criar superposicao
    qc.h([0, 1]);

    # 3. Oracle: marcar o estado 11
    qc.cz(0, 1);

    # 4. Difusor
    qc.h([0, 1]);
    qc.x([0, 1]);
    qc.cz(0, 1);
    qc.x([0, 1]);
    qc.h([0, 1]);

    # 5. Medicao
    qc.measure([0, 1], [0, 1]);

    # 6. Executar no simulador
    simulator = AerSimulator();
    compiled = transpile(qc, simulator);

    result = simulator.run(
        compiled,
        shots=1000
    ).result();

    # 7. Mostrar resultados
    counts = result.get_counts();
    print("Resultados:", counts);
