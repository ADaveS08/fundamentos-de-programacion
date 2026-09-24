import time

def Tiempo_de_Carga():

    print("Cargando...")
    for i in range(11):
        porcentaje = i * 10
        barra = "■" * i + "-"*(10 - 1)
        print(f"\r[{barra}] {porcentaje}%", end="")
        time.sleep(0.1)




Registrados = []

def Nuevo_integrante():



    try:
        print("\n=============================================")
        print("\t---REGISTRO DE NUEVO JUGADOR---")
        nombre = input("\nIngresa tu nombre: ")
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
            print("Error, No se permite el uso de texto en este apartado. Intenta de nuevo.")

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

    print("\n=============================================")
    print("\n       JUGADORES REGISTRADOS")
    print("=============================================")

    if len(Registrados) == 0:
        print("No hay jugadores registrados.")
        return

    for jugador in Registrados:
        print(f"Nombre: {jugador['Nombre']}")
        print(f"Edad: {jugador['Edad']} años")
        print(f"Estatura: {jugador['Estatura']} m")
        print("---------------------------------------------")

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

    print("\nJugadores guardados correctamente.")

#--------------------------------------------------------------------------------------
# Leer el Archivo

    
def Leer_Archivo():
    print("\nLeyendo archivo...\n")

    try:
        with open("jugadores.txt", "r", encoding="utf-8") as jugadores:
            contenido = jugadores.read()
            
            # .strip() remueve espacios en blanco, tabulaciones y saltos de línea
            if not contenido.strip():
                print("El archivo está vacío.")
            else:
                print(contenido)

    except FileNotFoundError:
        print("El archivo 'jugadores.txt' no se encontró.")




# ------------------------------------------------------------------------------------ 
# Menu principal


while True:
    Menu = [
    ["1", "Registrar jugador"],
    ["2", "Consultar jugadores"],
    ["3", "Guardar jugadores"],
    ["4", "Leer archivo"],
    ["5", "Información del equipo"],
    ["6", "Finalizar programa"]
]


    print("\n=============================================")
    print("\t       MENU PRINCIPAL")
    print("---------------------------------------------")
    print("(1) Registrar Jugador")
    print("(2) Consultar Jugadores")
    print("(3) Guardar jugadores")
    print("(4) Leer Archivo")
    print("(5) Información del equipo")
    print("(6) Finalizar el programa")
    print("---------------------------------------------")

    try:
        opcion = int(input("Ingresa una opción numérica del 1-6: "))

        if opcion == 1:
            Tiempo_de_Carga()
            Nuevo_integrante()

        if opcion == 2:
            Tiempo_de_Carga()
            Consultar_Jugadores()

        if opcion == 3:
            Tiempo_de_Carga()
            Guardar_Jugadores()

        if opcion == 4:
            Tiempo_de_Carga()
            Leer_Archivo()

        #if opcion == 5:

        if opcion == 6:
            print("\nPrograma finalizado.")
            print("!Hasta pronto¡")
            break

        elif opcion not in range(1, 7):
            print("Error, solo puedes ingresar opciones del 1 - 6.")


    
    except ValueError:
        print("No se permite el uso de texto en este apartado. Intenta de nuevo.")





