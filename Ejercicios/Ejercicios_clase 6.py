#1.1. Crear una lista con números del 1 al 5.

mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)

#1.. Modificar el tercer elemento a 10.

mi_lista[2] = 10
print(mi_lista)

#1.3. Agregar el número 7 al final.

mi_lista.append(7)
print(mi_lista)

#2.1. Crear una tupla con los números 1, 2 y 3.

mi_tupla = (1, 2, 3)

#3.1. Crear una matriz 3x3 con números consecutivos.

mi_matriz = [[1,2,3],
             [4,5,6],
             [7,8,9]
             ]

# 3.2. Modificar el elemento de la segunda fila, tercera columna a 10.

mi_matriz[1][2] = 10
print(mi_matriz)

#

mi_lista = [1, 2, 3]

mi_lista.insert(1, 25) # así insertamos un nuevo valor en la posición indicada.

mi_lista.remove(3) # esto elimina el primer dato que coincida con el indicado.

mi_lista.pop(0) #Elimina y devuelve la posición marcada.

