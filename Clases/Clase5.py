'''
Ejercicio 1️⃣: Evaluación de Expresiones Booleanas
📌 Objetivo: Evaluar expresiones numéricas que devuelvan valores booleanos.
Crea variables con expresiones matemáticas y convierte los resultados en booleanos.
Muestra el valor booleano de cada una.
'''
from django.template.defaultfilters import length

expresion1 = 10>5
expresion2 = 7+3==10
expresion3 = 4*2==9
expresion4 = 20<15
print(expresion1, expresion2, expresion3, expresion4)
print()

'''
Ejercicio 2️⃣: Operaciones Matemáticas con Booleanos
📌 Objetivo: Descubrir cómo Python trata los valores True y False en operaciones matemáticas.
Suma True + True y False + True.
Multiplica True * 10 y False * 50.
Muestra los resultados y explica qué ocurre.
'''

print(True+True)
print(True-True)
print(False+True)
print(False+False)
print(False-False)
print(True*10)
print(False*50)
# En las soluciones se ve que True es igual a 1 y False es igual a 0.
print()

'''
Ejercicio 3️⃣: Conversión entre Tipos Básicos
📌 Objetivo: Convertir entre tipos de datos (números, cadenas y booleanos).
Convierte un número en cadena y muéstralo.
Convierte una cadena numérica en un entero.
Convierte un booleano en un número.
'''

print(str(8))
print(int("1236"))
print(int(True))
print()

'''
Ejercicio 4️⃣: Propiedades de las Cadenas
📌 Objetivo: Manipular cadenas y explorar sus propiedades.
Crea una cadena con tu nombre.
Muestra el primer y último carácter.
Muestra la longitud de la cadena.
Convierte la cadena a mayúsculas y minúsculas.
'''

nombre = "Kenneth"
print(nombre[0], nombre[-1])
print(length(nombre))
print(nombre.upper())
print(nombre.lower())
print()

'''
Ejercicio 5️⃣: Operaciones con Cadenas y Números
📌 Objetivo: Realizar operaciones matemáticas con cadenas y números.
Concatenar cadenas con números usando str().
Multiplicar una cadena para repetirla varias veces.
'''

print("Barcelona"+str(123)+"camión"+str(456))
print("Hola" * 5)
print()

'''
Ejercicio 6️⃣: Operaciones con Caracteres y Códigos ASCII
📌 Objetivo: Explorar caracteres y su representación en ASCII.
Obtén el código ASCII de la letra 'A'.
Convierte un número en su carácter ASCII correspondiente.
'''

codigo = ord("A")
print(codigo)
codigo_numero = chr(42)
print(codigo_numero)
print()

'''
Ejercicio 7️⃣: Evaluación de Expresiones Lógicas
📌 Objetivo: Trabajar con operadores lógicos (and, or, not).
Evalúa expresiones lógicas combinando números y operadores lógicos.
Muestra los resultados.
'''

print(10>5 and 3<8)
print(5==5 or 2>10)
print(not(4==4 and 3>1))