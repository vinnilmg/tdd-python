"""
TDD - Test Driven Development (Desenvolvimento dirigido a testes)

Red
Parte 1: Criar o teste e ver falha no teste

Green
Parte 2: Criar o código e ver o sucesso no teste

Refactor
Parte 3: Melhorar código
"""
try:
    import sys
    import os

    # Pegar o caminho do src
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

import unittest
from baconcomovos import bacon_com_ovos


class TestBaconComOvos(unittest.TestCase):

    def test_bacon_com_ovos_assertion_error(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('0')


    def test_bacon_com_ovos_retorna_bacon_com_ovos(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f"[{entrada}] não retornou [{saida}]")


    def test_bacon_com_ovos_retorna_passar_fome(self):
        entradas = (1, 2, 4, 7, 11)
        saida = 'Passar fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f"[{entrada}] não retornou [{saida}]"
                )


    def test_bacon_com_ovos_retorna_bacon(self):
        entradas = (6, 9, 12, 18, 21)
        saida = 'Bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f"[{entrada}] não retornou [{saida}]"
                )


    def test_bacon_com_ovos_retorna_ovos(self):
        entradas = (10, 50, 20, 25, 35)
        saida = 'Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f"[{entrada}] não retornou [{saida}]"
                )


if __name__ == '__main__':
    unittest.main(verbosity=2)
