#-------------------------------------------------------------------------------------------
# Colores

# Reset
RESET = "\033[0m"

# Colores normales
NEGRO = "\033[30m"
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CIAN = "\033[36m"
BLANCO = "\033[37m"

# Colores brillantes
GRIS = "\033[90m"
ROJO_CLARO = "\033[91m"
VERDE_CLARO = "\033[92m"
AMARILLO_CLARO = "\033[93m"
AZUL_CLARO = "\033[94m"
MAGENTA_CLARO = "\033[95m"
CIAN_CLARO = "\033[96m"
BLANCO_BRILLANTE = "\033[97m"

# Fondos normales
FONDO_NEGRO = "\033[40m"
FONDO_ROJO = "\033[41m"
FONDO_VERDE = "\033[42m"
FONDO_AMARILLO = "\033[43m"
FONDO_AZUL = "\033[44m"
FONDO_MAGENTA = "\033[45m"
FONDO_CIAN = "\033[46m"
FONDO_BLANCO = "\033[47m"

# Fondos brillantes
FONDO_GRIS = "\033[100m"
FONDO_ROJO_CLARO = "\033[101m"
FONDO_VERDE_CLARO = "\033[102m"
FONDO_AMARILLO_CLARO = "\033[103m"
FONDO_AZUL_CLARO = "\033[104m"
FONDO_MAGENTA_CLARO = "\033[105m"
FONDO_CIAN_CLARO = "\033[106m"
FONDO_BLANCO_BRILLANTE = "\033[107m"





#-----------------------------------------------------------------------------------------
# Bienvenida


print(f"""{FONDO_AZUL} ███  ████  █████  ███  
█     █   █ █     █   █ 
█     ████  ████  █████ 
█     █  █  █     █   █ 
 ███  █   █ █████ █   █ """)


print(f"""\n█████ █   █ 
  █   █   █ 
  █   █   █ 
  █   █   █ 
  █    ███  {RESET}""")

print(f"""{FONDO_BLANCO_BRILLANTE},{NEGRO}\n█████  ███  █   █ ███ ████   ███  
█     █   █ █   █  █  █   █ █   █ 
████  █   █ █   █  █  ████  █   █ 
█     █  █  █   █  █  █     █   █ 
█████  ██ █  ███  ███ █      ███  {RESET}""")

print(f"""{FONDO_ROJO_CLARO}\n████  █████ 
█   █ █     
█   █ ████  
█   █ █     
████  █████ """)

print(f"""\n████   ███   ████ █   █ █████ █████ ████   ███  █     █     
█   █ █   █ █     █  █  █       █   █   █ █   █ █     █     
████  █████  ███  ███   ████    █   ████  █████ █     █     
█   █ █   █     █ █  █  █       █   █   █ █   █ █     █     
████  █   █ ████  █   █ █████   █   ████  █   █ █████ █████ {RESET}""")








import time
import threading

Usuario_Correcto = "TheGoat" 
Contraseña_Correcta = "1234"

def Iniciar_Sesion():

    intentos = 0

    while intentos < 3:

        usuario = input(f"{CIAN}\nIngresa tu usuario: {RESET}")
        contraseña = input(f"{CIAN}Ingresa tu contraseña: {RESET}")

        if usuario == Usuario_Correcto and contraseña == Contraseña_Correcta:
            print(f"{VERDE}Inicio de sesión exitoso.{RESET}")
            return True
        else:
            intentos += 1
            print(f"{ROJO}Usuario o contraseña incorrectos.{RESET}")
            print(f"Intento {intentos} de 3.")

    print(f"{ROJO_CLARO}\nHas superado el número máximo de intentos.{RESET}")
    return False


# def Capturar_fecha()
    






evento_temporizador = threading.Event()
inactividad_detectada = threading.Event()


def Tiempo_de_Carga():

    print(f"{VERDE_CLARO}Cargando...{RESET}")
    for i in range(11):
        porcentaje = i * 10
        barra = "■■" * i + "--" * (10 - i)
        print(f"\r[{barra}] {porcentaje}%", end="")
        time.sleep(0.15)

def Tiempo_de_Carga2():

    print(f"{VERDE_CLARO}Cargando...{RESET}")
    for i in range(11):
        porcentaje = i * 10
        barra = "■■" * i + "--" * (10 - i)
        print(f"\r[{barra}] {porcentaje}%", end="")
        time.sleep(0.05)


def Temporizador_Inactividad():

    while True:
        for i in range(600):

            if evento_temporizador.wait(1):
                break

        else:
            inactividad_detectada.set()
            break


def Iniciar_Temporizador():

    hilo = threading.Thread(
        target=Temporizador_Inactividad,
        daemon=True
    )
    hilo.start()

def Reiniciar_Temporizador():

    evento_temporizador.set()
    evento_temporizador.clear()

