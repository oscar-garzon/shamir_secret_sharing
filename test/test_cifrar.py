import os
import sys
import unittest

from hypothesis import given, strategies as st

sys.path.append(os.getcwd())

from src.cifrar import Cifrador

class Tests(unittest.TestCase):

    def setUp(self):
        """ Crea una cifrador y le da un documento a cifrar"""
        self.c = Cifrador('probando123', 8, 4)


    def test_constructor(self):
        self.assertIsInstance(self.c, Cifrador)
        self.assertRaises(Exception, Cifrador, 'proba', 5, 7)


    def test_cifra_aes(self):
        """! Test unitario para encriptar data con AES"""

        self.c._cifra_aes



    @given(st.integers())
    def test_horner(self, x):
        self.assertEqual(self.c._horner(x, [6,2,3,2]), 6 + 2*x + 3*x*x + 2*x*x*x)
        self.assertEqual(self.c._horner(x, [1234, 567, 23, 45]), 1234 + 567*x + 23*x*x + 45*x*x*x)  

if __name__ == '__main__':
    unittest.main()
