lista_raw = input("Introduce una lista de palabras separadas por comas:")

lista = lista_raw.split(",")

lista_sin_duplicados = set(lista)

lista_ordenada = sorted(lista_sin_duplicados)

print(lista_ordenada)