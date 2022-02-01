import os
import sys
import unittest
import hashlib
from  unittest.mock import patch


from hypothesis import given, strategies as st

sys.path.append(os.getcwd())

from src.cifrar import Cifrador
from src.descifrar import Descifrador

class TestMain(unittest.TestCase):
    """! Clase para checar que se mantienen los invariantes del programana
    en general."""

    @patch('builtins.input', lambda _: 'sinaloa')
    def test_key(self):
        """! Test para verificar que la llave generada al hacer Cifrador.cifrar
        es igual a la obtenida por Descifrador"""

        c = Cifrador('asdfa', 8, 4)
        criptograma, evaluaciones = c.cifrar()

        d = Descifrador(evaluaciones, criptograma)
        self.assertEqual(c.key, d.key)


    @given(st.text(), st.text())
    def test_cifrar_descifrar(self, s, psw):    

        @patch('builtins.input', lambda _: psw)
        def cifrar_descifrar():
            """! Test para verificar que el mensaje encriptado es igual al
            desencriptado"""
            c = Cifrador(s, 8, 4)
            cripto, eval = c.cifrar()

            d = Descifrador(eval, 'encrypted.bin')
            self.assertEqual(s, d.descifra())

        cifrar_descifrar()
        
if __name__ == '__main__':
    unittest.main()