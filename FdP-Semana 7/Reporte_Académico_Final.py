import time


def Tiempo_de_Carga():

    print("Cargando...")
    for i in range(11):
        porcentaje = i * 10
        barra = "■■" * i + "--" * (10 - i)
        print(f"\r[{barra}] {porcentaje}%", end="")
        time.sleep(0.1)

def Tiempo_de_Carga2():

    print("Cargando...")
    for i in range(11):
        porcentaje = i * 10
        barra = "■■" * i + "--" * (10 - i)
        print(f"\r[{barra}] {porcentaje}%", end="")
        time.sleep(0.05)

#-----------------------------------------------------------------------------------------
# def (1)

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

    while True:
        try:
            Experiencia = int(input("Ingresa tu experiencia en el juego en meses con números enteros: "))

            if Experiencia < 0:
                print("No se permiten números negativos")
                continue
            break
        except ValueError:
            print("Error, solo se permiten números")
            
        


    Jugador = {
        "Nombre": nombre,
        "Edad": edad,
        "Estatura": estatura,
        "Experiencia": Experiencia
    }
    

    Registrados.append(Jugador)
    print(f"\n¡{nombre} ha sido registrad@ con éxito!")




# -----------------------------------------------------------------------------------
# Lista de jugadores def (2)

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
        print(f"Experiencia: {jugador['Experiencia']} meses")
        print("---------------------------------------------")

#---------------------------------------------------------------------------------------
# Guardar a los jugadores en un archivo .txt. def(3)

def Guardar_Jugadores():

            # "as" da nombre temporal al .txt
    with open("jugadores.txt", "w") as L_Jugadores:

        for jugador in Registrados:
            L_Jugadores.write(f"Nombre: {jugador['Nombre']}\n")
            L_Jugadores.write(f"Edad: {jugador['Edad']}\n")
            L_Jugadores.write(f"Estatura: {jugador['Estatura']} m\n")
            L_Jugadores.write(f"Experiencia: {jugador['Experiencia']} meses\n")
            L_Jugadores.write("-----------------------------\n")
        
        print("\nJugadores guardados correctamente.")
    

    
#--------------------------------------------------------------------------------------
# Leer el Archivo def (4)

    
def Leer_Archivo():
    print("\nLeyendo archivo...\n")

    try:
        with open("jugadores.txt", "r", encoding="cp1252") as jugadores:
            contenido = jugadores.read()

            if not contenido.strip():
                print("El archivo está vacío.")
            else:
                print(contenido)

    except FileNotFoundError:
        print("El archivo 'jugadores.txt' no se encontró.")

#--------------------------------------------------------------------------------------
# Mini menu dentro de Menú principal def(5)


def Informacion_de_equipo():
    print("\n=============================================")
    print("\n       INFORMACION DEL EQUIPO")
    print("=============================================")


    EstaturaB = 1.65
    ExperienciaB = 24

    EstaturaE = 1.75
    ExperienciaE = 6

    EstaturaA = 1.70
    ExperienciaA = 12

    EstaturaP = 1.75
    ExperienciaP = 18

    EstaturaAP = 1.80
    ExperienciaAP = 20


    Posiciones = [
        ("Ala-Pivot", EstaturaAP, ExperienciaAP),
        ("Pivot", EstaturaP, ExperienciaP),
        ("Alero", EstaturaA, ExperienciaA),
        ("Escolta", EstaturaE, ExperienciaE),
        ("Base", EstaturaB, ExperienciaB)
    ]

    if len(Registrados) == 0:
        print("No hay jugadores registrados.")
        return


    for jugador in Registrados:

        Posicion = "Sin posición recomendada"

        for NombrePosicion, EstaturaMinima, ExperienciaMinima in Posiciones:

            if jugador["Estatura"] >= EstaturaMinima and jugador["Experiencia"] >= ExperienciaMinima:
                Posicion = NombrePosicion
                break

        print(f"\nNombre: {jugador['Nombre']}")
        print(f"Estatura: {jugador['Estatura']} m")
        print(f"Experiencia: {jugador['Experiencia']} meses")
        print(f"Posición recomendada: {Posicion}")
        print("---------------------------------------------")

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
            Tiempo_de_Carga2()
            Nuevo_integrante()

        elif opcion == 2:
            Tiempo_de_Carga2()
            Consultar_Jugadores()

        elif opcion == 3:
            Tiempo_de_Carga2()
            Guardar_Jugadores()

        elif opcion == 4:
            Tiempo_de_Carga2()
            Leer_Archivo()

        elif opcion == 5:
            Tiempo_de_Carga2()
            Informacion_de_equipo()

        elif opcion == 6:
            print("\nPrograma finalizado.")
            print("!Hasta pronto¡")
            break

        else:
            if opcion not in range(1, 7):

                print("Error, solo puedes ingresar opciones del 1 - 6.")


    except ValueError as error:
        print("OCURRIÓ UN ERROR:")
        print(error)





