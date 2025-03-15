# 📌 EJERCICIOS CLASE 3

import random
import math

# 1️⃣ Generador de nombres de usuario
#     Pide al usuario su nombre y apellido.
#     Genera un nombre de usuario en minúsculas, sin espacios.
#     Añade un número aleatorio al final.
#     Muestra el nombre de usuario generado.

print("📌 EJERCICIO 1\n")
nombre_apellido = input("Escribe tu nombre y tu primer apellido:")
lista_strings = nombre_apellido.split(" ")
nombre = lista_strings[0].lower()
apellido = lista_strings[1].lower()
numero_random = str(random.randint(1,100))
usuario = nombre + apellido + numero_random
print(f"Tu nombre de usuario es: {usuario}")
print()

# 2️⃣ Analizador de frases
#     Pide al usuario que ingrese una frase.
#     Muestra la cantidad de caracteres de la frase.
#     Indica si la frase contiene la palabra "Python".
#     Convierte la frase a mayúsculas.
#     Muestra la frase invertida.

print("📌 EJERCICIO 2\n")
input_frase = input("Escribe la frase que quieras:")
print(f"Tu frase consta de {len(input_frase)} carácteres.")
if "Python" in input_frase:
    print("¡Tu frase contiene la palabra Python!")
else:
    print("Tu frase no contiene la palabra Python...")
frase_mayusculas = input_frase.upper()
frase_invertida = frase_mayusculas[::-1]
print(frase_invertida)

print()

# 3️⃣ Cálculo de descuentos
#     Pide al usuario el precio de un producto.
#     Aplica un 15% de descuento.
#     Muestra el precio final con dos decimales.
#     Muestra el precio redondeado hacia arriba.

print("📌 EJERCICIO 3\n")
input_precio = input("¿Qué precio tiene tu producto?")
precio_descuento = float(input_precio) * 0.85
print("El precio de tu producto con el 15% de descuento aplicado es de: {:.2f}".format(precio_descuento))
print(f"Si me das {math.ceil(precio_descuento)}€ te doy el cambio.")
print()

# 4️⃣ Generador de etiquetas de productos
#     Pide el nombre de un producto y su precio.
#     Convierte el nombre del producto a mayúsculas.
#     Muestra el precio con dos decimales.
#     Genera un código basado en el valor ASCII de la primera letra del producto.

print("📌 EJERCICIO 4\n")
input_producto = input("¿Cuál es tu producto?")
input_precio_producto = float(input("¿Cuál es su precio?"))
nombre_producto = input_producto.upper()
precio_producto = round(input_precio_producto, 2)
codigo_producto = ord(nombre_producto[0])
print(f"Tu producto es: {nombre_producto}")
print(f"El precio de tu producto es: {precio_producto}€")
print(f"El código encriptado de tu producto es: {codigo_producto}")
print()

# 5️⃣ Conversión de tipos y manipulación de listas
#     Pide al usuario una lista de números separados por comas.
#     Convierte cada número a entero.
#     Elimina los números repetidos.
#     Muestra la lista ordenada sin duplicados.

print("📌 EJERCICIO 5\n")
input_lista = input("Escribe una lista de números separados por coma:")
lista = input_lista.split(",")
lista_numeros = list(map(int, lista))
lista_sin_duplicados = set(lista_numeros)
print (sorted(lista_sin_duplicados))
print()

# 6️⃣ Creación de mensajes personalizados
#     Pide al usuario su nombre, edad y ciudad.
#     Muestra un mensaje con toda la información.
#     Si la edad es menor de 18, redondea hacia arriba hasta la mayoría de edad.

print("📌 EJERCICIO 6\n")
import math
nombre_usuario = input("¿Cuál es tu nombre?")
edad_usuario = int(input("¿Cuál es tu edad?"))
ciudad_usuario = input("¿Cuál es tu ciudad?")
#if edad_usuario < 18:
#    edad_usuario = 18
#Visto en la solución de Mario:
edad_redondeada = math.ceil(edad_usuario/18)*18
print(f"Tu nombre es {nombre_usuario}, tienes {edad_usuario} años y vives en {ciudad_usuario}. Edad mínima adulta: {edad_redondeada} años.")
print()

# 7️⃣ Generador de contraseñas aleatorias
#     Pide al usuario su nombre.
#     Genera una contraseña segura con la primera letra en mayúscula, un número aleatorio y un símbolo especial.
#     Muestra la contraseña generada.

print("📌 EJERCICIO 7\n")
nombre = input ("¿Cuál es tu nombre?")
inicial = nombre[0].upper()
numero = random.randint(10000000,99999999)
simbolo = "/"
contraseña = inicial + str(numero) + simbolo
print(contraseña)
print()

# 8️⃣ Verificación de nombres en listas
#     Pide al usuario su nombre.
#     Verifica si su nombre está en una lista de invitados predefinida.
#     Si está en la lista, muestra su posición.

print("📌 EJERCICIO 8\n")
lista_nombre = [
    "Kenneth",
    "Paula",
    "Sara",
    "Sofía",
    "Mateo",
    "Valeria",
    "Lucas",
    "Martina",
    "Diego",
    "Camila",
    "Andrés",
    "Isablea",
    "Tomás"
]
invitado = input("¿Cuál es tu nombre?")
if invitado in lista_nombre:
    print(f"Hola {invitado}. Tu posición en la lista es la número {lista_nombre.index(nombre)+1}.")
else:
    print("Tu nombre no se encuentra en la lista.")
print()

# 9️⃣ Manipulación de nombres
#     Pide al usuario su nombre y apellido.
#     Convierte el nombre a minúsculas y el apellido a mayúsculas.
#     Genera un alias combinando las primeras 3 letras del nombre y del apellido.
#     Muestra el alias generado.

print("📌 EJERCICIO 9\n")
name_surname = input("Por favor, introduce tu nombre y tu apellido:")
name = name_surname.split(" ")[0]
surname = name_surname.split(" ")[1]
print(f"Tu nombre en minúsculas es {name.lower()} y tu apellido en mayúsculas es {surname.upper()}")
alias = (name[:3] + surname[:3]).capitalize()
print(f"Tu alias es {alias}.")
print()

# 🔟 Formatear y mostrar datos matemáticos
#     Pide al usuario un número decimal.
#     Muestra el número redondeado a dos decimales.
#     Calcula y muestra su cuadrado.
#     Calcula y muestra su raíz cuadrada.

print("📌 EJERCICIO 10\n")
numero_decimal = input("Por favor, introduce un número decimal:")
print(f"Tú numero decimal redondeado a dos decimales es {round(float(numero_decimal) , 2)}.")
print(f"El cuadrado de tu número es {float(numero_decimal)**2.0}.")
print(f"La raíz cuadrada de tu número es {float(numero_decimal)**0.5}.")
print()