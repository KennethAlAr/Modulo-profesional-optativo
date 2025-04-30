# Escribe un programa que pida al usuario dos números enteros positivos y encuentre el primer número primo entre ellos.
# Un número primo es un número mayor que 1 que solo es divisible por 1 y por sí mismo.
# El programa debe imprimir el primer número primo encontrado o un mensaje indicando que no se encontraron números primos en el rango.

primer_numero = int(input("Introduce un número entero positivo: "))
segundo_numero = int(input("Introduce otro número entero positivo:"))

numero_primo = 0

for i in range(primer_numero, segundo_numero+1):
    activador = False
    for j in range(2, i):
        if i % j == 0:
            activador = True
    if activador == False:
        numero_primo = i
        break

if numero_primo == 0:
    print(f"No hay ningún número primo entre {primer_numero} y {segundo_numero}.")
else:
    print(f"El primer número primo entre {primer_numero} y {segundo_numero} es: {numero_primo}")