# 📌Ejercicio 1 - Escribe un programa que pida al usuario un número entero y determine si es par o impar.
# El programa debe imprimir un mensaje indicando el resultado.

numero_par_impar = int(input("Introduce un número entero: "))

if numero_par_impar % 2 == 0:
    print(f"El número {numero_par_impar} es par.")
else:
    print(f"El número {numero_par_impar} es impar.")

# 📌Ejercicio 2 - Escribe un programa que pida al usuario un número entero y determine si es positivo, negativo o cero.
# El programa debe imprimir un mensaje indicando el resultado.

numero_positivo_negativo = int(input("Introduce un número entero: "))

if numero_positivo_negativo > 0:
    print(f"El número {numero_positivo_negativo} es positivo.")
elif numero_positivo_negativo < 0:
    print(f"El número {numero_positivo_negativo} es negativo.")
else:
    print(f"El número {numero_positivo_negativo} es cero.")

# 📌Ejercicio 3 - Escribe un programa que pida al usuario un número entero y determine si es divisible por 3 y 5.
# El programa debe imprimir un mensaje indicando el resultado.

numero_divisible_3_5 = int(input("Introduce un número entero:"))

if numero_divisible_3_5 % 5 == 0:
    if numero_divisible_3_5 % 3 == 0:
        print(f"El número {numero_divisible_3_5} es divisible entre 3 y entre 5.")
    else:
        print(f"El número {numero_divisible_3_5} es divisible entre 5.")
elif numero_divisible_3_5 % 3 == 0:
    print(f"El número {numero_divisible_3_5} es divisible entre 3.")
else:
    print(f"El número {numero_divisible_3_5} no es divisible ni entre 3 ni entre 5.")

# 📌Ejercicio 4 - Escribe un programa que pida una nota (0-10) y muestre:
# "Suspenso" si es menor de 5
# "Aprobado" si es entre 5 y 6
# "Notable" si es entre 7 y 8
# "Sobresaliente" si es 9 o 10

nota = float(input("Introduce tu nota del 1 al 10:"))

if nota < 5:
    print("Suspenso.")
elif nota >= 5 and nota < 7:
    print("Aprobado.")
elif nota >= 7 and nota < 9:
    print("Notable.")
else:
    print("Sobresaliente.")

# 📌Ejercicio 5 - Escribe un programa que pida el nombre de un día de la semana y muestre si es "laborable" o "fin de semana".

dias_laborables = ["lunes", "martes", "miércoles", "jueves", "viernes"]

dia_input = input("Introduce un día de la semana: ").lower()

if dia_input in dias_laborables:
    print(f"El {dia_input} es laborable.")
else:
    print(f"El {dia_input} es fin de semana.")

# 📌Ejercicio 6 - Escribe un programa que pida un año y muestra si es bisiesto. Un año es bisiesto si es divisible por 4,
# pero no por 100, o si es divisible por 400.

ano_input = int(input("Introduce un año: "))

if ano_input % 400 == 0:
    print(f"El año {ano_input} es bisiesto.")
elif ano_input % 4 == 0:
    if not ano_input % 100 == 0:
        print(f"El año {ano_input} es bisiesto.")
    else:
        print(f"El año {ano_input} no es bisiesto.")
else:
    print(f"El año {ano_input} no es bisiesto.")

# 📌Ejercicio 7 - Escribe un programa que pida dos números y un operador (+, -, *, /) y muestre el resultado de la operación.

numero_calculadora_1 = float(input("Introduce un número: "))
numero_calculadora_2 = float(input("Introduce otro número: "))
operador_calculadora = input("Introduce un operador (+, -, * ó /): ")

if operador_calculadora == "+":
    print(f"La suma entre {numero_calculadora_1} y {numero_calculadora_2} es: {numero_calculadora_1 + numero_calculadora_2}")
elif operador_calculadora == "-":
    print(f"La resta entre {numero_calculadora_1} y {numero_calculadora_2} es: {numero_calculadora_1 - numero_calculadora_2}")
elif operador_calculadora == "*":
    print(f"La multiplicación entre {numero_calculadora_1} y {numero_calculadora_2} es: {numero_calculadora_1 * numero_calculadora_2}")
elif operador_calculadora == "/":
    print(f"La división entre {numero_calculadora_1} y {numero_calculadora_2} es: {numero_calculadora_1 / numero_calculadora_2}")

# 📌Ejercicio 8 - Escribe un programa que pida el nombre de un mes y muestre cuántos días tiene (puedes simplificar febrero a 28 días siempre).

meses_31_dias = ["enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"]
meses_30_dias = ["abril", "junio", "septiembre", "noviembre"]

nombre_mes = input("Introduce el nombre de un mes: ").lower()

if nombre_mes in meses_31_dias:
    print(f"{nombre_mes.capitalize()} tiene 31 días.")
elif nombre_mes in meses_30_dias:
    print(f"{nombre_mes.capitalize()} tiene 30 dias.")
elif nombre_mes == "febrero":
    print(f"{nombre_mes.capitalize()} tiene 28 días.")

# 📌Ejercicio 9 - Escribe un programa que pida el precio de un producto y, si supera los 100 €,
# aplique un descuento del 10%. Muestra el precio final.

precio = float(input("Introduce el precio de tu producto: "))

if precio > 100:
    print(f"El precio final es de {precio * 0.9}. Aplicado un 10% de descuento.")
