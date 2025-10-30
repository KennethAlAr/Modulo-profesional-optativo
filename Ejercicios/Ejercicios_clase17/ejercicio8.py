# Escribe un programa que simule un sistema de acceso a un recurso protegido.
# El programa debe pedir al usuario un nombre de usuario y una contraseña, y verificar si son correctos.
# Si el acceso es exitoso, debe registrar la fecha y hora del acceso en un archivo de log.
# Si el acceso falla, debe registrar el intento fallido en el mismo archivo de log.
# El programa debe definir una función que realice esta tarea.

import datetime

def control_acceso(user, password):
    if password == "1234":
        with open("log.txt", "a") as file:
            log = file.write(f"[ACCESO] Usuario: {user} - {datetime.datetime.now()}\n")
        print("Acceso concedido")
    else:
        with open("log.txt", "a") as file:
            log = file.write(f"[ERROR] Usuario: {user} - {datetime.datetime.now()}\n")
        print("Acceso denegado")


user = input("Introduce tu nombre de usuario:\n")
password = input("Introduce la contraseña:\n")

control_acceso(user, password)