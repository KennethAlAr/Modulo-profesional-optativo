# Ejercicio 1 - Sumar elementos de una lista
# Escribe un programa que pida al usuario una lista de números enteros separados por comas y calcule la suma de todos
# los elementos de la lista. El programa debe imprimir el resultado.

lista_input = input("Introduce una lista de números separados por comas: \n").split(",")

resultado = 0

for i in range(len(lista_input)):
    resultado += int(lista_input[i])

print(resultado)
resultado = 0

for numero in lista_input:
    resultado += int(numero)

print(resultado)

lista = [int(num) for num in lista_input]

print(lista)

# Ejercicio 2 - Contar elementos de una lista
# Escribe un programa que pida al usuario una lista de palabras separadas por comas y cuente cuántas palabras hay en la lista.
# El programa debe imprimir el resultado.

print("La longitud de la lista es: ", len(input("Introduce una lista de palabras separadas por comas: \n").split(",")))

lista_palabras = input("Introduce una lista de palabras separadas por comas: \n").split(",")
resultado = 0

for palabra in lista_palabras:
    resultado += 1

print(resultado)

# Ejercicio 3 - Mayor y menor elemento de una lista
# Escribe un programa que pida al usuario una lista de números enteros separados por comas y encuentre el mayor y el
# menor elemento de la lista. El programa debe imprimir ambos resultados.

lista_numeros = [int(num) for num  in (input("Introduce una lista de números separados por comas: \n").split(","))]

lista_numeros.sort()

print(f"El mayor es {lista_numeros[-1]} y el menor es {lista_numeros[0]}")

# Ejercicio 4 - Sumar dos listas de igual longitud¶
# Escribe un programa que pida al usuario dos listas de números enteros separados por comas y sume los elementos de ambas listas.
# El programa debe imprimir la lista resultante. Si las listas no tienen la misma longitud, el programa debe imprimir un mensaje de error.

lista1 = [int(num) for num  in (input("Introduce una lista de números separados por comas: \n").split(","))]
lista2 = [int(num) for num  in (input("Introduce otra lista de números separados por comas: \n").split(","))]
lista_suma = []

if len(lista1) == len(lista2):
    for i in range(len(lista1)):
        lista_suma.append(lista1[i] + lista2[i])
    print(lista_suma)
else:
    print("Las listas no tienen el mismo tamaño.")

# Ejercicio 5 - Invertir una lista
# Escribe un programa que pida al usuario una lista de números enteros separados por espacios y la invierta.
# El programa debe imprimir la lista invertida.

lista_enteros = [int(num) for num  in (input("Introduce una lista de números separados por espacios: \n").split(" "))]

lista_enteros.reverse()

print(lista_enteros)

# Ejercicio 6 - Dias de la semana¶
# Escribe un programa que reciba números enteros positivos hasta la introducción de un 0. Por cada número, suponiendo que el 1
# representa el lunes, el 2 el martes, etc., imprime el nombre del día correspondiente.
# Ejemplo:
# Ingrese un número (0 para salir): 1
# Lunes
# Ingrese un número (0 para salir): 3
# Miércoles
# Ingrese un número (0 para salir): 8
# Lunes
# Ingrese un número (0 para salir): 0

semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

while True:
    input_usuario = int(input("Introduce un número de día de la semana (0 para salir): \n"))
    if input_usuario == 0:
        print("Programa terminado")
        break
    print(semana[((input_usuario%7)-1)])