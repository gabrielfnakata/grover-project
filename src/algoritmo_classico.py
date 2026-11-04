def algoritmoClassico():
    todasPossibilidades = ["00", "01", "10", "11"];

    elementoProcurado = "11";

    tentativas = 0;

    for elemento in todasPossibilidades:
        tentativas += 1;

        if elemento == elementoProcurado:
            print("Encontrado:", elemento);
            print("Tentativas:", tentativas);
            break;