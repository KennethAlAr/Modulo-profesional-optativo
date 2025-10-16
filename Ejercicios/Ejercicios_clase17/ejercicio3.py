
def escribir_nombres_en_archivo(nombres, archivo):
    if len(nombres) == 0:
        raise ValueError("No se ha proporcionado ningún nombre:\n")
    with open(archivo, 'a') as file:
        for nombre in nombres:
            file.write(f"{nombre}\n")

nombres = input("Introduce una lista de nombres separados por espacio").split()
escribir_nombres_en_archivo(nombres, "nombres.txt")