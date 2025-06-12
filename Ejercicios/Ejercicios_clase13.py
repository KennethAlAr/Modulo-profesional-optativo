# Ejercicio 1 - Calcular el área de un círculo
# Escribe un programa que pida al usuario el radio de un círculo y calcule su área.
# El programa debe definir una función que reciba el valor del radio, realice el cálculo del área y luego imprima el resultado.

import math

def calcular_area(radio):
    area = math.pi * (radio**2)
    print(f"El área del círculo con radio {radio}ud es de {area:.2f} ud²")

input_radio = int(input("Introduce el radio de un círculo para calcular su área:\n"))

calcular_area(input_radio)

# Ejercicio 2 - Configura un mensaje de bienvenida
# Escribe un programa que pida al usuario un nombre, un apellido y una edad.
# El programa debe definir una función que reciba estos datos y luego imprima un mensaje de bienvenida personalizado.

def saludar(nombre, apellido, edad):
    print(f"¡Hola {nombre} {apellido}! Tienes {edad} años.")

input_nombre = input("Introduce tu nombre:\n")
input_apellido = input("Introduce tu apellido:\n")
input_edad = input("Introduce tu edad:\n")

saludar(input_nombre, input_apellido, input_edad)

# Ejercicio 3 - Calcular el factorial de un número
# Escribe un programa que pida al usuario un número entero y calcule su factorial.
# El programa debe definir una función que reciba el número, realice el cálculo del factorial y luego imprima el resultado.

def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero+1):
        factorial *= i
    return factorial

input_numero = int(input("Introduce un número entero para calcular su factorial:\n"))

resultado = calcular_factorial(input_numero)

print(f"El factorial de {input_numero} es {resultado}.")

# Ejercicio 4 - Verificar si un número es primo
# Escribe un programa que pida al usuario un número entero y verifique si es primo.
# El programa debe definir una función que reciba el número, realice la verificación y luego imprima si el número es primo o no.

def es_primo(numero):
    booleano = True
    for i in range(2, numero):
        if numero%i == 0:
            booleano = False
    return booleano

def cuantos_primos(numero):
    resultado = 0
    for i in range(2, numero+1):
        if es_primo(i):
            resultado += 1
    return resultado

input_primo = int(input("Introduce un número entero para ver si es un número primo:\n"))

resultado = print(f"¿El número {input_primo} es primo? {es_primo(input_primo)}.")

numero_primos = print(f"Entre 1 y {input_primo} hay {cuantos_primos(input_primo)} números primos.")

# Ejercicio 5 - Calcular la suma de dígitos de un número
# Escribe un programa que pida al usuario un número entero y calcule la suma de sus dígitos.
# El programa debe definir una función que reciba el número, realice el cálculo de la suma de los dígitos y luego imprima el resultado.

def suma_digitos(numero):
    resultado = 0
    while numero > 0:
        resultado += numero%10
        numero //= 10
    return resultado

input_digito = int(input("Introduce un número entero para saber la suma de sus dígitos:\n"))

print(f"La suma de los dígitos del número {input_digito} es {suma_digitos(input_digito)}")

# Ejercicio 6 - Convierte string
# Recibe un string y lo convierte a mayúscular

def convierte_string(frase):
    return frase.upper()

frase = input("Introduce una frase que quieras capitalizar.\n")
print(convierte_string(frase))

# Ejercicio 7 - Incrementar cada elemento de una lista
# Escribe un programa que pida al usuario una lista de números enteros separados por comas y un número entero.
# El programa debe definir una función que reciba la lista y el número, incremente cada elemento de la lista por el
# número dado y luego imprima la lista resultante.

def incrementa_lista(lista, numero): #Hay que tener en cuenta que al introducir un valor primitivo a una función, esta hace
    #una copia del mismo y no modifica el original. Contrariamente, si el valor no es primitivo no crea copia y lo modifica.
    lista_modificada = lista
    for i in range(len(lista_modificada)):
        lista_modificada[i] += numero
    return lista_modificada

lista_raw = input("Introduce una lista de números separados por una coma:\n").split(",")
lista = [int(num) for num in lista_raw]
input_numero_suma = int(input("Introduce un número entero:\n"))

print(incrementa_lista(lista, input_numero_suma))