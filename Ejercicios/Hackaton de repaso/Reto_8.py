frase = input("Introduce una frase:")

lista_frase = frase.split(" ")

numero_palabras = len(lista_frase)

primera = lista_frase[0]

ultima = lista_frase[-1]

print(f"Numero de palabras: {numero_palabras} - Primera palabra: '{primera}' - Última palabra: '{ultima}'")