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
from calculadora import soma


# Todos os testes tem de iniciar com 'Test~~'
class TestCalculadora(unittest.TestCase):

    def test_soma_5_mais_5_igual_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (1, 1, 2),
            (2, 3, 5),
            (10, 10, 20),
            (20, 30, 50),
            (50, 100, 150)
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    def test_soma_error(self):
        with self.assertRaises(TypeError):
            soma('1', 10)


if __name__ == '__main__':
    unittest.main(verbosity=2)
