# Nombre: Adam Dave Arellano Dompínguez
# Fecha: 04 de Septiembre del 2026
# Descripción: Este programa hace una tabla de pitagoras donde puedes consultar el resultado de una multiplicacion entre dos numeros, un numero correspondiente a filas y otro de columnas


tabla = []

# "f" de fila
for f in range(1, 11):
    fila = []

    # "c" de columna
    for c in range(1, 11):
        valor = f * c
        fila.append(valor)
    tabla.append(fila)

# Esta no regresa valores
def imprimir_tabla(tabla):
    for fila in tabla:
        print("\t".join(str(valor) for valor in fila))


# Esta funcion si regresa vaor
def consultar_producto(tabla, renglon, columna):
    producto = tabla[renglon - 1][columna - 1]
    return producto

print()

imprimir_tabla(tabla)

print()

renglon = int(input("(Fila) Ingresa un numero en un rango del 1 al 10: "))
columna = int(input("(Columna) Ingresa otro número en un rango del 1 al 10: "))

if 1 <= renglon <= 10 and 1 <= columna <= 10:
    producto = consultar_producto(tabla, renglon, columna)
    print("El producto es:", producto)
else:
    print("Error: el renglón y la columna deben estar entre 1 y 10.")