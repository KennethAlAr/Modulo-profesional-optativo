# Escribe un programa que simule un sistema de acceso a un recurso protegido.
# El programa debe pedir al usuario un nombre de usuario y una contraseña, y verificar si son correctos.
# Si el acceso es exitoso, debe registrar la fecha y hora del acceso en un archivo de log.
# Si el acceso falla, debe registrar el intento fallido en el mismo archivo de log.
# El programa debe definir una función que realice esta tarea.

from datetime import datetime

usuarios = {
    "jordi":"c0ntr4s3n4",
    "asires": "seguridad",
    "damdawers": "prototipo"
}

def control_acceso(user, password):
    with open("log.txt", "a") as file:
        if user not in usuarios.keys():
            file.write(f"[USER DONT EXIST] Usuario: {user} - {datetime.now().isoformat(timespec="seconds")}\n")
            raise ValueError("Acceso denegado.")

        if password == usuarios.get(user):
            file.write(f"[ACCESO] Usuario: {user} - {datetime.now().isoformat(timespec="seconds")}\n")
            print("Acceso concedido.")
        else:
            file.write(f"[ERROR-WRONG PASSWORD] Usuario: {user} - {datetime.now().isoformat(timespec="seconds")}\n")
            raise ValueError("Acceso denegado.")

while True:
    user = input("Introduce tu nombre de usuario:\n")
    password = input("Introduce la contraseña:\n")
    try:
        control_acceso(user, password)
    except Exception as e:
        print(e)