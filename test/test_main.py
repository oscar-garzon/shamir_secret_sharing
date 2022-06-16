import os
import sys
import unittest
from unittest.mock import patch

from matplotlib.pyplot import imread
from hypothesis import given, strategies as st

sys.path.append(os.getcwd())

from src import main
from src import utils


class Tests(unittest.TestCase):
    """! Clase para checar que se mantienen los invariantes del programana
    en general."""

    @patch("builtins.input", lambda _: "sinaloa")
    def test_cifrar_descifrar(self):
        """Encripta un archivo txt y una imagen y después los desencripta
        para ver si obtiene el mismo mensaje."""

        # Cifra un archivo de texto
        doc_evaluaciones = "evaluaciones.frg"
        evals = 8
        evals_min = 5
        contenido_archivo = "Esto es una prueba\n para encriptar."
        utils.escribir_archivo("prueba", "txt", contenido_archivo)
        doc_claro = "prueba.txt"
        main.cifrar(doc_evaluaciones, evals, evals_min, doc_claro)

        # Descifra el archivo de texto
        main.descifrar(doc_evaluaciones, "prueba.aes")
        with open(doc_claro) as file:
            contenido_obtenido = file.read()

        self.assertEqual(contenido_archivo, contenido_obtenido)

        # Cifra una imagen
        doc_evaluaciones = "evaluaciones.frg"
        evals = 8
        evals_min = 5
        doc_claro = "taquitos.jpeg"
        main.cifrar(doc_evaluaciones, evals, evals_min, doc_claro)
        img_arr_original = imread("taquitos.jpeg")

        # Descifra la imagen
        main.descifrar(doc_evaluaciones, "taquitos.aes")
        img_arr_obtenido = imread(doc_claro)

        self.assertTrue((img_arr_obtenido == img_arr_original).all())

    def correr_tests():
        unittest.main()


if __name__ == "__main__":
    unittest.main()
