"""Modulo que contiene a la clase Descifrador. La cual desencripta un archivo 
encriptado."""

from typing import List, Tuple
from Crypto.Cipher import AES
from base64 import b64decode

Punto = Tuple[int, int]


class Descifrador:
    def __init__(self, puntos: List[Punto], b64: str):
        """Constructor de la clase Descifrador.
        Cuando se llama al constructor se obtiene la llave para descifrar el
        criptograma."""

        self.puntos = puntos
        self.b64 = b64
        self.key = self._get_key().to_bytes(32, byteorder="big")

    def descifra(self) -> Tuple[bytes, bytes]:
        """Devuelve el doc_claro en bytes y el nombre del documento claro

        Lanza ValueError y KeyError si ocurren problemas
        """

        json_k = ["nonce", "header", "ciphertext", "tag"]
        jv = {k: b64decode(self.b64[k]) for k in json_k}

        cipher = AES.new(self.key, AES.MODE_GCM, nonce=jv["nonce"])
        cipher.update(jv["header"])
        plaintext = cipher.decrypt_and_verify(jv["ciphertext"], jv["tag"])
        nombre = self.b64["nombre"]
        return plaintext, nombre

    def _get_key(self) -> int:
        """Regresa la key necesaria para descifrar el criptograma."""
        result = 0
        for i in range(len(self.puntos)):
            result += self.puntos[i][1] * self._evalua_poli(i)
        result = (
            result
            % 208351617316091241234326746312124448251235562226470491514186331217050270460481
        )
        return result

    def _evalua_poli(self, indx) -> int:
        """Regresa el valor P_indx(0)"""

        result = 1
        for i in range(len(self.puntos)):
            if i != indx:
                result *= -self.puntos[i][0] / (
                    self.puntos[indx][0] - self.puntos[i][0]
                )
        return int(result)
