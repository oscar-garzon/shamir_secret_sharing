from typing import List

def escribir_archivo(nombre: str, extencion: str, contenido: str) -> None :
    """! Escribe contenido y lo guarda en un archivo llamado f'{nombre}.{terminacion}'

    @param nombre el nombre con el que se va guardar el archivo
    @param extencion extencion con el que se va guardar el archivo
    @param contenido el contenido del archivo"""
    with open(f"{nombre}.{extencion}", 'w') as archivo:
        archivo.write(contenido)

def list_to_str(l: List) -> str:
    s = ''
    for punto in l:
        s += f"({punto[0]}, {punto[1]})\n"
    return s


def horner(self, x: int, coefs: List[int]) -> int:
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
