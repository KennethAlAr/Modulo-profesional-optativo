import os

def move_file(path, new_path):
    path_without_file = new_path
    new_filename = ""
    if not os.path.isfile(path):
        raise FileNotFoundError("El archivo no existe.")
    if not os.path.isdir(new_path):
        path_without_file = os.path.rsplit("/",maxsplit=1)[0]
        new_filename = os.path.rsplit("/",maxsplit=1)[1]
        if not os.path.isdir(path_without_file):
            raise FileNotFoundError("No existe el directorio de destino.")
    if len(new_filename) == 0:
        raise ValueError("No se ha pasado un nombre de fichero")
    else:
        with open(path, "r") as old_file:
            old_file_data = old_file.read()
        with open(new_path, "w") as new_file:
            new_file.write(old_file_data)
        
        os.remove(path)

path = input("Introduce la ruta del archivo que quieres mover.\n")
new_path = input("Introduce la nueva ruta del archivo que quieres mover.\n")

try:
    move_file(path, new_path)
except Exception as e:
    print(e)