# Bienvenido al taller de Basquet. Falcon University Technological.

# Variables
Nombre = ""
Edad = 0
Estatura = 0.0
# Experiencia en meses
Experiencia = 0

# Mínimo de Cupos
Cupos = 20

# Requisitos de cada posicion (Estatura en Metros) (Experiencia en meses)

# Jugador Base
EstaturaB = 1.65
ExperienciaB = 24

# Jugador Escolta
EstaturaE = 1.75
ExperienciaE = 6

# Jugador Alero
EstaturaA = 1.70
ExperienciaA = 12

# Jugador Pivot
EstaturaP = 1.75
ExperienciaP = 18

# Jugador Ala-Pivote
EstaturaAP = 1.80
ExperienciaAP = 20


# Lista de posiciones con sus requisitos
Posiciones = [
    ("Ala-Pivot", EstaturaAP, ExperienciaAP),
    ("Pivot", EstaturaP, ExperienciaP),
    ("Alero", EstaturaA, ExperienciaA),
    ("Escolta", EstaturaE, ExperienciaE),
    ("Base", EstaturaB, ExperienciaB)
]


# Las variables que acumulan los valores
TotalJugadores = 0
SumaEdades = 0
SumaEstaturas = 0


# Registro de integrantes del grupo
while TotalJugadores < Cupos:

    print("\n-- REGISTRO DE JUGADOR ---")

    Nombre = input("Ingresa tu nombre completo: ")
    Edad = int(input("Ingresa tu edad: "))
    Estatura = float(input("Ingresa tu estatura en metros: "))
    Experiencia = int(input("Ingresa tu experiencia en meses: "))

    # Verificar si es mayor o menor de edad
    if Edad < 18:
        print("\nEres menor de edad, no puedes registrarte.")

    elif Edad >= 18:

        # Recomendacion de posicion
        Posicion = "Sin posicion recomendada :c"

        # Recorrer las posiciones disponibles
        for NombrePosicion, EstaturaMinima, ExperienciaMinima in Posiciones:

            if Estatura >= EstaturaMinima and Experiencia >= ExperienciaMinima:
                Posicion = NombrePosicion
                break

        # Mostrar resultados
        print("\n--- DATOS DEL JUGADOR ---")
        print("Nombre:", Nombre)
        print("Edad:", Edad)
        print("Estatura:", Estatura, "m")
        print("Experiencia:", Experiencia, "meses")
        print("Posicion recomendada:", Posicion)

        # Acumular valores
        TotalJugadores += 1
        SumaEdades += Edad
        SumaEstaturas += Estatura

    # Preguntar si se desea registrar otro jugador
    if TotalJugadores < Cupos:
        Continuar = input("\n¿Deseas registrar otro jugador? (si/no): ")

        if Continuar.lower() != "si":
            break


# Se muestra el resumen
print("\n--- RESUMEN DEL REGISTRO DEL EQUIPO ---")
print("Total de jugadores registrados:", TotalJugadores)

if TotalJugadores > 0:

    PromedioEdad = SumaEdades / TotalJugadores
    PromedioEstatura = SumaEstaturas / TotalJugadores

    print("Promedio de edad:", round(PromedioEdad, 2), "Años")
    print("Promedio de estatura:", round(PromedioEstatura, 2), "m")

else:
    print("No se registraron jugadores.")

