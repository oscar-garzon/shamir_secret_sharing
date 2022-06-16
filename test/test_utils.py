import os
import sys
import unittest

from hypothesis import given, strategies as st

sys.path.append(os.getcwd())

from src import utils

class TestUtils(unittest.TestCase):

    #  def test_escribir_archivo(self):
    #     utils.escribir_archivo('texto', 'txt', 'Estoy probando \n si funciona\n este método.')

    # @given(st.lists(st.tuples(st.integers(),st.integers())))
    # def test_list_to_str(self, lst):
    #     res_obtenido = utils.list_to_str(lst)
    #     self.assertIsInstance(res_obtenido, str)

    #     res_obtenido = utils.list_to_str([(1,2),(3,4)])
    #     self.assertEqual(res_obtenido,'(1, 2)\n(3, 4)\n') 

    #@given(st.lists(st.tuples(st.integers(), st.integers())))
    def test_escribir_fragmentos(self, fragmentos=[(1, 2), (1,45), (3, 895)]):
        """ Verifica que los valores de escribir_fragmentos sean los escritos
        en el archivo"""
        utils.escribir_fragmentos(fragmentos, 'prueba')
        with open('prueba.frg') as file:
            resultado_lectura = file.read().split('\n')
        print(resultado_lectura)
        self.assertEqual(resultado_lectura, ['(1, 2)', '(1, 45)', '(3, 895)'])

    #@given(fragmentos=st.lists(st.tuples(st.integers(), st.integers())))
    def test_fragmentos_a_lista(self, fragmentos=[(1, 2), (1,45), (3, 895)]):
        """Verifica que los fragmentos en doc_evaluaciones
        sean pasados a una lista como Tuple[int, int]"""
        utils.escribir_fragmentos(fragmentos, 'prueba')
        
        with open('prueba.frg') as file:
            resultados = utils.fragmentos_a_lista(file.read())

        self.assertEqual(fragmentos, resultados)
        

if __name__ == '__main__':
    unittest.main()
