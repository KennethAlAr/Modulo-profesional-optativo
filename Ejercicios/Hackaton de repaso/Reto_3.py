nombre = input("Escribe tu nombre y tus apellidos:")

nombres = nombre.split(" ")
iniciales = ""
for palabra in nombres:
    iniciales += palabra[0].upper()

print(f"Tus iniciales son {iniciales}")