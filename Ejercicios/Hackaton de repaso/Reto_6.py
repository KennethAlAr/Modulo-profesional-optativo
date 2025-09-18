censura = ["tonto", "feo"]

frase = input("Introduce una frase para analizar:")

lista = frase.split(" ")
lista_censurada = []
for palabra in lista:
    if palabra in censura:
        palabra = "*"*(len(palabra))
    lista_censurada.append(palabra)

frase_censurada = " ".join(lista_censurada)

print(frase_censurada)

