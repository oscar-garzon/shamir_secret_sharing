"""! Punto de entrada del programa. Se realizan operaciones de alto nivel
para cifrar y descifrar"""

from typing import List

from cifrar import Cifrador
from utils import escribir_archivo, list_to_str


def cifrar(doc_evaluaciones: str, evals: int, evals_min: int, doc_claro: str) -> None:
    """! Guarda el criptograma de doc_claro y el archivo donde están las
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

    #Leo el documento claro
    with open(f"{doc_claro}") as archivo:
        texto = archivo.read()

    #Cifro el documento
    c = Cifrador(texto, evals, evals_min)
    criptograma, evaluaciones = c.cifrar()

    
    # Escribo el criptograma
    escribir_archivo(doc_evaluaciones, 'aes', criptograma)

    #Escribo las evaluaciones
    escribir_archivo(doc_evaluaciones, 'frg', list_to_string(evaluaciones))


def descifrar(doc_evaluaciones: str, doc_cifrado: str) -> None:
    """! Guarda en disco el documento claro con su nombre original.

    @param doc_evaluaciones el nombre del documento con, al menos, t de las n evaluaciones requeridas.
    @param doc_cifrado el nombre del archivo cifrado."""

    


