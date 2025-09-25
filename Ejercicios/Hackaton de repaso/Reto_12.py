import random
import statistics

dados = random.randint(1, 6)

tiradas = []

for i in range (0,10):
    tiradas.append(random.randint(1, 6))

print (tiradas)

for i in range(0,10):
    print(f"La tirada numero {i} ha sido un: {tiradas[i]}")

print(f"El primer número mas repetido es {statistics.mode(tiradas)}")