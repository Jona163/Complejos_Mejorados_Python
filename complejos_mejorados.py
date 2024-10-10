# Autor: Jonathan Hernández
# Fecha: 09 octubre 2024
# Descripción: Código para complejos mejorados.
# GitHub: https://github.com/Jona163


import cmath
import math
import matplotlib.pyplot as plt
from colorama import Fore, Style

# Función para mostrar el menú de opciones
def menu():
    print("----------MENU----------")
    print(f"{Fore.GREEN}1. SUMA")
    print(f"{Fore.YELLOW}2. RESTA")
    print(f"{Fore.BLUE}3. MULTIPLICACION")
    print(f"{Fore.MAGENTA}4. DIVISION")
    print(f"{Fore.CYAN}5. POTENCIAS A LA N")
    print(f"{Fore.RED}6. POTENCIAS DE i")
    print(f"{Fore.GREEN}7. RAICES DE NUMEROS COMPLEJOS")
    print(f"{Fore.YELLOW}8. SALIR")
    print(Style.RESET_ALL)

 #Función para realizar operaciones entre números complejos
def realizar_operacion(complejo1, complejo2, operacion):
    if operacion == 1:
        resultado = complejo1 + complejo2
    elif operacion == 2:
        resultado = complejo1 - complejo2
    elif operacion == 3:
        resultado = complejo1 * complejo2
    elif operacion == 4:
        # Manejo de división por cero
        if complejo2 == 0:
            print(f"{Fore.RED}Error: No se puede dividir por cero.")
            return None
        resultado = complejo1 / complejo2
    return resultado
