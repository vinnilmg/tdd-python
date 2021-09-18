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
from unittest.mock import patch
from Pessoa import Pessoa


class TestPessoa(unittest.TestCase):

    # Executa antes de cada teste
    def setUp(self):
        self.pessoa = Pessoa('Vinicius', 'Gomes')
        self.pessoa2 = Pessoa('Maria', 'Helena')

    # Executa dps de cada teste
    def tearDown(self):
        # print(f'Teste [{self._testMethodName}] finalizado.')
        pass

    def test_pessoa_nome_correto(self):
        self.assertEqual(self.pessoa.nome, 'Vinicius')
        self.assertEqual(self.pessoa2.nome, 'Maria')

    def test_pessoa_sobrenome_correto(self):
        self.assertEqual(self.pessoa.sobrenome, 'Gomes')
        self.assertEqual(self.pessoa2.sobrenome, 'Helena')

    def test_pessoa_dados_obtidos_false(self):
        self.assertFalse(self.pessoa.dados_obtidos)
        self.assertFalse(self.pessoa2.dados_obtidos)

    def test_pessoa_nome_e_str(self):
        self.assertIsInstance(self.pessoa.nome, str)
        self.assertIsInstance(self.pessoa2.nome, str)

    def test_pessoa_sobrenome_e_str(self):
        self.assertIsInstance(self.pessoa.sobrenome, str)
        self.assertIsInstance(self.pessoa2.sobrenome, str)

    def test_pessoa_dados_obtidos_sucesso(self):
        with patch('requests.get') as fake_req:
            fake_req.return_value.ok = True

            self.assertEqual(self.pessoa.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.pessoa.dados_obtidos)

            self.assertEqual(self.pessoa2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.pessoa2.dados_obtidos)

    def test_pessoa_dados_obtidos_falha_404(self):
        with patch('requests.get') as fake_req:
            fake_req.return_value.ok = False

            self.assertEqual(self.pessoa.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.pessoa.dados_obtidos)

            self.assertEqual(self.pessoa2.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.pessoa2.dados_obtidos)

    def test_pessoa_dados_obtidos_sucesso_e_falha(self):
        with patch('requests.get') as fake_req:
            fake_req.return_value.ok = True

            self.assertEqual(self.pessoa.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.pessoa.dados_obtidos)

            self.assertEqual(self.pessoa2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.pessoa2.dados_obtidos)

            fake_req.return_value.ok = False

            self.assertEqual(self.pessoa.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.pessoa.dados_obtidos)

            self.assertEqual(self.pessoa2.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.pessoa2.dados_obtidos)


if __name__ == '__main__':
    unittest.main(verbosity=2)
