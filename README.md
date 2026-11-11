# Grover Project

Projeto acadêmico desenvolvido em Python para demonstrar e comparar uma busca quântica utilizando o Algoritmo de Grover com uma busca clássica sequencial. O programa permite escolher qualquer um dos quatro estados de 2 bits (`00`, `01`, `10`, `11`) como alvo e exibe a amplificação de amplitude produzida pelo algoritmo, além de uma comparação conceitual entre as duas abordagens.

Todos os resultados são obtidos no simulador ideal `AerSimulator` do Qiskit e não incluem os efeitos de ruído de hardware quântico real.

---
### Qubits e superposição

Um qubit é a unidade básica de informação quântica. Ao contrário de um bit clássico, que assume apenas o valor 0 ou 1, um qubit pode estar em **superposição**: uma combinação linear de ambos os estados ao mesmo tempo. A porta **Hadamard (H)** é usada para colocar um qubit em superposição uniforme, atribuindo probabilidade igual de 50% para cada resultado ao ser medido.

Com 2 qubits, a aplicação de Hadamard em ambos gera superposição uniforme sobre os quatro estados `|00>`, `|01>`, `|10>` e `|11>`, cada um com probabilidade teórica de 25%.

### Oráculo

O oráculo é uma operação que identifica o estado-alvo sem revelar seu valor diretamente. No Algoritmo de Grover, o oráculo inverte a fase (sinal da amplitude) do estado-alvo, marcando-o para a etapa seguinte. Uma consulta ao oráculo equivale a uma verificação no contexto clássico.

Neste projeto, o oráculo é dinâmico: para qualquer alvo escolhido, o circuito aplica portas X nos qubits cujo bit correspondente no alvo é `0`, executa a porta CZ (que inverte a fase quando ambos os qubits estão em `|1>`), e depois desfaz as portas X. O Qiskit usa ordem little-endian: o bit mais à direita do estado corresponde ao qubit 0.

### Difusor

O difusor realiza a inversão sobre a média das amplitudes, amplificando a amplitude do estado marcado pelo oráculo e reduzindo as demais. A sequência de portas utilizada é: `H → X → CZ → X → H`.

### Amplificação de amplitude

A combinação oráculo + difusor constitui uma iteração de Grover. Para 2 qubits (N = 4 estados), uma única iteração é suficiente para elevar a probabilidade do estado-alvo a 100%.

---

## Busca clássica vs Algoritmo de Grover

### Busca clássica (sequencial)

A busca percorre a lista `["00", "01", "10", "11"]` elemento por elemento até encontrar o alvo. O número de verificações depende da posição do alvo na lista:

| Alvo | Verificações |
|------|-------------|
| 00   | 1 (melhor caso) |
| 01   | 2 |
| 10   | 3 |
| 11   | 4 (pior caso) |

Considerando que qualquer dos quatro alvos é igualmente provável:

- Melhor caso: 1 verificação
- Media esperada: (N+1)/2 = 2,5 verificações
- Pior caso: N = 4 verificações
- Complexidade: O(N)

### Algoritmo de Grover

O circuito aplica superposição uniforme, executa uma iteração de Grover (oráculo + difusor) e mede os qubits.

- Iterações de Grover por execução: 1
- Consultas ao oráculo por execução: 1
- Complexidade: O(sqrt(N)) consultas ao oráculo

O programa executa o circuito 1000 vezes (**shots**). Cada shot é uma execução independente do circuito com uma consulta ao oráculo. Os shots são usados para estimar a distribuição de probabilidade — não são iterações adicionais do algoritmo.

---

## Instalação e execução

### Pré-requisitos

- Python 3.8 ou superior
- pip

### 1. Clone o repositório

```bash
git clone git@github.com:gabrielfnakata/grover-project.git
cd grover-project
```

### 2. Instale as dependências

```bash
pip install qiskit qiskit-aer
```

### 3. Execute o projeto

