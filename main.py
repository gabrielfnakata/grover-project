from src import algoritmoClassico, algoritmoQuantico


def main():
    print("=== Busca classica ===")
    verificacoes_classicas = algoritmoClassico()

    print("\n=== Busca quantica com Qiskit Aer ===")
    shots = 1000
    resultados = algoritmoQuantico(shots=shots)

    acertos = resultados.get("11", 0)
    taxa_de_acerto = acertos / shots * 100

    print("\n=== Comparacao ===")
    print(f"Alvo procurado: 11 (entre 4 possibilidades)")
    print(f"Busca classica: {verificacoes_classicas} verificacoes neste caso.")
    print(
        "Busca de Grover: 1 iteracao e 1 consulta ao oracle por shot; "
        f"{shots} shots correspondem a {shots} execucoes do circuito."
    )
    print(f"Taxa de resultados iguais ao alvo no simulador: {taxa_de_acerto:.1f}%")
    print(
        "Observacao: os shots sao repeticoes para estimar o resultado, "
        "nao iteracoes adicionais dentro de cada circuito."
    )


if __name__ == "__main__":
    main()
