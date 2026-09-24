nombre = input("Ingresa tu nombre: ")

while True:
    try:
        edad = int(input("Ingresa tu edad: "))

        if edad <= 17:
            print("La edad debe ser mayor a 17 años")
            continue
        break
    except ValueError:
        print("Error, ingresa un número entero para la edad")