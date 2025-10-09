inventario = {}

while True:
    try:
        opcion = int(input("Sistema de Gestión:\n1-Añadir producto\n2-Vender producto\n3-Visualizar inventario\n4- Salir\n"))
    except:
        ValueError("Tiennes que escoger una opción de la 1 a la 4")

    match opcion:
        case 1:
            nombre = input("Introduce el nombre del producto:\n")
            cantidad = input("Introduce la cantidad del producto:\n")
            inventario[nombre] = inventario.get(nombre, 0) + cantidad # El get inicializa si no existe y pone por default el 0. Si existe coge el value que ya tenga
        case 2:
            stock = inventario.get(nombre)
            if stock == None:
                print("No existe el producto en el inventario")
            elif stock < cantidad:
                print("No existe suficiente cantidad en el inventario")
            else:
                inventario[nombre] = stock - cantidad
        case 3:
            if not inventario:
                print("Inventario vacío")
            else:
                for producto, cantidad in sorted(inventario.items()):
                    print(f"Producto: {producto} - Cantidad: {cantidad} unidades")
        case 4:
            print("Saliendo")
            exit()
