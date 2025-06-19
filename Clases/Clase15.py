import os
from colorama import Fore, Style
from Clase15.lectura import leer_entero, leer_string
from Clase15.escritura import imprimir, imprimir_con_marco, imprimir_con_marco_centrado

colores_mensajes = {
    "ERROR" : Fore.LIGHTRED_EX,
    "MENU" : Fore.BLUE,
    "INPUT" : Fore.YELLOW,
    "SUCCESS" : Fore.LIGHTGREEN_EX
}

def listar_archivos(ruta):
    try:
        return os.listdir(ruta)
    except FileNotFoundError:
        raise FileNotFoundError

def existe_archivo(archivo):
    return os.path.exists(archivo)

def crear_archivo(nombre):
    return open(nombre, "x")

def crear_directorio(nombre):
    try:
        os.mkdir(nombre)
    except FileExistsError:
        raise FileExistsError

def color_segun_extension(ruta, archivo):
    if os.path.isdir(ruta+archivo):
        return "magenta"
    elif len(archivo.split(".")[-1]) == 1:
        return "white"
    elif archivo.split(".")[-1] == "txt":
        return "green"
    elif archivo.split(".")[-1] in ["jpg", "png"]:
        return "blue"
    elif archivo.split(".")[-1] in ["mp3", "wma"]:
        return "yellow"
    return "white"

def colorear(color):
    if color == "magenta":
        return Fore.MAGENTA
    elif color == "blue":
        return Fore.BLUE
    elif color == "yellow":
        return Fore.YELLOW
    elif color == "green":
        return Fore.GREEN
    elif color == "white":
        return Fore.WHITE

def main():
    opcion = -1
    while opcion != 5:
        menu = """MENU\n1. Listar archivos\n2. Verificar existencia de archivo\n3. Crear archivo\n4. Crear directorio\n5. Salir"""
        imprimir_con_marco_centrado(menu, colores_mensajes["MENU"])

        # imprimir_con_marco("MENÚ", colores_mensajes["MENU"])
        # imprimir("1. Listar archivos", colores_mensajes["MENU"])
        # imprimir("2. Verificar existencia de archivo", colores_mensajes["MENU"])
        # imprimir("3. Crear archivo", colores_mensajes["MENU"])
        # imprimir("4. Crear directorio", colores_mensajes["MENU"])
        # imprimir("5. Salir\n", colores_mensajes["MENU"])

        opcion = leer_entero("Introduce una opción:\n", Fore.YELLOW)

        if opcion == 1:
            ruta = leer_string("Introduce la ruta que quieres consultar:\n")
            try:
                archivos = listar_archivos(ruta)
                for archivo in archivos:
                    imprimir(archivo, colorear(color_segun_extension(ruta, archivo)))
            except FileNotFoundError:
                imprimir(f"La ruta {ruta} no existe.", Fore.RED)
            except:
                imprimir("Error al consultar la ruta, inténtalo de nuevo.", Fore.RED)
            print()
        elif opcion == 2:
            archivo = leer_string("¿Qué archivo quieres ver si existe?\n")
            if existe_archivo(archivo):
                imprimir("✅ El archivo existe", Fore.GREEN)
            else:
                imprimir("❌ El archivo no existe", Fore.RED)
            print()
        elif opcion == 3:
            nombre_archivo = leer_string("Introduce el nombre del nuevo archivo:\n")
            if existe_archivo(nombre_archivo):
                imprimir("Ese nombre ya existe.", Fore.RED)
            else:
                archivo = crear_archivo(nombre_archivo)
                imprimir(f"Archivo {archivo.name} creado con éxito.", Fore.GREEN)
        elif opcion == 4:
            nombre_directorio = leer_string("Introduce el nombre del nuevo directorio:\n")
            try:
                crear_directorio(nombre_directorio)
                imprimir(f"Directorio {nombre_directorio} creado con éxito.\n", Fore.GREEN)
            except FileExistsError:
                print(f"Directorio {nombre_directorio} ya existe\n")
        elif opcion == 5:
            pass
        elif opcion > 5:
            print("Opción no válida\n")


if __name__ == '__main__':
    main()