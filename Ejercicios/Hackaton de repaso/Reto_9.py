palabra = input("Introduce una palabra:")

# palabra_reverse = palabra[::-1]
#
# letras = ["a", "e", "i", "o", "u"]
#
# resultado = ""
#
# for letra in palabra_reverse:
#     if letra in(letras):
#         resultado += "*"
#     else:
#         resultado += letra
#
# print (resultado)

for i in range (len(palabra)-1, -1, -1):
    if palabra[i].lower() in ("a", "e", "i", "o", "u"):
        print("*", end="")
    else:
        print(palabra[i], end="")
print()