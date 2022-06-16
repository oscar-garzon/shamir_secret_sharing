import os
import sys
import unittest

from hypothesis import example, given, strategies as st

sys.path.append(os.getcwd())

from src.descifrar import Descifrador


class Tests(unittest.TestCase):
    """! Clase para pruebas unitarias de la clase {@link Descifrador}"""

    @given(
        st.integers(min_value=1),
        st.integers(min_value=1),
        st.integers(min_value=1),
        st.integers(min_value=1),
    )
    def test_get_key(self, k, x1, x2, x3):
        """! Test unitario para ver si _get_key regresa la key correcta.
        Se construye un polinomio con coeficientes aleatorios. Se evaluan
        r puntos y con estos se construye un Descifrador. Se espera que
        _get_key regrese el término independiente del polinomio original."""
        p = 208351617316091241234326746312124448251235562226470491514186331217050270460481
        evaluaciones = []
        for i in range(1, 5):
            valor = k + x1 * i + x2 * i * i + 3 * i * i * i
            evaluaciones.append((i, valor % p))
        d = Descifrador(evaluaciones, "asdfas")
        self.assertEqual(d._get_key(), k)


if __name__ == "__main__":
    unittest.main()
