import sys
import os

def list_files(path):
    if not os.path.isdir(path):
        raise NotADirectoryError("La ruta proporcionada no corresponde a un directorio")
    result = 0
    dir_items = os.listdir(path)
    for item in dir_items:
        if os.path.isfile(os.path.join(path, item)):
            result += 1
    return result
try:
    if len(sys.argv) != 2:
        raise IndexError("El programa debe llamarse con un solo argumento")
    print(f"Numero de archivos en el directorio: {list_files(sys.argv[1])}")
except IndexError as e:
    print(e)

