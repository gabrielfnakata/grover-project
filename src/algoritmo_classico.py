TODAS_POSSIBILIDADES = ["00", "01", "10", "11"]


def algoritmoClassico(alvo="11"):
    tentativas = 0

    for elemento in TODAS_POSSIBILIDADES:
        tentativas += 1

        if elemento == alvo:
            print("Encontrado:", elemento)
            print("Verificacoes realizadas:", tentativas)
            break

    return tentativas


def estatisticasClassicas():
    """
    Calcula as estatisticas da busca linear considerando que qualquer
    um dos estados pode ser o alvo com igual probabilidade.

    - Melhor caso: o alvo e o primeiro elemento -> 1 verificacao.
    - Pior caso: o alvo e o ultimo elemento -> N verificacoes.
    - Media: (1 + 2 + ... + N) / N = (N + 1) / 2 verificacoes.
      A complexidade media da busca linear e O(N).

    n e derivado de TODAS_POSSIBILIDADES para evitar valores fixos
    desconectados da estrutura de dados real.

    Retorna um dicionario com as tres metricas.
    """
    n = len(TODAS_POSSIBILIDADES)
    melhor = 1
    pior = n
    media = (n + 1) / 2  # média

    return {"melhor": melhor, "media": media, "pior": pior}
