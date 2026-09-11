# Una **tupla** es una secuencia ordenada e **inmutable** de elementos en Python
# A diferencia de las listas, una vez creada una tupla no se pueden agregar, eliminar ni modificar sus elementos. 
# Se define con paréntesis `()`.


numeros = (10, 20, 30, 40, 50)
frutas = ("manzana", "plátano", "cereza")
datos = ("Adam", 20, 1.65, True)



lista = (1)

print(type(numeros))

#############################################################


numeros = (2, 6, 8, 10, 6, 2, 1)
lista_de_num = list(numeros)


lista_de_num.sort()

#############################################################

# Empaquetado: varios valores se agrupan en una tupla
punto = (3, 5)

# Desempaquetado: cada elemento se asigna a una variable
x, y = punto
print(x)  # 3
print(y)  # 5

# Desempaquetado directo de la tupla
a, b, c = (7, 8, 9)
print(a, b, c)  # 7 8 9