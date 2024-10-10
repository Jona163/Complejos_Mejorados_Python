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

# Función para graficar números complejos en el plano cartesiano
def graficar_cartesiano(complejo1, complejo2, resultado):
    fig, ax = plt.subplots()
    # Graficar operandos y resultado si son distintos
    if complejo1 != resultado:
        ax.plot([complejo1.real, complejo2.real], [complejo1.imag, complejo2.imag], 'bo-', label='Operandos')
        ax.text(complejo1.real, complejo1.imag, f'({complejo1.real}, {complejo1.imag})', fontsize=10, ha='right')
        ax.text(complejo2.real, complejo2.imag, f'({complejo2.real}, {complejo2.imag})', fontsize=10, ha='right')
    ax.plot([resultado.real], [resultado.imag], 'ro', label='Resultado')
    ax.text(resultado.real, resultado.imag, f'({resultado.real}, {resultado.imag})', fontsize=10, ha='right')

 # Ajustes estéticos del gráfico
    ax.spines['left'].set_position('zero')
    ax.spines['left'].set_color('gray')
    ax.spines['bottom'].set_position('zero')
    ax.spines['bottom'].set_color('gray')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_aspect('equal', adjustable='box')
    ax.legend(loc='upper left')
    plt.xlabel('Real')
    plt.ylabel('Imaginario')
    plt.title("Gráfica cartesiana", fontsize=15, color='red', fontname="Times New Roman")
    plt.grid(True)
    plt.show()

# Función para graficar números complejos en el plano polar
def graficar_polar(complejo1, complejo2, resultado):
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    # Graficar operandos y resultado si son distintos
    if complejo1 != resultado:
        ax.plot([cmath.phase(complejo1), cmath.phase(complejo2)], [abs(complejo1), abs(complejo2)], 'bo-', label='Operandos')
    ax.plot([cmath.phase(resultado)], [abs(resultado)], 'ro', label='Resultado')
    ax.legend(loc='upper right')
    ax.set_title("Gráfica polar", fontsize=15, fontname="Times New Roman")  # Modificado el título aquí
    plt.show()

# Bucle principal
repetir = True
while repetir:
    print(f"{Fore.CYAN}**************Calculadora de Numeros Complejos**************")
    print("Numeros de la forma a+bi")
    print("Con a como la parte real y b la parte imaginaria")
    print("************************************************************")
    menu()

 case = int(input(f"{Fore.YELLOW}Selecciona una operacion: {Style.RESET_ALL}"))
    if case == 8:
        # Opción para salir
        print(f"{Fore.RED}Saliendo de la calculadora...")
        repetir = False
    elif case in [1, 2, 3, 4]:
