from .escritura import imprimir

'''
Funciones para leer diferentes tipos de datos con control de errores.

leer_entero()
-> hola
-> ValueError
'''

def leer_entero(mensaje, color):
    # Esto debería hacer un input, intentar castearlo a int, y devolver valor entero.
    # Si al intentar castear la entrada no es un número, capturar excepción y elevarla.
    try:
        imprimir(mensaje, color)
        entero = int(input())
    except:
        raise ValueError("Debes introducir un número entero.")
    return entero

def leer_string(mensaje, color = None):
    imprimir(mensaje, color)
    return input()

def leer_string_en_lista(mensaje, color = None):
    imprimir(mensaje, color)
    return input().split("")