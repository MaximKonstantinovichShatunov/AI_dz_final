from qiskit import QuantumCircuit, transpile, Aer, execute

class QuantumSimulation:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.circuit = QuantumCircuit(num_qubits, num_qubits)
        
    def apply_hadamard(self, target_qubit):
        self.circuit.h(target_qubit)
        
    def measure(self, target_qubit, classical_bit):
        self.circuit.measure(target_qubit, classical_bit)
        
    def simulate(self):
        simulator = Aer.get_backend('aer_simulator')
        compiled_circuit = transpile(self.circuit, simulator)
        sim_result = execute(compiled_circuit, simulator).result()
        counts = sim_result.get_counts()
        return counts

# Создание экземпляра класса и проведение квантовой симуляции
sim = QuantumSimulation(1)
sim.apply_hadamard(0)
sim.measure(0, 0)
results = sim.simulate()

# Вывод результатов
for state, count in results.items():
    print(f"Состояние {state} встречается {count} раз")