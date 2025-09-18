frase = input("Introduce una frase:")

caracteres = len(frase)
lista = frase.split(" ")
numero_palabras = len(lista)

larga = ""

for palabra in lista:
    if len(palabra) > len(larga):
        larga = palabra

print(f"Tu frase tiene {caracteres} caracteres, {numero_palabras} palabras y la palabra mas larga es '{larga}'.")