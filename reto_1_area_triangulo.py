def area(base, altura, lados_iguales):
    area = base*altura/2
    if lados_iguales == 0:
        tipo_triangulo = "escaleno"
        print("El triángulo es ",tipo_triangulo," y su área es ", area, ".")
    elif lados_iguales == 2:
        tipo_triangulo = "isósceles"
        print("El triángulo es ",tipo_triangulo," y su área es ", area, ".")
    elif lados_iguales == 3:
        tipo_triangulo = "equilatero"
        print("El triángulo es ",tipo_triangulo," y su área es ", area, ".")
    else:
        print("El trángulo sólo puede tener 0, 2 o 3 lados iguales.")  

def main():
    base = int(input("Favor ingresar el valor de la base: "))
    altura = int(input("Favor ingresar el valor de la altura: "))
    lados_iguales = int(input("Favor ingresar el número de lados iguales: "))
    area(base, altura, lados_iguales)

if __name__ == "__main__":
    print("""
    Hola, con este programa puedes calcular el área de un triángulo y su clasificación.
    """)
    main()

    