def Verificar_Inactividad():

    if inactividad_detectada.is_set():

        respuesta = input("\n¿Sigues estando ahí? (s/n): ").lower()

        if respuesta == "s":
            inactividad_detectada.clear()
            Reiniciar_Temporizador()
            return True

        elif respuesta == "n":
            print("Sesión finalizada por inactividad.")
            return False

        else:
            print("Respuesta no válida.")
            return False

    return True


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

    print(f"\n\n{AZUL}============================================={RESET}")
    print(f"{VERDE_CLARO}       JUGADORES REGISTRADOS{RESET}")
    print(f"{AZUL}============================================={RESET}")

    if len(Registrados) == 0:
        print(f"{ROJO}No hay jugadores registrados.{RESET}")
        return

    for jugador in Registrados:
        print(f"Nombre: {jugador['Nombre']}")
        print(f"Edad: {jugador['Edad']} años")
        print(f"Estatura: {jugador['Estatura']} m")
        print(f"Experiencia: {jugador['Experiencia']} meses")
        print(f"{AZUL}---------------------------------------------{RESET}")

#---------------------------------------------------------------------------------------
# Guardar a los jugadores en un archivo .txt. def(3)

def Guardar_Jugadores():

            
    with open("FdP-Semana 7/jugadores.txt", "w") as L_Jugadores:

        for jugador in Registrados:
            L_Jugadores.write(f"Nombre: {jugador['Nombre']}\n")
            L_Jugadores.write(f"Edad: {jugador['Edad']}\n")
            L_Jugadores.write(f"Estatura: {jugador['Estatura']} m\n")
            L_Jugadores.write(f"Experiencia: {jugador['Experiencia']} meses\n")
            L_Jugadores.write("---------------------------------------------\n")
        
        print(f"{VERDE}\nJugadores guardados correctamente.{RESET}")


    
#--------------------------------------------------------------------------------------
# Leer el Archivo def (4)

    
def Leer_Archivo():
    print("\n\n=============================================")
    print("\n\tLeyendo archivo...")
    print("\n-----------------------------------")

    try:
        with open("FdP-Semana 7/jugadores.txt", "r", encoding="cp1252") as jugadores:
            contenido = jugadores.read()

            if not contenido.strip():
                print(f"{ROJO}El archivo está vacío.{RESET}")
            else:
                print(contenido)

    except FileNotFoundError:
        print(f"{ROJO}El archivo 'jugadores.txt' no se encontró.{RESET}")

#--------------------------------------------------------------------------------------
# Información de equipo def (5)

def Informacion_de_equipo():
    print("\n=============================================")
    print("\n       INFORMACION DEL EQUIPO")
    print("=============================================")

    Posiciones = []

    try:
        with open("FdP-Semana 7/posiciones.txt", "r", encoding="cp1252") as archivo:

            for linea in archivo:
                datos = linea.strip().split(",")

                NombrePosicion = datos[0]
                EstaturaMinima = float(datos[1])
                ExperienciaMinima = int(datos[2])

                Posiciones.append(
                    (NombrePosicion, EstaturaMinima, ExperienciaMinima)
                )

    except FileNotFoundError:
        print("No se encontró el archivo posiciones.txt")
        return

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

acceso = Iniciar_Sesion()

if acceso:

    Iniciar_Temporizador()

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


        print(f"{AMARILLO}\n============================================={RESET}")
        print(f"{MAGENTA}\t       MENU PRINCIPAL{RESET}")
        print(f"{AMARILLO}---------------------------------------------{RESET}")
        print(f"{AMARILLO}(1) {RESET}{MAGENTA_CLARO}Registrar Jugador{RESET}")
        print(f"{AMARILLO}(2) {RESET}{MAGENTA_CLARO}Consultar Jugadores{RESET}")
        print(f"{AMARILLO}(3) {RESET}{MAGENTA_CLARO}Guardar jugadores{RESET}")
        print(f"{AMARILLO}(4) {RESET}{MAGENTA_CLARO}Leer Archivo{RESET}")
        print(f"{AMARILLO}(5) {RESET}{MAGENTA_CLARO}Información del equipo{RESET}")
        print(f"{AMARILLO}(6) {RESET}{MAGENTA_CLARO}Finalizar el programa{RESET}")
        print(f"{AMARILLO}---------------------------------------------{RESET}")

        try:
            opcion = int(input(f"{CIAN}Ingresa una opción numérica del 1-6: {RESET}"))
            Reiniciar_Temporizador()

            if opcion == 1:
                Tiempo_de_Carga()
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

                    print(f"{ROJO}Error, solo puedes ingresar opciones del 1 - 6.{RESET}")
            


        except ValueError as error:
            print(f"{ROJO}OCURRIÓ UN ERROR:{RESET}")
            print(f"{ROJO}error{RESET}")