```bash
python main.py
```

O programa solicita o estado-alvo no terminal. Pressionar Enter sem digitar nada usa `11` como padrão. Entradas fora de `00`, `01`, `10`, `11` são rejeitadas.

---

## Exemplo de saída

Execução com alvo `01`:

```
Digite o estado-alvo (00, 01, 10 ou 11) [padrao: 11]: 01

=== Busca classica ===
Encontrado: 01
Verificacoes realizadas: 2

=== Busca quantica com Qiskit Aer ===
--- Antes de Grover (superposicao uniforme) ---
Resultados (superposicao uniforme): {'11': 250, '10': 253, '01': 241, '00': 256}
Shots executados: 1000

--- Depois de Grover (oraculo + difusor) ---
Resultados: {'01': 1000}
Shots executados: 1000
Iteracoes de Grover por shot: 1
Consultas ao oraculo por shot: 1
Alvo procurado: 01

=== Amplificacao de amplitude (antes vs depois de Grover) ===
Estado        Antes     Depois
------------------------------
00            25.6%       0.0%
01            24.1%     100.0% <-- alvo
10            25.3%       0.0%
11            25.0%       0.0%

=== Comparacao conceitual: classica vs Grover ===

Alvo selecionado: 01 (entre 4 possiveis)

-- Busca classica (sequencial) --
  Verificacoes para '01' nesta execucao: 2
  Melhor caso (qualquer alvo):  1 verificacao
  Media esperada (qualquer alvo): 2.5 verificacoes
  Pior caso (qualquer alvo):    4 verificacoes
  Complexidade: O(N) — a media numerica exata e (N+1)/2 verificacoes.

-- Algoritmo de Grover (quantico) --
  Iteracoes de Grover por execucao do circuito: 1
  Consultas ao oraculo por execucao do circuito: 1
  Shots realizados: 1000
  Cada shot e uma execucao independente do circuito, com 1 consulta ao oraculo. Total: 1000 consultas no experimento.
  Taxa de acerto observada: 100.0%
  Complexidade: O(sqrt(N)) consultas ao oraculo.

-- Observacoes --
  A comparacao e conceitual: refere-se ao numero de consultas ao oraculo,
  nao ao tempo de execucao em hardware real.
  Teoricamente, antes de Grover cada estado tem 25% de probabilidade.
  No circuito ideal com 2 qubits e uma iteracao, o alvo atinge 100%.
  As frequencias observadas antes de Grover podem variar entre execucoes,
  pois dependem das medicoes do circuito de superposicao.
```

---

## Testes automatizados

Os testes utilizam `unittest` (biblioteca padrão do Python) e cobrem:

| Conjunto | Casos |
|----------|-------|
| Busca clássica - verificações por alvo | 5 |
| Estatísticas clássicas - melhor/média/pior caso | 4 |
| Algoritmo de Grover - 100% de acerto para os 4 alvos | 6 |
| Superposição uniforme - distribuição e soma dos shots | 3 |
| Validação de entrada - padrão e rejeição de alvos inválidos | 5 |
| **Total** | **23** |

### Como executar os testes

A partir da raiz do projeto:

```bash
python -m unittest discover -s tests -v
```

Resultado esperado:

```
Ran 23 tests in ~2s
OK
```

---

## Limitações

- O projeto usa apenas 2 qubits (N = 4 estados). A vantagem do Grover sobre a busca clássica torna-se mais expressiva conforme N cresce.
- Uma única iteração de Grover é o número ótimo para N = 4. Para N maior, o número ideal de iterações cresce proporcionalmente a sqrt(N).
- Os resultados são obtidos no simulador ideal `AerSimulator`, sem ruído. Em hardware quântico real, o resultado seria probabilístico e sujeito a erros.
- Os shots são repetições para estimar a distribuição de probabilidade do circuito. Não representam iterações adicionais do algoritmo nem múltiplas consultas ao oráculo em uma única execução.
