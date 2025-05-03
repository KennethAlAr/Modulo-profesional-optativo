# 📌Ejercicio 1 - CONTADOR - Escribe un programa que pida al usuario un número entero positivo e imprima los números desde el 0
# hasta ese número (incluido). El programa debe imprimir los números en cada iteración.

numero_contador = int(input("Ingresa un número entero positivo:\n"))

for i in range (numero_contador+1):
    print(i)

# 📌Ejercicio 2 - CONTADOR DE NÚMEROS PARES - Escribe un programa que pida al usuario un número entero positivo y
# cuente cuántos números pares hay desde 0 hasta ese número (incluido). El programa debe imprimir el resultado.

numero_contador_pares = int(input("Ingresa un número entero positivo:\n"))
contador = 0

for i in range (numero_contador_pares+1):
    if i%2 == 0:
        contador += 1

print(f"Entre 0 y {numero_contador_pares} hay {contador} números pares.")

# 📌Ejercicio 3 - CUENTA ATRÁS - Escribe un programa que pida al usuario un número entero positivo y realice una cuenta
# atrás desde ese número hasta 0. El programa debe imprimir cada número en la cuenta atrás.

numero_cuenta_atras = int(input("Introduce un número entero positivo:\n"))

for i in range(numero_cuenta_atras, -1, -1): #Hay que tener el cuenta que el primer valor siempre lo incluye y el segundo no.
    print(i)

# 📌Ejercicio 4 - FACTORIAL - Escribe un programa que pida al usuario un número entero positivo y calcule su factorial.
# El programa debe imprimir el resultado. El factorial de un número n se define como el producto de todos los números
# enteros desde 1 hasta n.

numero_factorial = int(input("Introduce un número entero positivo:\n"))
contador_factorial = 1

for i in range(1, numero_factorial+1):
    contador_factorial *= i

print(f"El factorial de {numero_factorial} es {contador_factorial}")

# 📌Ejercicio 5 - MÚLTIPLE DE 3 O 5 - Escribe un programa que pida al usuario un número entero positivo e imprima
# solamente los números múltiplos de 3 o de 5 dentro de ese rango.
# Si el número es múltiplo de 3, imprime el número seguido de el mensaje "es múltiplo de 3".
# Si el número es múltiplo de 5, imprime el número seguido del mensaje "es múltiplo de 5". Si el número es múltiplo de
# ambos no debes imprimir nada.

numero_multiplos = int(input("Ingresa un número entero positivo:\n"))

for i in range(numero_multiplos+1):
    if i%3 == 0 and i%5 == 0:
        continue
    elif i%5 == 0:
        print(f"{i} es múltiplo de 5")
    elif i % 3 == 0:
        print(f"{i} es múltiplo de 3")

# 📌Ejercicio 6 - TRIÁNGULO DE ASTERISCOS - Escribe un programa que pida al usuario un número entero positivo y dibuje
# un triángulo de asteriscos con la altura especificada.

numero_piramide = int(input("Ingresa un número entero positivo:\n"))

for i in range(1, numero_piramide+1):
    print("*" * i)

# 📌Ejercicio 7 - TABLA DE MULTIPLICAR - Escribe un programa que pida al usuario un número entero positivo y muestre
# la tabla de multiplicar de ese número.

numero_tabla = int(input("Ingresa un número entero positivo:\n"))

for i in range(1, 11):
    print(f"{i} x {numero_tabla} = {numero_tabla * i}")

# 📌Ejercicio 8 - CUADRADO CON CRUZ - Escribe un programa que pida al usuario un número entero positivo impar y
# dibuje un cuadrado de 'x' con una cruz en el medio.

numero_impar = int(input("Introduce un número entero positivo e impar:\n"))

for i in range(numero_impar):
    for j in range(numero_impar):
        if i == 0 or i == numero_impar-1:
            print("x" * numero_impar, end="")
            break
        if j == 0 or j == numero_impar-1 or j == i or j == numero_impar-i-1:
            print("x", end="")
        else:
            print(" ", end="")
    print()