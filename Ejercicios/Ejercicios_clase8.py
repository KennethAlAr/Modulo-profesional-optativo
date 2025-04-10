# Ejercicio 1️⃣ - Siempre negatifo, nunca positifo:
# Escribe un programa que pida al usuario un número entero y determine si es positivo o negativo.
# El programa debe imprimir un mensaje indicando el resultado.

numero = int(input("Escribe un número entero"))
print(numero)

if numero >= 0:
    print("es positivo")
else:
    print("es negativo")

# Ejercicio 2️⃣ - Portero de discoteca:
# Escribe un programa que simule el trabajo de un portero de discoteca.
# El programa debe pedir al usuario su edad y determinar si puede entrar o no.
# Si la edad es menor de 18 años, el programa debe imprimir "No puedes entrar".
# Si la edad es mayor o igual a 18 años, el programa debe imprimir "Puedes entrar".
# Si la edad es mayor de 60 años, el programa debe imprimir "Vete a la otra discoteca".
# Si la edad es menor de 18 años y mayor o igual de 16 años, el programa debe imprimir "Vete a la discoteca de menores"

edad = int(input("¿Cuántos años tienes?"))

if edad >= 18 and edad <= 60:
    print("Puedes entrar")
elif edad > 60:
    print("Vete a oldSkoolVeterans")
elif edad >= 16: # No hace falta especificar si son menores de 18 años porque ya pasan por la primera condición.
    print("Vete a KinderGarden")
else:
    print("Vete a tu casa")

# Ejercicio 3️⃣ - Pacman
# Escribe un programa que pida al usuario dos números enteros correspondientes
# a la casilla que está Pacman (1er número) y a la que está un fantasma (2o número),
# luego debe recibir un texto con el formato "normal" o "caramelo". Si el texto es
# "normal" y los números son iguales, el programa debe imprimir "Pacman ha sido atrapado".
# Si el texto es "caramelo" y los números son iguales, el programa debe imprimir "Pacman ha comido al fantasma".
# En cualquier otro caso, el programa debe imprimir "Pacman ha escapado".

posicion_pacman = int(input("¿En qué posición está Pacman?"))
posicion_fantasma = int(input("¿En qué posición está el fantasma?"))

if posicion_pacman == posicion_fantasma:
    #Caramelo -> Pacman come fantasma
    #Invisible -> Pacman escapa
    #Normal -> Pacman atrapado
    estado_pacman = input("¿Cómo es el estado de Pacman?")
    if estado_pacman == "caramelo":
        print("Pacman se ha comido al fantasma")
    elif estado_pacman == "invisible":
        print("Pacman ha escapado")
    else:
        print("Pacman ha sido atrapado")
else:
    print("Pacman ha escapado")


# Ejercicio 4️⃣ - Múltiplos de 3 y 5
# Escribe un programa que pida al usuario un número entero y determine si es múltiplo de 3 o de 5.
# El programa debe imprimir un mensaje indicando el resultado. Si el número es múltiplo de ambos,
# debe imprimir "Múltiplo de 3 y 5". Si no es múltiplo de ninguno, debe imprimir "No es múltiplo de 3 ni de 5".

numero_introducido = int(input("Introduce un número entero:"))

if numero_introducido % 3 == 0:
    if numero_introducido % 5 == 0:
        print("Múltiplo de 3 y de 5.")
    else:
        print("Múltiplo de 3.")
elif numero_introducido % 5 == 0:
    print("Múltiplo de 5.")
else:
    print("No es múltiplo de 3 ni de 5.")


# Ejercicio 5️⃣ - Puede entrar en el servidor de Discord?
# Escribe un programa que pida un rol y una academia de estudios,
# si el rol es "alumno" y la academia es "Prometeo" el programa debe darle acceso al servidor de Discord oficial
# y al de los alumnos, donde se critica a los profes. Si el rol es "profesor" y la academia es "Prometeo"
# el programa debe darle acceso al servidor de Discord oficial, pero no al de los alumnos.
# En cualquier otro caso, el programa debe imprimir "No tienes acceso al servidor de Discord".

rol = input("¿Eres profesor o alumno?")
academia = input("¿Cuál es tu academia?")

if rol == "alumno" and academia == "Prometeo":
    print("Acceso concedido al discord oficial y al underground")
elif rol == "profesor" and academia == "Prometeo":
    print("Acceso concedido al discord oficial (no existe ningún otro)")
else:
    print("No tienes acceso al servidor de discord.")