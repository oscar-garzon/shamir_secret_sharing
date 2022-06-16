import os
import sys
import unittest
#import hashlib
from  unittest.mock import patch

from matplotlib.pyplot import imread
from hypothesis import given, strategies as st

sys.path.append(os.getcwd())

# from src.cifrar import Cifrador
# from src.descifrar import Descifrador

from src import main 
from src import utils 

# import main
# import utils

class TestMain(unittest.TestCase):
    """! Clase para checar que se mantienen los invariantes del programana
    en general."""
    
    @patch('builtins.input', lambda _: 'sinaloa')
    def test_cifrar_descifrar(self):
        """Encripta un archivo txt y una imagen y después los desencripta
        para ver si obtiene el mismo mensaje."""
        
        #Cifra un archivo de texto
        doc_evaluaciones = 'evaluaciones'
        evals = 8
        evals_min = 5
        contenido_archivo = 'Esto es una prueba\n para encriptar.'
        utils.escribir_archivo('prueba', 'txt', contenido_archivo)
        doc_claro = 'prueba.txt'
        main.cifrar(doc_evaluaciones, evals, evals_min, doc_claro)

        #Descifra el archivo de texto
        #Agrega excepcion para cuando el archivo no exista
        main.descifrar(doc_evaluaciones + '.frg', 'prueba.aes' )
        with open('se_logro') as file:
            contenido_obtenido = file.read()
        
        self.assertEqual(contenido_archivo, contenido_obtenido)

#        Cifra una imagen
        doc_evaluaciones = 'evaluaciones'
        evals = 8
        evals_min = 5
        doc_claro = 'taquitos.jpeg'
        main.cifrar(doc_evaluaciones, evals, evals_min, doc_claro)

#       Descifra la imagen
#       Agrega excepcion para cuando el archivo no exista
        main.descifrar(doc_evaluaciones + '.frg', 'taquitos.aes' )
        img_arr_obtenido = imread('se_logro')
        img_arr_original = imread('taquitos.jpeg')

        self.assertTrue( (img_arr_obtenido == img_arr_original).all() )


#    def test_ciphertext_alterado(self):
#        """Se da un ciphertext modificado"""


#Este test hazlo desde programa principal. Truena cuando las
#evaluaciones son menos de las requeridas entonces, el int no
#se puede transformar a bytes
#    @patch('builtins.input', lambda _: 'sinaloa')    
    # def test_key_incorrecta(self):
    #     c = Cifrador('hola bebe', 6,3)
    #     cripto, eval = c.cifrar()

    #     #Número insuficiente de evaluaciones
    #     d = Descifrador(eval[:2], 'encrypted.bin') <- aquí truena
    #     self.assertRaises((ValueError, OverflowError), d.descifra)

    #     #Evaluaciones suficientes pero incorrectas
    #     eval_incorrectas = [(x, y +5) for (x,y) in eval]
    #     d = Descifrador(eval_incorrectas, 'encrypted.bin')
    #     self.assertRaises((ValueError, OverflowError), d.descifra )


if __name__ == '__main__':
    unittest.main()
