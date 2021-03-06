"""Modulo que contiene a la clase Cifrador. 
La cual encripta un archivo encriptado."""

import hashlib
from typing import Dict, Tuple, List
from random import randint
from base64 import b64encode
from getpass import getpass

from Crypto.Cipher import AES


class Cifrador:

    Punto = Tuple[int, int]

    def __init__(self, evals: int, evals_min: int):
        """Construye un cifrador con todas sus propiedades.
        Pide al usuario generar una contraseña. A esta contraseña
        se le aplica SHA-256 y esta se guarda  en self.key"""

        if evals < evals_min:
            raise Exception

        self.evals = evals
        self.evals_min = evals_min
        contra = getpass("Escriba una contraseña para generar encriptación: ")
        self.key = hashlib.sha256(bytes(contra, "utf8")).digest()
        self.cipher = AES.new(self.key, AES.MODE_GCM)

    def cifrar(self, doc_claro: str) -> Dict:
        """Regresa un diccionario con cipher.nonce, header,
        ciphertext, tag y el nombre original del documento claro"""

        with open(doc_claro, "rb") as doc:
            doc_bytes = doc.read()

        header = bytes(doc_claro, "utf-8")
        data = doc_bytes
        self.cipher.update(header)
        ciphertext, tag = self.cipher.encrypt_and_digest(data)

        json_k = ["nonce", "header", "ciphertext", "tag"]
        json_v = [
            b64encode(x).decode("utf-8")
            for x in [self.cipher.nonce, header, ciphertext, tag]
        ]
        result = dict(zip(json_k, json_v))
        result["nombre"] = doc_claro
        return result

    def obtener_evaluaciones(self) -> List[Punto]:
        """Regresa las n evaluaciones(puntos) del polinomio"""

        p = 208351617316091241234326746312124448251235562226470491514186331217050270460481
        coefs = [randint(1, p) for i in range(self.evals_min - 1)]
        coefs = [int.from_bytes(self.key, byteorder="big")] + coefs

        evals = [(i, self._horner(i, coefs) % p) for i in range(1, self.evals + 1)]
        return evals

    def _horner(self, x: int, coefs: List[int]) -> int:
        """Implementación del algoritmo  de horner.
        Regresa el valor del polinomio evaluado en x.
        El polinomio es el formado por los valores de coefs.
        El índice del arreglo corresponde con la potencia de la variable
        independiente. Es decir, el término independiente va en coefs[0]"""

        result = 0
        for i in range(self.evals_min - 1, -1, -1):
            result = (result * x) + coefs[i]
        return result
