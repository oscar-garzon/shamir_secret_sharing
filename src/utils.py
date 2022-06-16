from typing import List, Tuple

from excepciones import FragmentosFileError

Punto = Tuple[int, int]

def escribir_archivo(nombre: str, extencion: str, contenido: str) -> None :
    """ Escribe contenido y lo guarda en un archivo llamado f'{nombre}.{terminacion}'

    @param nombre el nombre con el que se va guardar el archivo
    @param extencion extencion con el que se va guardar el archivo
    @param contenido el contenido del archivo"""
    with open(f"{nombre}.{extencion}", 'w') as archivo:
        archivo.write(contenido)


def escribir_fragmentos(fragmentos :List[Tuple[int, int]], nombre_archivo :str) -> None:
    """Escribe nombre_archivo con un fragmento en cada linea"""
    
    l = len(fragmentos)
    line = ''
    with open(nombre_archivo, 'w') as output:
        for i,frag in enumerate(fragmentos):
            if i != l-1:
                line += f"({str(frag[0])}, {str(frag[1])})\n"
            else: 
                line += f"({str(frag[0])}, {str(frag[1])})"
        output.write(line)        


def fragmentos_a_lista(fragmentos: str) -> List[Punto]:
    """ Toma los fragmentos que vienen de doc_evaluaciones
    y regresa una lista con los puntos """

    puntos = []
    try:
        for fragmento in fragmentos.split('\n'):
            x, y = fragmento.split(',')
            x = int(x[1:])   
            y = int(y[:-1])
            puntos.append((x,y))
    except ValueError:
        raise FragmentosFileError() 
    
    return puntos


""" def list_to_str(l: List) -> str:
    s = ''
    for punto in l:
        s += f"({punto[0]}, {punto[1]})\n"
    return s """



