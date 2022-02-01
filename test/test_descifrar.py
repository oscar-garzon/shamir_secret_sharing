import os
import sys
import unittest

from hypothesis import example, given, strategies as st

sys.path.append(os.getcwd())

from src.descifrar import Descifrador
from src.utils import horner

class TestCifrador(unittest.TestCase):
    """! Clase para pruebas unitarias de la clase {@link Descifrador}"""


    def setUp(self):
        """ Crea una descifrador y le da un criptograma a descifrar"""
        self.c = Descifrador([(1,13),(2,38),(3,93),(4,190)], 'encrypted.bin')

    
    def test_evalua_poli(self):
        """ Test unitario para _evalua_poli"""

        self.assertEqual(self.c._evalua_poli(0), 4)
        self.assertEqual(self.c._evalua_poli(1), -6)
        self.assertEqual(self.c._evalua_poli(2), 4)
        self.assertEqual(self.c._evalua_poli(3), -1)


    @given(st.integers(min_value = 1), st.integers(min_value = 1), st.integers(min_value = 1), st.integers(min_value = 1))
    def test_get_key(self, x, y, z, k):
        """! Test unitario para ver si _get_key regresa la key correcta.
        Se construye un polinomio con coeficientes aleatorios. Se evaluan
        r puntos y con estos se construye un Descifrador. Se espera que
        _get_key regrese el término independiente del polinomio original."""
        p = 208351617316091241234326746312124448251235562226470491514186331217050270460481
        evaluaciones = []
        for i in range(1,5):
            valor = k + z*i + y*i*i + x*i*i*i
            evaluaciones.append((i, valor % p))
        d = Descifrador(evaluaciones, b'asdfas')
        self.assertEqual(d._get_key(), k)


    # def test_descifra(self):
    #     """! Test unitario para Descifrador.descifra. Verifica que se regrese
    #     el contenido claro del criptograma"""
    #     self.assertEqual(self.c.descifra, 'probando123')


 
if __name__ == '__main__':
    unittest.main()


