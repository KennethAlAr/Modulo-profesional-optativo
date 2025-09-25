string = input("Escribe un texto:").split()

buscada = input("Escribe la palabra que quieres buscar: ")

for palabra in string:
    formato = ""
    for letra in palabra:
        if letra.isalpha():
            formato += letra
    palabra = formato

contador = 0

for palabra in string:
    if buscada == palabra:
        contador += 1

print(f"El texto tiene {contador} veces la palabra '{buscada}'")