else:
    print(f"El precio final es de {precio}. No se ha aplicado ningún descuento.")

# 📌Ejercicio 10 - Escribe un programa que pida día, mes y año. Comprueba si la fecha introducida es válida.
# Recuerda que, en los años bisiestos, febrero tiene 29 días.
# Puedes usar el algoritmo del ejercicio 6 para determinar si un año es bisiesto.

fecha_dia = int(input("Introduce el día de la fecha que quieres introducir (1-31): "))
fecha_mes = int(input("Introduce el mes de la fecha que quieres introducir (1-12): "))
fecha_ano = int(input("Introduce el año de la fecha que quieres introducir (1-31): "))

mes_30_dias = [4, 6, 9, 11]
mes_31_dias = [1, 3, 5, 7, 8, 10, 12]

if (fecha_dia < 1 or fecha_dia > 31) or (fecha_mes < 1 or fecha_mes > 12):
    print("Fecha no válida.")
elif fecha_mes == 2 and ((fecha_ano % 4 == 0 and not fecha_ano % 100 == 0) or (fecha_ano % 400 == 0)):
    if fecha_dia <= 29:
        print("Fecha válida.")
    else:
        print("Fecha no válida.")
elif fecha_mes == 2 and (not fecha_ano % 4 == 0 or fecha_ano % 100 == 0):
    if fecha_dia <= 28:
        print("Fecha válida.")
    else:
        print("Fecha no válida.")
elif fecha_mes in mes_30_dias:
    if fecha_dia <= 30:
        print("Fecha válida.")
    else:
        print("Fecha no válida.")
elif fecha_mes in mes_31_dias:
    if fecha_dia <= 31:
        print("Fecha válida.")
    else:
        print("Fecha no válida.")

# 📌Ejercicio 11 - Escribe un programa que pida al usuario dos números enteros e imprima la secuencia de números entre
# ellos (incluidos) en orden ascendente. El primer número siempre será menor que el segundo.

primer_numero = int(input("Introduce un número entero: "))
segundo_numero = int(input("Introduce un número entero mayor que el anterior: "))

while primer_numero <= segundo_numero:
    print(primer_numero)
    primer_numero += 1

# 📌Ejercicio 12 - Escribe un programa que pida al usuario dos números enteros e imprima la secuencia de números entre
# ellos (incluidos) en orden ascendente. Si el primer número es mayor que el segundo, imprime la secuencia en orden descendente.
# Debes imprimir la secuencia de números en una sola línea, separados por espacios.

#Además, el argumento end=" " en la función print() se utiliza para imprimir los números en la misma línea, separados por espacios.
# Si no se especifica, print() por defecto añade un salto de línea al final de cada impresión. Por lo tanto,
# al usar end=" ", estamos indicando que queremos que el siguiente número se imprima en la misma línea, separado por un espacio.

numero_1 = int(input("Introduce un número entero: "))
numero_2 = int(input("Introduce otro número entero: "))

if numero_1 < numero_2:
    while numero_1 <= numero_2:
        print(numero_1, end=" ")
        numero_1 += 1
else:
    while numero_1 >= numero_2:
        print(numero_1, end = " ")
        numero_1 -= 1

# 📌Ejercicio 13 - Escribe un programa que pida al usuario un número entero positivo e imprima la tabla de multiplicar
# de ese número (del 1 al 10).

numero_tabla = int(input("Introduce un número entero positivo: "))

for i in range(1, 11):
    print(f"{numero_tabla} x {i} = {numero_tabla * i}")

# 📌Ejercicio 14 - Escribe un programa que pida al usuario un número entero positivo e imprima la suma de los números
# pares, por un lado, y la suma de los números impares por otro. El programa debe imprimir ambos resultados.

numero_sumas = int(input("Introduce un número entero positivo: "))

suma_pares = 0
suma_impares = 0

for i in range(1, numero_sumas+1):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i

print(f"La suma de todos los números pares entre 1 y {numero_sumas} es: {suma_pares}")
print(f"La suma de todos los números impares entre 1 y {numero_sumas} es: {suma_impares}")

# 📌Ejercicio 15 - Escribe un programa que pida al usuario un número entero positivo y calcules la suma de la potencia
# de 3 de cada número desde 1 hasta el número introducido. El programa debe imprimir el resultado.

numero_potencia = int(input("Introduce un número entero positivo: "))

suma_potencia = 0

for i in range(1, numero_potencia+1):
    suma_potencia += (i**3)

print(f"La suma de las potencias de tres de los números entre el 1 y el {numero_potencia} es: {suma_potencia}")

# 📌Ejercicio 16 - Escribe un programa que pida al usuario un número entero positivo e imprima la lista de divisores
# de ese número. Un divisor de un número 'n' es un número entero que divide a 'n' sin dejar residuo.
# El programa debe imprimir todos los divisores del número introducido.

numero_divisible = int(input("Introduce un número entero positivo: "))
lista_divisores = []
for i in range(1, numero_divisible+1):
    if numero_divisible % i == 0:
        lista_divisores.append(i)

print(f"{numero_divisible} es divisible entre los siguientes números: {lista_divisores}")

# 📌Ejercicio 17 - Escribe un programa que reciba un número entero positivo y una letra. El programa debe imprimir la
# letra tantas veces como el número introducido.

numero_letra = int(input("Introduce un número entero positivo: "))
letra = input("Introduce una letra: ")

print(numero_letra*letra)