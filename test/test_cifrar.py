import os
import sys
import unittest
from unittest.mock import patch

from hypothesis import given, strategies as st

sys.path.append(os.getcwd())

from src.cifrar import Cifrador


class Tests(unittest.TestCase):
    @patch("builtins.input", lambda _: "sinaloa")
    def setUp(self):
        """ Crea una cifrador. """
        self.evals = 8
        self.evals_min = 4
        self.c = Cifrador(self.evals, self.evals_min)

    @given(st.integers())
    def test_horner(self, x):
        self.assertEqual(
            self.c._horner(x, [6, 2, 3, 2]), 6 + 2 * x + 3 * x * x + 2 * x * x * x
        )
        self.assertEqual(
            self.c._horner(x, [1234, 567, 23, 45]),
            1234 + 567 * x + 23 * x * x + 45 * x * x * x,
        )

    def test_obtener_evaluaciones(self):
        """ Verifica que obtener_evaluaciones regresa una lista con
        el números de evaluaciones(tuplas) requeridas"""
        evals = self.c.obtener_evaluaciones()
        self.assertEqual(len(evals), self.evals)


if __name__ == "__main__":
    unittest.main()
