'''
Ejercicio 1️⃣: Comparación de números y booleanos
📌 Objetivo: Usar comparaciones con números y analizar los resultados booleanos.
Crea tres variables numéricas con valores diferentes.
Compara los valores entre sí (>, <, >=, <=, ==, !=).
Almacena los resultados en nuevas variables booleanas y muéstralos.
'''

numero_a, numero_b, numero_c = 1, 4, 6
comparacion_a = numero_a > numero_b
comparacion_b = numero_b < numero_c
comparacion_c = numero_c >= numero_a
comparacion_d = numero_a <= numero_c
comparacion_e = numero_b == numero_a
comparacion_f = numero_c != numero_b

print(f"¿Es {numero_a} mayor que {numero_b}? {comparacion_a}")
print(f"¿Es {numero_b} menor que {numero_c}? {comparacion_b}")
print(f"¿Es {numero_c} mayor o igual que {numero_a}? {comparacion_c}")
print(f"¿Es {numero_a} menor o igual que {numero_c}? {comparacion_d}")
print(f"¿Es {numero_b} igual que {numero_a}? {comparacion_e}")
print(f"¿Es {numero_c} diferente que {numero_b}? {comparacion_f}")
print()

'''
Ejercicio 2️⃣: Propiedades y manipulación de cadenas
📌 Objetivo: Trabajar con cadenas y métodos integrados de Python.
Crea una cadena con una frase corta.
Muestra cuántos caracteres tiene la cadena.
Convierte toda la cadena a mayúsculas y minúsculas.
Cuenta cuántas veces aparece una letra específica en la cadena.
'''

frase_corta = "Tatakae"
print(f"La cadena '{frase_corta}' tiene {len(frase_corta)} caracteres.")
print(f"La cadena '{frase_corta}' en mayúsculas es: {frase_corta.upper()}")
print(f"La cadena '{frase_corta}' en minúsculas es: {frase_corta.lower()}")
print(f"La letra 'a' aparece {frase_corta.count("a")} veces en la cadena '{frase_corta}'.")
print()

'''
Ejercicio 3️⃣: Operaciones matemáticas con números y booleanos
📌 Objetivo: Realizar cálculos numéricos usando valores booleanos.
Define dos variables booleanas (verdadero, falso) con los valores True y False.
Realiza operaciones matemáticas con estos valores (+, *, -).
Muestra los resultados y analiza qué sucede.
'''

verdadero = True
falso = False
print(f"verdadero mas verdadero es igual a {verdadero+verdadero}")
print(f"verdadero mas falso es igual a {verdadero+falso}")
print(f"falso mas falso es igual a {falso+falso}")
print(f"verdadero por verdadero es igual a {verdadero*verdadero}")
print(f"verdadero por falso es igual a {verdadero*falso}")
print(f"falso por falso es igual a {falso*falso}")
print(f"verdadero menos verdadero es igual a {verdadero-verdadero}")
print(f"verdadero menos falso es igual a {verdadero-falso}")
print(f"falso menos verdadero es igual a {falso-verdadero}")
print(f"falso menos falso es igual a {falso-falso}")
print()

'''
Ejercicio 4️⃣: Extracción de caracteres en una cadena
📌 Objetivo: Extraer partes de una cadena utilizando índices y slicing.
Define una cadena con una palabra o nombre.
Extrae y muestra los tres primeros caracteres.
Extrae y muestra los tres últimos caracteres.
Extrae los caracteres en posiciones impares de la cadena.
'''

cadena = "Corcholis"
print(f"Los tres primeros carácteres de '{cadena}' son: {cadena[:3]}")
print(f"Los tres últimos carácteres de '{cadena}' son: {cadena[-3:]}")
cadena_impares = ""
for i in range(0, len(cadena)-1):
    if i%2==1:
        cadena_impares = cadena_impares + cadena[i]

print(f"Si quitamos las posiciones pares de la cadena '{cadena}' la nueva cadena es '{cadena_impares}'")
# Cómo la primera posición de la cadena es "0" en este caso los pares son el primero, tercero quinto, etc.
# Si se quiere quitar el segundo, cuarto, sexto, etc. el "if" debe ser "if i%2==0:"
print()

'''
Ejercicio 5️⃣: Conversión de tipos y evaluación booleana
📌 Objetivo: Convertir entre tipos básicos y analizar valores booleanos.
Convierte un número en una cadena y muestra el tipo de dato.
Convierte una cadena numérica en un número entero y muestra el tipo.
Convierte diferentes valores ("", "Texto", 0, 1, -1, None) a booleanos y muestra los resultados.
'''

numero = 32
cadena = str(numero)

print(f"El tipo de dato de la variable 'numero' es: {type(numero)}")
print(f"El tipo de dato de la variable 'cadena' es: {type(cadena)}")

cadena_numerica = "42"
numero_cadena = int(cadena_numerica)

print(f"El tipo de dato de la variable 'cadena_numerica' es: {type(cadena_numerica)}")
print(f"El tipo de dato de la variable 'numero_cadena' es: {type(numero_cadena)}")

cadena_vacia = ""
cadena_texto = "Texto"
numero_0 = 0
numero_1 = 1
numero_menos1 = -1
none = None

booleano_cadena_vacia = bool(cadena_vacia)
booleano_cadena_texto = bool(cadena_texto)
booleano_numero_0 = bool(numero_0)
booleano_numero_1 = bool(numero_1)
booleano_numero_menos1 = bool(numero_menos1)
booleano_none = bool(none)

print(f"El resultado de convertir a booleano '{cadena_vacia}' es: {booleano_cadena_vacia}")
print(f"El resultado de convertir a booleano '{cadena_texto}' es: {booleano_cadena_texto}")
print(f"El resultado de convertir a booleano '{numero_0}' es: {booleano_numero_0}")
print(f"El resultado de convertir a booleano '{numero_1}' es: {booleano_numero_1}")
print(f"El resultado de convertir a booleano '{numero_menos1}' es: {booleano_numero_menos1}")
print(f"El resultado de convertir a booleano '{none}' es: {booleano_none}")