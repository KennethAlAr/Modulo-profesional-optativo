import os

def list_directory(path):
    if not os.path.exists(path):
        raise FileNotFoundError("El archivo no existe")

    elementos = os.listdir(path)
    resultado = {
        "archivos": [],
        "directorios":[]
    }
    for elemento in elementos:
        if os.path.isfile(elemento):
            resultado["archivos"].append(elemento)
        if os.path.isdir(elemento):
            resultado["directorios"].append(elemento)

    return resultado

path = input("Introduce la ruta que quieres listar:\n")

try:
    print(list_directory(path))
except Exception as e:
    print(e)