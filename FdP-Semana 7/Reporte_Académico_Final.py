
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

    # Estatura

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




# -----------------------------------------------------------------------------------
# Lista de jugadores

def Consultar_Jugadores():

    print("\n===================================")
    print("       JUGADORES REGISTRADOS")
    print("===================================")

    if len(Registrados) == 0:
        print("No hay jugadores registrados.")
        return

    for jugador in Registrados:
        print(f"Nombre: {jugador['Nombre']}")
        print(f"Edad: {jugador['Edad']} años")
        print(f"Estatura: {jugador['Estatura']} m")
        print("-----------------------------------")

#---------------------------------------------------------------------------------------
# Guardar a los jugadores en un archivo .txt

def Guardar_Jugadores():

            # "as" da nombre temporal al .txt
    with open("jugadores.txt", "w") as L_Jugadores:

        for jugador in Registrados:
            L_Jugadores.write(f"Nombre: {jugador['Nombre']}\n")
            L_Jugadores.write(f"Edad: {jugador['Edad']}\n")
            L_Jugadores.write(f"Estatura: {jugador['Estatura']} m\n")
            L_Jugadores.write("-----------------------------\n")

    print("Jugadores guardados correctamente.")

#--------------------------------------------------------------------------------------
# Leer el Archivo




# ------------------------------------------------------------------------------------ 
# Menu principal


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

        if opcion == 3:
            Guardar_Jugadores()

        #if opcion == 4:

        #if opcion == 5:

        if opcion == 6:
            print("\nPrograma finalizado.")
            print("!Hasta pronto¡")
            break

        if not opcion == 1 or 2 or 3 or 4 or 5 or 6:
            print("Error, solo puedes ingresar opciones del 1 - 6.")


    
    except ValueError:
        print("NMS we, qpdo.")




