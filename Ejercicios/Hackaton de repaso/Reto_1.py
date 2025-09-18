precio = float(input("Introduce el precio original del producto:"))
descuento = float(input("Introduce el procentaje de descuento que tiene el producto:"))
final = precio * (100-descuento) / 100

print(f"El precio del producto original es de {precio:.2f}€ y el descuento es del {descuento}%."
      f"El precio final es de {final:.2f}€.")