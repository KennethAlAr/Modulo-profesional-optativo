# Programa principal: menú, flujo general y coordinación

from cli import *
from services import *

def main():
    while True:
        try:
            print_menu()
            option = read_menu_option()
            match option:
                case 1: 
                    # Primero pedir ciudad
                    # Llamar API
                    # Llamar API forecast
                    # Formatear salida
                    city = input_city()
                    lat, long, country = get_geolocation(city)
                    fore_data = get_forecast(lat, long)
                    print(f"Tiempo de la ciudad: {city}, país: {country}")
                    print(f"Temperatura maxima: {fore_data["temp_max"]}")
                    print(f"Temperatura minima: {fore_data["temp_min"]}")
                    print(f"Amanece: {fore_data["sunrise"]}")
                    print(f"Anochece: {fore_data["sunset"]}")
                    print(f"Porbabilidad de lluvia: {fore_data["prec_prob"]}")
                case 0:
                    break
                case _:
                    print("Tienes que escoger una opción numérica válida")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()