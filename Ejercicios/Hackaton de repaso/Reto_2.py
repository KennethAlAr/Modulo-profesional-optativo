edad = int(input("Introduce tu edad:"))

if edad<13:
    print("Eres un/a niño/a")
elif edad < 18:
    print("Eres un/a adolescente")
elif edad < 64:
    print("Eres un/a adulto/a")
else:
    print("Eres senior")