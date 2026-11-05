# Grover Project

Projeto desenvolvido em Python para demonstrar e comparar uma busca quântica utilizando o Algoritmo de Grover com uma busca clássica tradicional. Essas duas abordagens são utilizadas para encontrar um elemento específico (bits 11) dentro do conjunto de possibilidades.

## Como executar
1. Clone o repositório:
    ```bash
    git clone git@github.com:gabrielfnakata/grover-project.git
    ```

2. Entre na pasta:
    ```bash
    cd grover-project
    ```

3. Instale as dependências:
    ```bash
    pip install qiskit qiskit-aer
    ```

4. Execute o projeto:
    ```bash
    python main.py
    ```

## Comparacao dos algoritmos

O exemplo procura o estado `11` no conjunto `00`, `01`, `10` e `11`.
Na busca classica, a lista e percorrida em ordem e `11` e o ultimo elemento,
portanto esse caso faz 4 verificacoes. O numero depende da posicao do alvo;
para um alvo escolhido uniformemente entre as quatro posicoes, a media seria
2,5 verificacoes.

O circuito quantico aplica uma iteracao de Grover, isto e, uma consulta ao
oracle que marca `11`, seguida pelo difusor. O simulador roda o circuito em
1000 shots: cada shot e uma execucao/medicao do circuito, nao uma iteracao de
Grover. A taxa impressa indica a proporcao dessas medicoes que retornou `11`.
Como o simulador e ideal, esse resultado nao inclui os efeitos de ruido de um
hardware quantico real.

Essa demonstracao compara o numero de verificacoes classicas deste caso com
as iteracoes de Grover por execucao, mas nao demonstra vantagem pratica de
tempo: o espaco tem apenas quatro itens e o circuito foi repetido para obter
uma distribuicao de resultados.