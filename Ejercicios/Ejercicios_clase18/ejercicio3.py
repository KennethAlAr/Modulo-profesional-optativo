import os

def delete_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError("El archivo no existe")
    if os.path.isdir(path):
        raise ValueError(f"{path} es un directorio")

    os.remove(path)

    return f"El archivo {path} ha sido eliminado con éxito."


path = input("Introduce la ruta del archivo que quieres eliminar:\n")

try:
    delete_file(path)
except Exception as e:
    print(e)
