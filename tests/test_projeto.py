"""
Testes automatizados do Grover Project.

Executar a partir da raiz do projeto:
    python -m unittest tests/test_projeto.py -v

Ou para todos os testes da pasta tests/:
    python -m unittest discover -s tests -v

Os testes cobrem:
  - Busca classica: numero de verificacoes para cada alvo.
  - Estatisticas classicas: melhor caso, media e pior caso.
  - Algoritmo de Grover: taxa de acerto de 100% para os quatro estados.
  - Validacao de entrada: rejeicao de alvos invalidos e padrao "11".
"""

import unittest
from io import StringIO
from unittest.mock import patch

from src.algoritmo_classico import algoritmoClassico, estatisticasClassicas
from src.algoritmo_quantico import algoritmoQuantico, superposicaoUniforme

class TestBuscaClassica(unittest.TestCase):
    """Verifica o numero de verificacoes da busca linear para cada alvo."""

    def test_alvo_00_primeira_posicao(self):
        with patch("sys.stdout", new_callable=StringIO):
            resultado = algoritmoClassico(alvo="00")
        self.assertEqual(resultado, 1)

    def test_alvo_01_segunda_posicao(self):
        with patch("sys.stdout", new_callable=StringIO):
            resultado = algoritmoClassico(alvo="01")
        self.assertEqual(resultado, 2)

    def test_alvo_10_terceira_posicao(self):
        with patch("sys.stdout", new_callable=StringIO):
            resultado = algoritmoClassico(alvo="10")
        self.assertEqual(resultado, 3)

    def test_alvo_11_quarta_posicao(self):
        with patch("sys.stdout", new_callable=StringIO):
            resultado = algoritmoClassico(alvo="11")
        self.assertEqual(resultado, 4)

    def test_padrao_e_11(self):
        with patch("sys.stdout", new_callable=StringIO):
            resultado = algoritmoClassico()
        self.assertEqual(resultado, 4)


class TestEstatisticasClassicas(unittest.TestCase):
    """Verifica os valores de melhor caso, media e pior caso."""

    def setUp(self):
        self.stats = estatisticasClassicas()

    def test_melhor_caso(self):
        self.assertEqual(self.stats["melhor"], 1)

    def test_media(self):
        self.assertEqual(self.stats["media"], 2.5)

    def test_pior_caso(self):
        self.assertEqual(self.stats["pior"], 4)

    def test_retorna_dicionario(self):
        self.assertIsInstance(self.stats, dict)
        self.assertIn("melhor", self.stats)
        self.assertIn("media", self.stats)
        self.assertIn("pior", self.stats)

class TestAlgoritmoQuantico(unittest.TestCase):
    """
    Verifica que o algoritmo de Grover encontra cada alvo com 100% de
    probabilidade no simulador ideal (AerSimulator), usando 1000 shots.
    """

    SHOTS = 1000

    def _executar(self, alvo):
        """Executa o circuito suprimindo saida no terminal."""
        with patch("sys.stdout", new_callable=StringIO):
            counts = algoritmoQuantico(alvo=alvo, shots=self.SHOTS)
        return counts

    def test_grover_alvo_00(self):
        counts = self._executar("00")
        self.assertEqual(counts.get("00", 0), self.SHOTS,
                         "Esperado 100% de acerto para o alvo '00'")

    def test_grover_alvo_01(self):
        counts = self._executar("01")
        self.assertEqual(counts.get("01", 0), self.SHOTS,
                         "Esperado 100% de acerto para o alvo '01'")

    def test_grover_alvo_10(self):
        counts = self._executar("10")
        self.assertEqual(counts.get("10", 0), self.SHOTS,
                         "Esperado 100% de acerto para o alvo '10'")

    def test_grover_alvo_11(self):
        counts = self._executar("11")
        self.assertEqual(counts.get("11", 0), self.SHOTS,
                         "Esperado 100% de acerto para o alvo '11'")

    def test_retorna_dicionario(self):
        counts = self._executar("11")
        self.assertIsInstance(counts, dict)

    def test_soma_dos_shots(self):
        counts = self._executar("11")
        self.assertEqual(sum(counts.values()), self.SHOTS)

class TestSuperposicaoUniforme(unittest.TestCase):
    """
    Verifica que o circuito de referencia (apenas Hadamard) retorna
    os quatro estados e que a soma dos counts equivale aos shots.
    """

    SHOTS = 1000

    def test_soma_dos_shots(self):
        with patch("sys.stdout", new_callable=StringIO):
            counts = superposicaoUniforme(shots=self.SHOTS)
        self.assertEqual(sum(counts.values()), self.SHOTS)

    def test_retorna_dicionario(self):
        with patch("sys.stdout", new_callable=StringIO):
            counts = superposicaoUniforme(shots=self.SHOTS)
        self.assertIsInstance(counts, dict)

    def test_todos_os_estados_possiveis(self):

        with patch("sys.stdout", new_callable=StringIO):
            counts = superposicaoUniforme(shots=self.SHOTS)
        for estado in ("00", "01", "10", "11"):
            self.assertGreater(counts.get(estado, 0), 0,
                               f"Estado '{estado}' nao apareceu nos resultados")


class TestValidacaoEntrada(unittest.TestCase):
    """
    Verifica a logica de validacao do main.py sem executar o programa
    completo: testa o padrao "11" e a rejeicao de entradas invalidas.
    """

    def _executar_main(self, entrada):
        """Simula uma execucao do main com a entrada fornecida."""
        from main import main
        with patch("builtins.input", return_value=entrada), \
             patch("sys.stdout", new_callable=StringIO) as saida:
            main()
        return saida.getvalue()

    def test_entrada_vazia_usa_padrao_11(self):
        saida = self._executar_main("")
        self.assertIn("11", saida)
        self.assertNotIn("Estado invalido", saida)

    def test_entrada_invalida_exibe_erro(self):
        saida = self._executar_main("99")
        self.assertIn("Estado invalido", saida)

    def test_entrada_invalida_nao_executa_algoritmo(self):
        saida = self._executar_main("abc")
        self.assertNotIn("Encontrado", saida)
        self.assertNotIn("Resultados:", saida)

    def test_alvo_valido_00_executa(self):
        saida = self._executar_main("00")
        self.assertIn("Encontrado: 00", saida)
        self.assertNotIn("Estado invalido", saida)

    def test_alvo_valido_11_executa(self):
        saida = self._executar_main("11")
        self.assertIn("Encontrado: 11", saida)
        self.assertNotIn("Estado invalido", saida)


if __name__ == "__main__":
    unittest.main()
