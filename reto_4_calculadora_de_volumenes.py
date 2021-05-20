import math


def run():
    opcion = int(input("Ingrese la opción de la figura geométrica: "))
    if opcion == 1:
        radio = int(input("Ingrese el radio de la base del cilindro: "))
        altura = int(input("Ingrese la altura del cilindro: "))
        area_base = math.pi*radio**2
        volumen = area_base*altura
        print(f"El volumen del cilindro es {volumen}.")
    elif opcion == 2:
        radio = int(input("Ingrese el radio de la esfera: "))
        volumen = (4/3)*math.pi*radio**3
        print(f"El volumen de la esfera es {volumen}.")
    elif opcion == 3:
        longitud = int(
            input("Ingrese la longitud de una de las aristas del cubo: "))
        volumen = longitud**3
        print(f"El volumen del cubo es {volumen}.")
    elif opcion == 4:
        longitud = int(
            input("Ingrese la longitud de una de las aristas de la base de la pirámide: "))
        altura = int(input("Ingrese la altura de la piramide: "))
        area_base = longitud**2
        volumen = area_base*altura/3
        print(f"El volumen de la pirámide es {volumen}.")
    else:
        radio = int(input("Ingrese el radio de la base del cono: "))
        altura = int(input("Ingrese la altura del cono: "))
        area_base = math.pi*radio**2
        volumen = area_base*altura/3
        print(f"El volumen del cono es {volumen}.")


if __name__ == "__main__":
    print("""
    Hola, ¿A qué tipo de figura geométrica le quieres calcular el volumen?
    1: Cilindro.
    2: Esfera.
    3: Cubo.
    4: Pirámide.
    5: Cono.
    """)
    run()
