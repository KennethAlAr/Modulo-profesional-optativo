'''
Vamos a realizar un programa que lea el archivo sistema_log_extenso.txt
y imprima por pantalla todos los mensajes del tipo ERR
'''

log = open("sistema_log_extenso.txt", "r") #Referencia al archivo

log_data = log.readlines() #Lista con todas las lineas en String

for line in log_data:
    if "ERROR" in line:
        print(line, end="")