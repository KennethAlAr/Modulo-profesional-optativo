# Créame un diccionario.
persona = {
    "nombre" : "Kenneth",
    "edad" : 36,
    "registrado" : True,
}

print(persona)

#Accédeme a un valor por su clave.
print(persona["edad"])
print(persona["registrado"])

#Añadir una nueva clave-valor.

persona["ciudad"] = "Montdaca"
persona["Número de hijos"] = 0
print(persona)

#Cambiar el valor de una clave.
persona["ciudad"] = "Montcada i Reixac"
persona["Número de hijos"] = 3
print(persona)

#eliminar una clave.
del persona["registrado"]
print(persona)

#Comprobar si una clave ya existe.
existe_nombre = "nombre" in persona
print(existe_nombre)
existe_kenneth = "Kenneth" in persona["nombre"]
print(existe_kenneth)

#Comparar dos valores booleanos.
persona["registrado"] = True
es_menor_y_registrado = persona["edad"] < 18 or persona["registrado"]
print(es_menor_y_registrado)

#Usar NOT con un booleano.
no_veo_registro = not persona["registrado"]
print(no_veo_registro)

#Créame un conjunto a partir de una lista de duplicados.
numeritos = [7,8,4,7,1,2,3,4,7,2,6,8,4]

#Convierto a conjunto. ASÍ ELIMINO DUPLICIDADES Y LOS ORDENA.
conjuntito = set(numeritos)
print(conjuntito)

#Comparar si dos colecciones tienen los mismos elementos únicos.
coleccion_a = set([1,2,2,3,4])
coleccion_b = set([3,4,2,1])

mismos_elementos = coleccion_a == coleccion_b
print(mismos_elementos)