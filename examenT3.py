import random
import math


def pedir_numero(mensaje):
    """Pide un número decimal positivo al usuario."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("Debe ser un número mayor que 0.")
        except ValueError:
            print("Ingrese un número válido.")


def pedir_cantidad(mensaje):
    """Pide un entero positivo (cantidad de puntos)."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("Debe ser un entero mayor que 0.")
        except ValueError:
            print("Ingrese un número entero válido.")


def en_elipse(x, y, a, b):
    return (x ** 2) / (a ** 2) + (y ** 2) / (b ** 2) <= 1


def en_hiperbola(x, y, c, d):
    return (x ** 2) / (c ** 2) - (y ** 2) / (d ** 2) >= 1


def montecarlo(a, b, c, d, n):
    dentro_elipse = 0
    dentro_interseccion = 0

    for _ in range(n):
        x = random.uniform(-a, a)   
        y = random.uniform(-b, b)   

        if en_elipse(x, y, a, b):
            dentro_elipse += 1
            if en_hiperbola(x, y, c, d):
                dentro_interseccion += 1

    return dentro_elipse, dentro_interseccion


def main():
    print("=== Área de la intersección elipse-hipérbola (Montecarlo) ===")
    a = pedir_numero("Ingrese a (elipse): ")
    b = pedir_numero("Ingrese b (elipse): ")
    c = pedir_numero("Ingrese c (hipérbola): ")
    d = pedir_numero("Ingrese d (hipérbola): ")
    n = pedir_cantidad("Cantidad de puntos aleatorios: ")

    dentro_elipse, dentro_interseccion = montecarlo(a, b, c, d, n)

    area_elipse = math.pi * a * b

    if dentro_elipse > 0:
        area_interseccion = (dentro_interseccion / dentro_elipse) * area_elipse
    else:
        area_interseccion = 0

    print("\n=== RESULTADOS ===")
    print(f"Puntos generados: {n}")
    print(f"Puntos dentro de la elipse: {dentro_elipse}")
    print(f"Puntos dentro de la intersección elipse-hipérbola: {dentro_interseccion}")
    print(f"Área de la elipse (pi*a*b): {area_elipse:.4f}")
    print(f"Área aproximada de la intersección: {area_interseccion:.4f}")


main()