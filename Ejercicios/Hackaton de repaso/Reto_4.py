string = input("Introduce una cadena de texto:")

mayusculas = 0
minusculas = 0

for letra in string:
    if letra.isupper():
        mayusculas += 1
    elif letra.islower():
        minusculas += 1

total = mayusculas + minusculas

porcentaje_mayusculas = (mayusculas * 100) / total
porcentaje_minusculas = (minusculas * 100) / total

print(f"Tu string tiene un total de {total} letras. {porcentaje_mayusculas:.2f}% son mayusculas ({mayusculas} letras) y {porcentaje_minusculas:.2f}% minúsculas ({minusculas} letras).")