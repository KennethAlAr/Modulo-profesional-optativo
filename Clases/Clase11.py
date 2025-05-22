mi_lista = [1, 2, 3, 4, 5]

print("Elemento popeado: ", mi_lista.pop())

print("Lista popeada: ", mi_lista)

mi_lista.append(6)

print("Lista con nuevo elemento: ", mi_lista)

mi_lista.insert(0, 6)

print("Lista con nuevo elemento insertado: ", mi_lista)

mi_lista.remove(3)

print("Lista sin el 3", mi_lista) # Solo borra el primero.

mi_lista.sort() # Ordena en orden ascendente, pero no devuelve un valor, modifica la lista

print("Lista ordenada: ", mi_lista) # Ordena en orden ascendente

print("Longitud de la lista", len(mi_lista))