import random

# 📌Ejercicio 9 - SUMA ACUMULATIVA
# Escribe un programa que pida al usuario una serie de números enteros y calcule la suma acumulativa de esos números.
# El programa debe seguir pidiendo números hasta que el usuario ingrese un 0. Al final, imprime la suma total.

print("Introduce números para sumarlos y para acabar introduce 0: \n")

numero = int(input())
resultado = 0

while numero != 0:
    resultado += numero
    numero = int(input())

print(f"El resultado es {resultado}")

# 📌Ejercicio 10 - AKINATOR NUMÉRICO
# Escribe un programa que escoja un número aleatorio entre 1 y 100 y le pida al usuario que adivine el número.
# El programa debe dar pistas al usuario si el número es mayor o menor que el número elegido.
# El programa debe seguir pidiendo números hasta que el usuario adivine el número correcto.

numero_aleatorio = random.randint(1,100)

numero_input = int(input("Introduce un número del 1 al 100:\n"))

while numero_input != numero_aleatorio:
    if numero_input > numero_aleatorio:
        print("Número incorrecto, el número secreto es mas bajo.")
    else:
        print("Número incorrecto , el número secreto es mas alto.")
    numero_input = int(input("Introduce un número del 1 al 100:\n"))

print(f"¡Correcto! El número secreto es {numero_aleatorio}. 👌")

# 📌Ejercicio 11 - MEDIA DE NOTAS
# Escribe un programa que pida al usuario cuantas evaluaciones hay que calificar.
# Seguidamente se recibirán ese número de series de notas (números decimales entre 0 y 10) y calcule la media de esas notas.
# El programa debe seguir pidiendo notas hasta que el usuario ingrese un -1. Al final, imprime la media.

numero_evaluaciones = int(input("Introduce el número de evaluaciones"))

for i in range(numero_evaluaciones):
    print(f"Introduce las notas de la evaluación número {i+1} e introduce -1 para terminar")
    nota = float(input())
    numero_notas = 0
    suma_notas = 0
    while nota != -1:
        suma_notas += nota
        numero_notas += 1
        nota = float(input())
    print(f"La media de notas de la evaluación número {i+1} es {suma_notas / numero_notas}")

# 📌Ejercicio 12 - MAYOR Y MENOR
# Escribe un programa que pida al usuario una serie de números enteros y determine cuál es el mayor y cuál es el menor.
# El programa debe seguir pidiendo números hasta que el usuario ingrese un 0. Al final, imprime el mayor y el menor.

mayor = float('-inf')
menor = float('inf')

numero_usuario = int(input("Introduce un valor (0 para terminar)"))

while numero_usuario != 0:
    if numero_usuario > mayor:
        mayor = numero_usuario
    if numero_usuario < menor:
        menor = numero_usuario

    numero_usuario = int(input())

print(f"Mayor: {mayor}, Menor: {menor}")

# 📌Ejercicio 13 - NÚMERO DE CIFRAS
# Escribe un programa que pida al usuario una serie de números enteros positivos hasta la introducción de un valor -1
# para cada número debe contar cuántas cifras tiene. El programa debe imprimir la longitud de cada número.
# No podéis usar la función len() para contar las cifras ni convertir el número a cadena.

numero_input = int(input("Introduce un número positivo (-1 para acabar): \n"))

while numero_input != -1:
    cifras = 1
    copia_numero = numero_input
    while copia_numero > 9:
        cifras += 1
        copia_numero //= 10
    print(f"El número de dígitos de {numero_input} es {cifras}.\n")
    numero_input = int(input("Introduce un número positivo (-1 para acabar): \n"))

# 📌Ejercicio 14 - NÚMERO DE CIFRAS
# Escribe un programa que pida al usuario un número entero positivo y determine si es primo o no.
# Un número primo es aquel que solo es divisible por 1 y por sí mismo. El programa debe imprimir el resultado.

numero_primo = int(input("Introduce un número entero positivo:\n"))

es_primo = 0

for i in range(2,numero_primo):
    if numero_primo%i == 0:
        es_primo += 1

if es_primo > 0:
    print(f"El número {numero_primo} no es primo.")
else:
    print(f"El número {numero_primo} es primo.")

# 📌Ejercicio 15 - BANCA ONLINE
# Escribe un programa que simule una cuenta bancaria.
# El programa debe permitir al usuario realizar las siguientes operaciones:
# 1. Ingresar dinero
# 2. Retirar dinero
# 3. Consultar saldo
# 4. Salir
# Inicializa el saldo en 0 y permite al usuario realizar operaciones hasta que decida salir.

saldo = 0

opcion = -1

while opcion != 4:
    print("Escoge una opción:")
    print("1. Ingresar dinero.")
    print("2. Retirar dinero.")
    print("3. Consultar saldo.")
    print("4. Salir.")

    opcion = int(input())

    if opcion == 1:
        saldo += int(input("¿Qué cantidad deseas ingresar?"))
    elif opcion == 2:
        saldo -= int(input("¿Qué cantidad deseas ingresar?"))
    elif opcion == 3:
        print(f"Tu saldo es: {saldo}€")
    else:
        print("Escoge una opción de la 1 a la 4.")

# 📌Ejercicio 16 - NÚMEROS PERFECTOS
# Escribe un programa que pida al usuario un número entero positivo y determine si es un número perfecto o no.
# Un número perfecto es aquel que es igual a la suma de sus divisores propios (excluyendo el propio número).
# Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 1 + 2 + 3 = 6.

numero_perfecto = int(input("Introduce un número entero positivo:\n"))
lista_divisores = []

for i in range(1,numero_perfecto):
    if numero_perfecto%i == 0:
        lista_divisores.append(i)

if sum(lista_divisores) == numero_perfecto:
    print(f"El número {numero_perfecto} es un número perfecto.")
else:
    print(f"El número {numero_perfecto} no es un número perfecto.")

# 📌Ejercicio 17 - CONVERSACIÓN BINARIA
# Escribe un programa que pida al usuario un número entero positivo y lo convierta a su representación binaria.
# El programa debe imprimir el resultado en forma de cadena de caracteres.

numero_decimal = int(input("Introduce un número entero positivo:\n"))

numero_division = numero_decimal
lista_binaria = []

while numero_division >= 2:
    lista_binaria.append(numero_division%2)
    numero_division //= 2

if numero_division == 1:
    lista_binaria.append(1)

lista_binaria.reverse()

resultado = "".join(str(i) for i in lista_binaria)

print(f"El número decimal {numero_decimal} en binario es {resultado}")