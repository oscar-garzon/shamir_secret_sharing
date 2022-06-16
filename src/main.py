"""! Punto de entrada del programa. Se realizan operaciones de alto nivel
para cifrar y descifrar"""

from typing import List, Tuple
import json
import os 
from sys import path, argv, exit


path.append(os.getcwd()+'/src')

from excepciones import FragmentosFileError  
from cifrar import Cifrador
from descifrar import Descifrador
from utils import escribir_fragmentos, fragmentos_a_lista
#from interfaz import correr 


def cifrar(doc_evaluaciones: str, evals: int, evals_min: int, doc_claro: str) -> None:
    """! Guarda  doc_claro cifrado y el archivo donde están las
    evaluaciones del polinomio con el nombre {doc_evaluaciones}.

    @param doc_evaluaciones el nombre del archivo en el que seran guardas
    las n evaluaciones
    @param evals el número total de evaluaciones requeridas
    @param evals_min el número mínimo de puntos necesarios para descrifrar
    @param doc_claro el nombre del archivo con el documento claro"""
    evals = int(evals)
    evals_min = int(evals_min)

    if evals <= 2:
        print('Número total de evaluaciones requeridas debe ser mayor a 2')
        exit()
    if evals_min <= 1 or evals_min > evals:
        print('El número mínimo de puntos necesarios para descrifrar es 1 < t <= n')
        exit()

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
    
    with open(doc_evaluaciones) as file:
        fragmentos = fragmentos_a_lista(file.read())

    with open(doc_cifrado) as file:
        b64 = json.load(file)
    
    d = Descifrador(fragmentos, b64)
    #doc_claro, header = d.descifra()  FALTA HACER QUE REGRESE HEADER
    doc_claro = d.descifra()

    with open('se_logro', 'wb') as file:
        file.write(doc_claro)


if __name__ == '__main__':
    def uso():
        print(
            ' \n Uso correcto:\n\n  Cifrar: python src/main.py c [nombre archivo para guardar evaluaciones] [número de evaluaciones requeridas ] [número mínimo de puntos necesarios para descifrar] [nombre archivo con documento claro]'
        )
        print(
            '  \n  Descifrar: python src/main.py d [nombre de archivo con evaluaciones] [nombre del archivo cifrado]'
        )
        exit()

    args_number = len(argv)

    if args_number != 6 and args_number != 4:
        uso()

    if argv[1] == "c":
        if args_number != 6:
            uso()       
        try:
            cifrar(argv[2], argv[3], argv[4], argv[5])
        except FileNotFoundError:
            print('Archivo no encontrado')
        
    elif argv[1] == "d":
        if args_number != 4:
            uso()
        try:
            descifrar(argv[2], argv[3])
        except FileNotFoundError:
            print('Archivo no encontrado')
        except (ValueError, KeyError):
            print('Problemas con la desencriptación')
        except FragmentosFileError:
            print("Archivo de fragmentos ha sido modificado. No se puede desencriptar el archivo")

