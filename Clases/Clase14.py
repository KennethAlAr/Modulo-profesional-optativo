import os

def listar_archivos():
    return os.listdir(".")

def existe_archivo(archivo):
    return os.path.exists(archivo)

def crear_archivo(nombre):
    return open(nombre, "x")

def crear_directorio(nombre):
    try:
        os.mkdir(nombre)
    except FileExistsError:
        raise FileExistsError

def main():
    opcion = -1
    while opcion != 5:
        print("### MENÚ ###")
        print("1. Listar archivos")
        print("2. Verificar existencia de archivo")
        print("3. Crear archivo")
        print("4. Crear directorio")
        print("5. Salir\n")

        opcion = int(input("Elije una opción:\n"))

        if opcion == 1:
            archivos = listar_archivos()
            for archivo in archivos:
                print(archivo)
            print()
        elif opcion == 2:
            archivo = input("¿Qué archivo quieres ver si existe?\n")
            if existe_archivo(archivo):
                print("✅ El archivo existe")
            else:
                print("❌ El archivo no existe")
            print()
        elif opcion == 3:
            nombre_archivo = input("Introduce el nombre del nuevo archivo:\n")
            if existe_archivo(nombre_archivo):
                print("Ese nombre ya existe.")
            else:
                archivo = crear_archivo(nombre_archivo)
                print(f"Archivo {archivo.name} creado con éxito.")
        elif opcion == 4:
            nombre_directorio = input("Introduce el nombre del nuevo directorio:\n")
            try:
                crear_directorio(nombre_directorio)
                print(f"Directorio {nombre_directorio} creado con éxito.\n")
            except FileExistsError:
                print(f"Directorio {nombre_directorio} ya existe\n")
        elif opcion == 5:
            pass
        elif opcion > 5:
            print("Opción no válida\n")


if __name__ == '__main__':
    main()