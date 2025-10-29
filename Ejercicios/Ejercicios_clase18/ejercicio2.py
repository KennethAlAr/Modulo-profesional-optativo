import os

def create_dir(path):
    path_splitted = path.split("/")
    for i in range(len(path_splitted)):
        if i == len(path_splitted)-1 and os.path.exists(path_splitted[i]):
            raise FileExistsError("El directorio ya existe")
        if not os.path.exists(path_splitted[i]):
            os.mkdir(path_splitted[i])
        os.chdir(path_splitted[i])

path = input("Introduce el nombre del nuevo directorio que quieres crear:\n")

try:
    create_dir(path)
except Exception as e:
    print(e)