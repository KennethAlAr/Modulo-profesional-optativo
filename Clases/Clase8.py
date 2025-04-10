numero = 1
print(numero)
numero = 10 * numero
print(numero)

if numero == 10: #Si el número es 10
    print("Es diez") # imprime "es diez"
elif numero == 0: #Si se ejecuta la primera condición, el resto de condiciones no se ejecutan.
    print("Es cero")
else: #Esto solo se ejecuta si ninguna de las otras opciones se ejecuta
    print("No es un número")