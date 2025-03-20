import math
import random

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

#8. Redondear un número decimal.
numero = 3.1416
print("Mi número redondeado es: ", round(numero, 3)) # el round redondea el número de decimales que le indiques.
print()

#9. Formateo de número decimales.
precio = 19.99
print("Precio con dos decimales: {:.5f}".format(precio)) # con el {:.Xf} marcamos el número de decimales que queremos tener con la X y redondea.
print()

#10. Obtener el valor ASCII de un caracter.
print("Esto es el código ASCII de 'A': ", ord('A'))
print()

#11. Elevar al cuadrado.
numero_al_cuadrado = 5
print("5 al cuadraod es: ", numero_al_cuadrado ** 2)
print()

#12. Raíz cuadrada.

#Con potencia de 1/x
print("Raíz cuadrada de 25 es: ", 25 ** 0.5)

#Con el paquete math y sqrt
numerito = 100
raiz = math.sqrt(numerito)
print("Raíz cuadrada de 100: ", raiz)
print()

#13. Divisiones enteras y resto.
print("División normal: ", 10/3)
print("División entera: ", 10//3)
print("Resto: ", 10%3)
print()

#14. Generar un número aleatorio.
print("Número aleatorio entre 1 y 10: ", random.randint(1,10))
print()

#15. Convertir números a cadenas y viceversa.
numerajo = 300
texto = str(numerajo)
print("Convertido a texto, soy: ", texto)
print(type(numerajo))
print(type(texto))

cadena = "200"
numerajo2 = int(cadena)
print("Convertido a número soy: ", numerajo)
print(type(cadena))
print(type(numerajo2))
print()

#16. Redondear hacia arriba y hacia abajo.
print("Redondeo hacia arriba del numero 3.2: ", math.ceil(3.2))
print("Redondeo hacia abajo del numero 3.2: ", math.floor(3.6))
print()

#17. Convertir una lista en un conjunto, es decir, eliminar duplicados.
numeroides = [1,2,3,3,4,5,5]
sin_duplicados = set(numeroides)
print("La lista de numeroides sin duplicados es: ", sin_duplicados)
print()

#18. Repetir una cadena.
print("Money!" * 3)
print()

#19. Tipo de dato.
dato = 3.14
print("El tipo de variable de DATO es: ", type(dato))
print()

#20. Combinar cadenas y variables en un print.
name = "Kenneth"
edad = 36
print(f"Hola, soy {name} y tengo {edad} años.")