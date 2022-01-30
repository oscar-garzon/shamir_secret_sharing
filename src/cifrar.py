"""Clase para cifrar un documento dado. Se utiliza el estandar
de cifrado AES. Y la función hash SHA-256 para generar una
contraseña segura"""

import hashlib
from typing import Tuple, List
from random import randint

from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad


class Cifrador():

    Punto = Tuple[int, int]

    #tal vez haga un getter setter para el documento

    def __init__(self, doc_claro: str, evals: int, evals_min: int ):
        """! Construye un cifrador con todas sus propiedades.
        Pide al usuario generar una contraseña. A esta contraseña
        se le aplica SHA-256 y esta se guarda  en self.key

        @param doc_claro El documento claro que se va a cifrar.
        @param evals el número total de evaluaciones que se van a crear.
        @param evals_min el número mínimo de evaluaciones requeridas para
        descifrar el documento
        @throws Exception si evals < evals_min"""

        if evals < evals_min:
            raise Exception 

        self.evals = evals
        self.evals_min = evals_min
        contra = input("Escriba una contraseña para generar encriptación: ")
        self.key = hashlib.sha256(bytes(contra, 'utf8')).digest()
        self.doc_claro = doc_claro 


    def cifrar(self) -> Tuple[bytes, List[Punto]]:
        """! Cifra self.doc usando self.key y construye un polinomio de
        grado self.evals_min - 1 con self.key como término independiente

        @return una tupla con el criptograma y las evaluaciones del polinomio"""

        return (self._cifra_aes(), self._obtener_evaluaciones())


    def _obtener_evaluaciones(self) -> List[Punto]:
        """! Regresa las n evaluaciones(puntos) del polinomio

        @return una lista con las n evaluaciones(puntos) """

        p = 208351617316091241234326746312124448251235562226470491514186331217050270460481
        coefs = [randint(1,p) for i in range(self.evals_min - 1)]
        coefs = [int.from_bytes(self.key)] + coefs 
        return [(i, self._horner(i, coefs) % p) for i in range(1, self.evals + 1)]


    def _horner(self, x: int, coefs: List[int]) -> int:
        """! Implementación del algoritmo  de horner.
        Regresa el valor del polinomio evaluado en x.
        El polinomio es el formado por los valores de coefs.
        El índice del arreglo corresponde con la potencia de la variable
        independiente. Es decir, el término independiente va en coefs[0]

        @param x el número a evaluar en el polinomio
        @param coefs el valor de los coeficientes del polinomio

        @return valor del polinomio evaluado en x"""

        result = 0
        for i in range(self.evals_min - 1, -1, -1):
            result = (result * x) + coefs[i]
        return result


    def _cifra_aes(self) -> bytes:
        """! Regresa una string con el criptograma. Se encripta
        usando el mecanismo de cifrado simétrico AES.

        @return el criptograma"""
        cipher = AES.new(self.key, AES.MODE_CBC)
        return cipher.encrypt(pad(bytes(self.doc_claro, 'utf8'), AES.block_size))


        
