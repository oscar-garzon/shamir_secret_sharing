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
        self.c = Cifrador(8, 4)

    def test_constructor(self):
        self.assertIsInstance(self.c, Cifrador)
        self.assertRaises(Exception, Cifrador, 5, 7)

    
    @given(st.integers())
    def test_horner(self, x):
        self.assertEqual(self.c._horner(x, [6,2,3,2]), 6 + 2*x + 3*x*x + 2*x*x*x)
        self.assertEqual(self.c._horner(x, [1234, 567, 23, 45]), 1234 + 567*x + 23*x*x + 45*x*x*x)


    def test_obtener(self):
        """! Test unitario para verificar que el número de evaluaciones
        devueltas por Cifrador.obtener sea correcto"""

        self.assertEqual(len(self.c.obtener()[1]), 8)


if __name__ == '__main__':
    unittest.main()
