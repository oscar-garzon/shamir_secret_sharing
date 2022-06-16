# Shamir Secret Sharing

Este repositorio contiene el tercer proyecto para la clase de Modelado y Programación de la Fac. de Ciencias de la UNAM.


## Descripción

Se tiene que implementar Esquema de Secreto Compartido de Shamir. El cual hace posible que un sólo dato pueda ser ocultado de manera que, a partir de él, se generan n diferentes datos y que con, al menos t ≤ n cualesquiera de ellos sea posible recuperar el dato original.


### Documentación
Para ver la documentación del programa ejecutar en un navegador web el archivo html html/src/index.html

### Correr programa

Hay que posicionarse en la carpeta samir_secret_sharing

```
$ cd shamir_secret_sharing/
```

Para cifrar un archivo:

```
$ python src/main.py c [nombre archivo para guardar evaluaciones] [número de evaluaciones requeridas ] [número mínimo de puntos necesarios para descifrar] [nombre archivo con documento claro]
```

Para descifrar:

```
$ python src/main.py d [nombre de archivo con evaluaciones] [nombre del archivo cifrado]

```

### Correr todos los tests
```
$ python -m test
```