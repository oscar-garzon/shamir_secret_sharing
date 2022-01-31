import os
import sys
import unittest

from hypothesis import given, strategies as st

sys.path.append(os.getcwd())

from src import utils

class TestUtils(unittest.TestCase):

    def test_escribir_archivo(self):
        utils.escribir_archivo('texto', 'txt', 'Estoy probando \n si funciona\n este método.')

    @given(st.lists(st.tuples(st.integers(),st.integers())))
    def test_list_to_str(self, lst):
        res_obtenido = utils.list_to_str(lst)
        self.assertIsInstance(res_obtenido, str)

        res_obtenido = utils.list_to_str([(1,2),(3,4)])
        self.assertEqual(res_obtenido,'(1, 2)\n(3, 4)\n')

if __name__ == '__main__':
    unittest.main()
