import os
import sys
import unittest
from unittest.mock import patch

from hypothesis import given, strategies as st

sys.path.append(os.getcwd())

from src.cifrar import Cifrador

class Tests(unittest.TestCase):

    @patch('builtins.input', lambda _: 'sinaloa')
    def setUp(self):
        """ Crea una cifrador. """
        self.evals = 8
        self.evals_min = 4
        self.c = Cifrador(self.evals, self.evals_min)

    # def test_constructor(self):
    #     self.assertIsInstance(self.c, Cifrador)
    #     self.assertRaises(Exception, Cifrador, 5, 7)

    
    # @given(st.integers())
    # def test_horner(self, x):
    #     self.assertEqual(self.c._horner(x, [6,2,3,2]), 6 + 2*x + 3*x*x + 2*x*x*x)
    #     self.assertEqual(self.c._horner(x, [1234, 567, 23, 45]), 1234 + 567*x + 23*x*x + 45*x*x*x)


    # def test_obtener(self):
    #     """! Test unitario para verificar que el número de evaluaciones
    #     devueltas por Cifrador.obtener sea correcto"""

    #     self.assertEqual(len(self.c.obtener()[1]), 8)
    
    # def test_cifrar(self):
    #     """ Test unitario para verificar que el método test regresa un
    #     objeto de tipo diccionario con cuatro elementos string: cipher.nonce, 
    #     header, ciphertext y tag"""

    def test_obtener_evaluaciones(self):
        """ Verifica que obtener_evaluaciones regresa una lista con
        el números de evaluaciones(tuplas) requeridas"""
        evals = self.c.obtener_evaluaciones()
        self.assertEqual(len(evals), self.evals)



if __name__ == '__main__':
    unittest.main()
