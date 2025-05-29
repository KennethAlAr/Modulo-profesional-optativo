# Ejercicio 1 - Capitales y países
# Escribe un programa que almacene en un diccionario las capitales de varios países, se introducirán los datos con la
# forma PAIS-CAPITAL. Esto debe ejecutarse indefinidamente hasta que el usuario introduzca "FIN INSERCIONES".
# El programa debe permitir al usuario consultar la capital de un país introduciendo su nombre. Si el país no está en el
# diccionario, el programa debe informar al usuario.

paises = {}

entrada = input("Indica un valor de la forma 'País-Capital' o escribe FIN INSERCIONES para finalizar\n").lower()

while entrada != "FIN INSERCIONES".lower():
    pais = entrada.split("-")[0]
    capital = entrada.split("-")[1]

    paises[pais] = capital

    entrada = input("Indica un valor de la forma 'País-Capital' o escribe FIN INSERCIONES para finalizar\n").lower()

input_pais = input("Introduce el nombre del país que quieres consultar.\n").lower()

if input_pais in paises:
    print(f"La capital de {input_pais.capitalize()} es {paises[input_pais].capitalize()}.")
else:
    print(f"Ese país no está en la lista.")

print()

# Ejercicio 2 - Contar palabras en un texto
# Escribe un programa que pida al usuario un texto y cuente cuántas veces aparece cada palabra en el texto.
# El programa debe imprimir un diccionario donde las claves son las palabras y los valores son sus respectivas frecuencias.
# Ignora la puntuación y considera las palabras en minúsculas.

palabras = {}
texto = input("Introduce un texto:\n").lower().split()

for palabra in texto:
    if palabra in palabras:
        palabras[palabra] += 1
    else:
        palabras[palabra] = 1

for palabra in palabras:
    print(f"{palabra}:{palabras[palabra]}")

print()

# Ejercicio 3 - Inventario de productos
# Escribe un programa que gestione un inventario de productos utilizando un diccionario.
# El programa debe permitir al usuario añadir productos con su nombre y cantidad, eliminar productos, y consultar la
# cantidad de un producto específico. El programa debe ejecutarse indefinidamente hasta que el usuario introduzca "SALIR".

inventario = {}
opcion = -1

while opcion != 4:
    print("Escoge una opción:")
    print("1. Añadir producto.")
    print("2. Eliminar producto.")
    print("3. Consultar producto.")
    print("4. Salir.")

    opcion = int(input("Introduce una opción:\n"))

    if opcion == 1:
        nombre = input("Introduce el nombre del producto:\n")
        cantidad = int(input("Introduce la cantidad del producto:\n"))
        inventario[nombre] = cantidad
    elif opcion == 2:
        nombre = input("Introduce el producto a eliminar:\n")
        if nombre in inventario:
            del inventario[nombre]
            print(f"Producto {nombre} eliminado del inventario.")
        else:
            print(f"No existe el producto {nombre} en el inventario.")
    elif opcion == 3:
        nombre = input("Introduce el producto a consultar.")
        if nombre in inventario:
            print(f"El producto {nombre} tiene una cantidad de {inventario[nombre]} unidades.")
        else:
            print(f"No existe el producto {nombre} en el inventario.")
    elif opcion > 4 or opcion < 1:
        print(f"La opción {opcion} no existe en la lista de comandos.")

print("Saliendo...")

print()

# Ejercicio 4 - Tupla de números
# Escribe un programa que pida al usuario una lista de números enteros separados por comas y almacene estos números en una tupla.
# Luego, el programa debe calcular y mostrar la suma, el promedio, el número máximo y el número mínimo de la tupla.

numeros = input("Introduce una lista de números separados por comas").split(",")
numeros = [int(num) for num in numeros]

tupla = tuple(numeros)

suma = 0
promedio = 0.0
maximo = float('-inf')
minimo = float('inf')

for numero in numeros:
    suma += numero
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero

promedio = suma / len(tupla)

print(f"Suma: {suma}")
print(f"Promedio: {promedio}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")