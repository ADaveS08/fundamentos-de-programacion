# Nombre: Adam Dave Arellano Dompínguez.
# Fecha: 04 de Septiembre del 2026
# Descripción: Este programa hace una tabla de pitagoras donde puedes consultar el resultado de una multiplicacion entre dos numeros, un numero correspondiente a filas y otro de columnas


tabla = []

for f in range(1, 11):
    fila = []

    # "c" de columna
    for c in range(1, 11):
        valor = f * c
        fila.append(valor)

    tabla.append(fila)


# Esta función no regresa valor
def imprimir_tabla(tabla):
    for fila in tabla:
        for valor in fila:
            print(valor, end="\t")
        print()


# Esta función sí regresa valor
def consultar_producto(tabla, renglon, columna):
    producto = tabla[renglon - 1][columna - 1]
    return producto


imprimir_tabla(tabla)

print()

renglon = int(input("Ingresa un numero de fila en rango del 1 al 10: "))
columna = int(input("Ingresa un numero de columna en un rango del 1 al 10: "))

if 1 <= renglon <= 10 and 1 <= columna <= 10:
    producto = consultar_producto(tabla, renglon, columna)
    print("El resultado de la multiplicación es:", producto)
