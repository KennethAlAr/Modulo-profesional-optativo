#1. Longitud de una cadena.
nombre = ("Kenneth Alonso")
print("Longitud del nombre: ", len(nombre))
print()

#2. Convertir texto a mayúsculas y minúsculas.
#upper
print("Esto soy yo en mayúsculas: ", nombre.upper())
#lower
print("Esto soy yo en minúsculas; ", nombre.lower())
print()

#3. Slicing.
print("Primeros 3 caracteres: ", nombre[:3])
print("Últimos 4 caracteres: ", nombre[-4:])
print("Del sexto al décimo caracter: ", nombre[5:10])
print()

#4. Reemplazar palabras en una cadena.
frase = "Me gusta Java"
print("Cambio la palabra: ", frase.replace("Java", "Python"))
print(frase) # El replace es un "maquillaje" no modifica la variable, es un cambio temporal.
print()

#5. Verificar si una cadena existe en otra.
print("Python" in frase)
nueva_frase = "Me gusta Python"
print("Python" in nueva_frase)
print()

#6. Unir varias palabras en una cadena.
palabras = ["Hola", "Mundo", "en", "Python"]
print("Frase completa con join: ", " " .join(palabras))
# En el segundo entrecomillado marcamos qué queremos que haga de separador.
print()

#7. Split.
oracion = "Python es divertido"
palabritas = oracion.split()
print("Lista de palabras de mi grupo: ", palabritas)
print()