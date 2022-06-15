"""! Punto de entrada del programa. Se realizan operaciones de alto nivel
para cifrar y descifrar"""

from typing import List, Tuple
import json

from cifrar import Cifrador
from utils import escribir_fragmentos


def cifrar(doc_evaluaciones: str, evals: int, evals_min: int, doc_claro: str) -> None:
    """! Guarda  doc_claro cifrado y el archivo donde están las
    evaluaciones del polinomio con el nombre {doc_evaluaciones}.

    @param doc_evaluaciones el nombre del archivo en el que seran guardas
    las n evaluaciones
    @param evals el número total de evaluaciones requeridas
    @param evals_min el número mínimo de puntos necesarios para descrifrar
    @param doc_claro el nombre del archivo con el documento claro"""

    if evals <= 2:
        print('Número total de evaluaciones requeridas debe ser mayor a 2')
    if evals_min < 1 or evals_min > evals:
        print('El número mínimo de puntos necesarios para descrifrar es 1 < t <= n')

    with open(doc_claro, 'rb') as archivo:
        doc_bytes = archivo.read()

    c = Cifrador(evals, evals_min)

    
    fragmentos = c.obtener_evaluaciones()
    resultado = c.cifrar(doc_claro)

    archivo_cifrado = doc_claro.split('.')[0] + '.aes'

    with open(archivo_cifrado, 'w') as output:
        json.dump(resultado, output, indent=6)

    escribir_fragmentos(fragmentos, doc_evaluaciones)


def descifrar(doc_evaluaciones: str, doc_cifrado: str) -> None:
    """! Guarda en disco el documento claro con su nombre original.

    @param doc_evaluaciones el nombre del documento con, al menos, t de las n evaluaciones requeridas.
    @param doc_cifrado el nombre del archivo cifrado."""
    return -1 

cifrar('prueba_evaluaciones', 10, 4, 'prueba.txt')
  


