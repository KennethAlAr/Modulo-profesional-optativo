from colorama import Fore, Style

'''
Quiero crear una función imprimir que:
1. reciba el mensaje a imprimir
2. opcionalmente reciba un color para que imprima el mensaje de ese color
'''

def imprimir(mensaje, color = None):
    if color != None:
        mensaje = color + mensaje + Style.RESET_ALL
    print(mensaje)

def imprimir_con_marco(mensaje, color = None):
    '''
    ---------
    |  Hola |
    ---------
    '''
    frases = mensaje.split("\n")
    long_frase = [len(frase) for frase in frases]
    long_max = (max(long_frase)) + 4
    mensaje = ""
    for frase in frases:
        mensaje += "| " + frase + " "*int(long_max-(len(frase)+3)) + "|\n"
    barra = "-" * long_max
    imprimir(barra + "\n" + mensaje + barra, color)

def imprimir_con_marco_centrado(mensaje, color):
    frases = mensaje.split("\n")
    long_frase = [len(frase) for frase in frases]
    long_max = (max(long_frase)) + 4
    mensaje = ""
    for frase in frases:
        espacios = int(long_max -(len(frase)+2))
        mensaje += "|" + " "*(espacios//2) + frase + " "*(espacios - (espacios//2)) + "|\n"
    barra = "-" * long_max
    imprimir(barra + "\n" + mensaje + barra, color)
