from src import algoritmoClassico, algoritmoQuantico, superposicaoUniforme, estatisticasClassicas


def main():
    alvo = input("Digite o estado-alvo (00, 01, 10 ou 11) [padrao: 11]: ").strip()
    if alvo == "":
        alvo = "11"

    if alvo not in ("00", "01", "10", "11"):
        print("Estado invalido. Use 00, 01, 10 ou 11.")
        return
    print("=== Busca classica ===")
    verificacoes = algoritmoClassico(alvo=alvo)

    stats = estatisticasClassicas()

    print("\n=== Busca quantica com Qiskit Aer ===")
    shots = 1000

    print("--- Antes de Grover (superposicao uniforme) ---")
    resultados_antes = superposicaoUniforme(shots=shots)

    print("\n--- Depois de Grover (oraculo + difusor) ---")
    resultados_depois = algoritmoQuantico(alvo=alvo, shots=shots)

    acertos = resultados_depois.get(alvo, 0)
    taxa_de_acerto = acertos / shots * 100

    estados = ["00", "01", "10", "11"]
    print("\n=== Amplificacao de amplitude (antes vs depois de Grover) ===")
    print(f"{'Estado':<8} {'Antes':>10} {'Depois':>10}")
    print("-" * 30)
    for estado in estados:
        antes = resultados_antes.get(estado, 0) / shots * 100
        depois = resultados_depois.get(estado, 0) / shots * 100
        marcador = " <-- alvo" if estado == alvo else ""
        print(f"{estado:<8} {antes:>9.1f}% {depois:>9.1f}%{marcador}")

    print("\n=== Comparacao conceitual: classica vs Grover ===")

    print(f"\nAlvo selecionado: {alvo} (entre 4 possiveis)")

    print("\n-- Busca classica (sequencial) --")
    print(f"  Verificacoes para '{alvo}' nesta execucao: {verificacoes}")
    print(f"  Melhor caso (qualquer alvo):  {stats['melhor']} verificacao")
    print(f"  Media esperada (qualquer alvo): {stats['media']} verificacoes")
    print(f"  Pior caso (qualquer alvo):    {stats['pior']} verificacoes")
    print("  Complexidade: O(N) — a media numerica exata e (N+1)/2 verificacoes.")

    print("\n-- Algoritmo de Grover (quantico) --")
    print("  Iteracoes de Grover por execucao do circuito: 1")
    print("  Consultas ao oraculo por execucao do circuito: 1")
    print(f"  Shots realizados: {shots}")
    print(
        f"  Cada shot e uma execucao independente do circuito, "
        f"com 1 consulta ao oraculo. Total: {shots} consultas no experimento."
    )
    print(f"  Taxa de acerto observada: {taxa_de_acerto:.1f}%")
    print("  Complexidade: O(sqrt(N)) consultas ao oraculo.")

    print("\n-- Observacoes --")
    print(
        "  A comparacao e conceitual: refere-se ao numero de consultas ao oraculo,"
        "\n  nao ao tempo de execucao em hardware real."
    )
    print(
        "  Teoricamente, antes de Grover cada estado tem 25% de probabilidade."
        "\n  No circuito ideal com 2 qubits e uma iteracao, o alvo atinge 100%."
        "\n  As frequencias observadas antes de Grover podem variar entre execucoes,"
        "\n  pois dependem das medicoes do circuito de superposicao."
    )


if __name__ == "__main__":
    main()
