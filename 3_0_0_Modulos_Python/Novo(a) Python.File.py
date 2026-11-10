import unittest

# Função que queremos testar
def somar(a, b):
    return a + b

# Classe de teste
class TesteOperacoes(unittest.TestCase):
    
    def test_soma_numeros_positivos(self):
        self.assertEqual(somar(2, 3), 5)

    def test_soma_numeros_negativos(self):
        self.assertEqual(somar(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
