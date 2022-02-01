from typing import List, Tuple

Punto = Tuple[int, int]

class Descifrador():
    def __init__(self, puntos: List[Punto], criptograma: bytes ):
        """! Constructor de la clase Descifrador.
        Cuando se llama al constructor se obtiene la llave par descifrar el
        criptograma.

        @param puntos una lista con los t puntos necesarios para reconstruir
        el polinomio.
        @param criptograma el documento a descifrar"""

        self.puntos = puntos
        self.criptograma = criptograma
        self.key = self._get_key().to_bytes(32, byteorder='big')




    def descifra(self) -> str:
        """! Devuelve el contenido descifrado del criptograma

        @return el contenido descifrado del criptograma"""

        file_in = open(self.criptograma, "rb")
        nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

        # let's assume that the key is somehow available again
        cipher = AES.new(self.key, AES.MODE_EAX, nonce)
        data = str(cipher.decrypt_and_verify(ciphertext, tag), 'utf-8')
        return data


    def _get_key(self) -> int:
        """! Regresa la key necesaria para descifrar el criptograma.

        @return la llave para descifrar criptograma."""
        result = 0
        for i in range(len(self.puntos)):
            result += self.puntos[i][1] * self._evalua_poli(i)
        result = result % 208351617316091241234326746312124448251235562226470491514186331217050270460481
        return result  


    def _evalua_poli(self, indx) -> int:
        """! Regresa el valor P_indx(0)

        @param indx el índice del polinomio a evaluar
        @return el valor de P_index evalueado en 0"""

        result = 1
        for i in range(len(self.puntos)):
            if i != indx:
                result *=  (-self.puntos[i][0] / (self.puntos[indx][0] - self.puntos[i][0]))
        return int(result)
