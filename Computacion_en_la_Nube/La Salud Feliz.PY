print("=== LA SALUD FELIZ ===")

Nombre = input("Ingresa tu nombre: ")
Edad = input("Ingresa tu edad: ")
Correo = input("Ingresa tu correo: ")
Tarjeta = input("Ingresa tu tarjeta de crédito: ")
Historial = input("Ingresa tu historial médico: ")

print("\n--- DATOS ORIGINALES ---")
print("Nombre:", Nombre)
print("Edad:", Edad)
print("Correo:", Correo)
print("Tarjeta:", Tarjeta)
print("Historial médico:", Historial)

print("\n--- ANONIMIZACIÓN ---")
print("Nombre: ANÓNIMO")
print("Correo: ANÓNIMO")
print("Tarjeta: ANÓNIMO")

print("\n--- PSEUDONIMIZACIÓN ---")
print("Identificador del usuario: USR001")

print("\n--- ENMASCARAMIENTO ---")
print("Tarjeta: **** **** ****", Tarjeta[-4:])

print("\n--- MINIMIZACIÓN DE DATOS ---")
print("Datos necesarios para la aplicación:")
print("Edad:", Edad)

print("\n--- LIMITACIÓN DEL PLAZO DE CONSERVACIÓN ---")
print("Los datos serán eliminados después de 30 días.")

print("\n=== PROTECCIÓN DE DATOS COMPLETADA ===")