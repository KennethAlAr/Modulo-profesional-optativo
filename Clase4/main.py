'''
Ejercicio 1: Operaciones numéricas complejas
Define cinco variables numéricas distintas (int, float, complex) y realiza diversas
operaciones matemáticas (potenciación, división entera, módulo).
Imprime los resultados formateados en una cadena clara y descriptiva.
'''



'''
Ejercicio 2: Combinación de cadenas y números
Define dos variables numéricas (int, float) y tres cadenas diferentes.
Genera una nueva cadena combinando texto con el resultado de operaciones aritméticas
entre estas variables. Usa conversión explícita (str()) para insertar valores numéricos en la cadena final.
'''



'''
Ejercicio 3: Manipulación avanzada de cadenas
Crea una cadena larga que contenga espacios en blanco al inicio, final, y en medio.
Realiza varias operaciones encadenadas como eliminar espacios extremos,
convertir todo a mayúsculas, y dividir la cadena en varias subcadenas usando un separador específico.
'''



'''
Ejercicio 4: Índices y subcadenas
Define una cadena extensa (mínimo 50 caracteres).
Obtén varias subcadenas usando la indexación por rangos (slicing) y genera
una nueva cadena combinando estas subcadenas en orden inverso.
Imprime la nueva cadena resultante.
'''

cadena_extensa = "Python es un super lenguaje que me re encanta"
subcadena = cadena_extensa[0:6] + "" + cadena_extensa[11:20]
resultado = subcadena[::-1]
print(resultado)

'''
Ejercicio 5: Formato y conversión numérica
Define variables numéricas (entero, flotante, complejo).
Crea una cadena con formato avanzado (f-string) que muestre estos números
con precisión definida (dos decimales, notación científica, etc.)
Evita concatenar directamente números y texto.
'''

entero, flotante, complejo = 12, 345.23976, 5+3j
formato = (f"Entero: {entero},"
           f"Flotante: {flotante:.2f},"
           f"Notación científica: {flotante:2e},"
           f"Complejo: {complejo}")
print(formato)

'''
Ejercicio 6: Operaciones combinadas entre números y cadenas
Define dos variables numéricas enteras y dos cadenas.
Realiza cálculos matemáticos diversos y genera una cadena formateada
que explique cada operación (sumas, restas, multiplicaciones, módulo)
claramente utilizando métodos de cadenas.
'''

num_a, num_b = 15, 4
cad_a, cad_b = "La multiplicación da: ", "y el resto: "
resultado_ej6 = f"{cad_a}{num_a*num_b}, {cad_b}{num_a%num_b}"
print(resultado_ej6)

'''
Ejercicio 7: Cálculo del área y perímetro
Define variables numéricas que representen dimensiones (largo, ancho, radio, altura).
Calcula el área y perímetro de distintas figuras geométricas
(rectángulo, círculo, triángulo rectángulo) y presenta todos
los resultados claramente en una sola cadena formateada usando conversiones explícitas.
'''

largo, ancho, radio, altura = 10, 5, 3, 4
area_rectangulo = largo*ancho
perimetro_rectangulo = 2*(largo+ancho)
area_circulo = 3.14 * radio ** 2
perimetro_circulo = 2 * radio * 3.14
area_triangulo = (largo*altura)/2
resultados = (f"Área de un rectángulo: {area_rectangulo}, "
              f"perímetro del rectángulo: {perimetro_rectangulo}, "
              f"área de un círculo: {area_circulo}, "
              f"perímetro del círculo: {perimetro_circulo}, "
              f"área del triángulo: {area_triangulo}")
print(resultados)

'''
Ejercicio 8: Análisis de texto complejo
Define una cadena extensa que represente un párrafo completo.
Utilizando únicamente métodos de cadenas y funciones integradas (len, upper, split),
obtén el número total de caracteres, palabras y el resultado de transformar el texto completamente a mayúsculas,
presentándolo claramente en una cadena nueva.
'''

parrafo = "Soy un ejemplo de párrafo largo de narices para ocupar todo el espacio que quiero"
caracteres = len(parrafo)
palabroides = len(parrafo.split())
mayusculas = parrafo.upper()
resultado= (f"Total de caracteres: {caracteres}, "
            f"total de palabras: {palabroides}, "
            f"\nTexto en mayúsculas: {mayusculas}")
print(resultado)

'''
Ejercicio 9: Fórmula cuadrática
Dados tres números que representan los coeficientes (a, b, c) de una ecuación cuadrática,
resuelve la fórmula cuadrática para obtener las raíces reales o complejas.
Imprime claramente en una cadena formateada los coeficientes y las raíces encontradas.

'''



'''
Ejercicio 10: Manejo y transformación de datos personales
Crea variables para representar datos personales (nombre, edad, peso, altura).
Calcula el índice de masa corporal (IMC) sin usar bucles, y presenta un resumen detallado
y formateado de todos estos datos personales, incluyendo el IMC con dos decimales.

'''