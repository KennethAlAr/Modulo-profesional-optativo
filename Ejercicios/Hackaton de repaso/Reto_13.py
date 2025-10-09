lista_peliculas = list()

opcion = input("Introduce una película:\n")

while opcion != "fin":
    lista_peliculas.append(opcion)
    opcion = input("Introduce otra película o fin para acabar:\n")

print(f"Número total de películas: {len(lista_peliculas)}")
print(f"Primera película: {lista_peliculas[0]}")
print(f"Primera película: {lista_peliculas[-1]}")
print(f"Todas las películas: {set(lista_peliculas)}")