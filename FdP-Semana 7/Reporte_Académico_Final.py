
Registrados = []

def Nuevo_integrante():
    try:
        nombre = input("Ingresa tu nombre: ")
    except ValueError:
        print("Error, Solo puedes ingresar texto.")
    

    # EDAD

    while True:
        try:
            edad = int(input("Ingresa tu edad: "))

            if edad <= 17:
                print("La edad debe ser mayor a 17 años")
                continue
            break
        except ValueError:
            print("Error, ingresa un número entero para la edad")

    # ESTATURA

    while True:
        try:
            estatura = float(input("Ingresa tu estatura en metros: "))

            if estatura <= 0:
                print("La estatura no puede ser 0 ni negativa")
                continue
            break
        except ValueError:
            print("Error, Ingresa un número decimal para la estatura")

    Jugador = {
        "Nombre": nombre,
        "Edad": edad,
        "Estatura": estatura
    }

    Registrados.append(Jugador)
    print(f"¡{nombre} ha sido registrad@ con éxito!")


def Consultar_Jugadores():
    print(Registrados)
    
    

        



while True:
    Menu = [
    ["1", "Registrar jugador"],
    ["2", "Consultar jugadores"],
    ["3", "Crear / modificar archivo"],
    ["4", "Leer archivo"],
    ["5", "Información del equipo"],
    ["6", "Finalizar programa"]
]


    print("\n===================================")
    print("       MENU PRINCIPAL")
    print("-----------------------------------")
    print("(1) Registrar Jugador")
    print("(2) Consultar Jugadores")
    print("(3) Crear / Modificar archivo")
    print("(4) Leer Archivo")
    print("(5) Información del equipo")
    print("(6) Finalizar el programa")
    print("-----------------------------------")

    try:
        opcion = int(input("Ingresa una opción numérica del 1-6: "))

        if opcion == 1:
            Nuevo_integrante()

        if opcion == 2:
            Consultar_Jugadores()

        #if opcion == 3:

        #if opcion == 4:

        #if opcion == 5:

        if opcion == 6:
            print("\nPrograma finalizado.")
            print("!Hasta pronto¡")
            break

    
    except ValueError:
        print("Hola")




