def run():
    limite_inferior = int(input("Ingresa el valor del número inferior: "))
    limite_superior = int(input("Ingresa el valor del número superior: "))
    fuera_rango = True

    while fuera_rango:
        numero_comparacion = int(input("Ingresa un número dentro del rango de los límites: "))
        if numero_comparacion >= limite_superior or numero_comparacion <= limite_inferior:
            print(f"El número {numero_comparacion} no está dentro del rango de los límites, ingresa otro.")
        else:
            print(f"El número {numero_comparacion} está dentro del rango de los límites, muy bien.")
            fuera_rango = False


if __name__ == "__main__":
    print("""
    Hola, por favor ingresa tres números: un límite inferior, un límite superior y número de comparación.
    El número de comparación debe ser diferente a los límites y estar dentro de su rango.
    """)
    run()