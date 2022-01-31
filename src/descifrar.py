from typing import List, Tuple

Punto = Tuple[int, int]

class Descifrador():
    def __init__(self, t_puntos: List[Punto], criptograma: str ):
        """! Constructor de la clase Descifrador.
        Cuando se llama al constructor se obtiene la llave par descifrar el
        criptograma.

        @param t_puntos una lista con los t puntos necesarios para reconstruir
        el polinomio.
        @param criptograma el documento a descifrar"""

        self.t_puntos = t_puntos
        self.criptograma = criptograma
        #self.key = self._get_key()



    def descifra(self) -> str:
        """! Devuelve el contenido descifrado del criptograma

        @return el contenido descifrado del criptograma"""


    def _get_key(self) -> int:
        """! Regresa la key necesaria para descifrar el criptograma.

        @return la llave para descifrar criptograma."""

        result = 0
        for i in range(len(self.t_puntos)):
            p_de_x = self.t_puntos[i][1]
            poli = self._evalua_poli(i)
            result += p_de_x * poli
            print(p_de_x, poli, result)
        return result


    def _evalua_poli(self, indx) -> int:
        """! Regresa el valor P_indx(0)

        @param indx el índice del polinomio a evaluar
        @return el valor de P_index evalueado en 0"""

        result = 1
        for i in range(len(self.t_puntos)):
            if i != indx:
                result *=  (-self.t_puntos[i][0] / (self.t_puntos[indx][0] - self.t_puntos[i][0]))
        return int(result)
