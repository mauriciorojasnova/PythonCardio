def run():
    opcion = int(input("¿Qué opción de conversión deseas usar?: "))
    if opcion == 1:
        millas = int(input("Ingresa el número de millas que deseas convertir: "))
        kilometros = 1.609344*millas
        print(f"{millas} millas correspoden a {kilometros} kilómetros.")
    else:
        kilometros = int(input("Ingresa el número de kilómetros que deseas convertir: "))
        millas = kilometros/1.609344
        print(f"{kilometros} kilómetros correspoden a {millas} millas.")

if __name__ == "__main__":
    print("""
    Hola, con este programas podrás hacer las siguientes conversiones:
    1: Si deseas pasar de millas a kilómetros.
    2: Si deseas pasar de kilómetros a millas.
    """)
    run()