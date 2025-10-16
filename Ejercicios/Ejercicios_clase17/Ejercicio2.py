import os

def count_lines_and_words(path):
    if not os.path.exists(path):
        raise FileNotFoundError("El archivo no existe")
    with open(path, 'r') as file:
        lines = file.readlines()
        words = 0
        for line in lines:
            words += len(line.split())
        return len(lines), words

try:
    lines, words = count_lines_and_words("ejemplo.txt")
    print(f"El número de líneas del archivo ejemplo.txt es de {lines} y tiene {words} palabras.")
except Exception as e:
    print(e)