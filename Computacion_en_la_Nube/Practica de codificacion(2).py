# Práctica: Cifra de Vigenère
while True:

    # Creamos una variable de texto llamada "palabra"
    # y le asignamos el valor "Hola"

    palabra = input("Coloca la palabra: ")


    # Recorremos cada letra de la palabra y convertimos
    # cada una a su número ASCII usando ord()
    valores_ascii = [ord(caracter) for caracter in palabra]


    # Creamos una nueva lista donde a cada número ASCII
    # le sumamos 3 unidades para codificarlo
    valores_codificados = [numero + 3 for numero in valores_ascii]


    # Recorremos la lista de números alterados y usamos chr()
    # para transformar cada número de vuelta a una letra
    letras_codificadas = [chr(numero) for numero in valores_codificados]


    # Unimos todas las letras individuales de la lista
    # en un solo texto continuo utilizando un separador vacío
    palabra_encriptada = "".join(letras_codificadas)


    # Mostramos la lista de números ASCII originales
    # y la palabra original
    print("Original:", valores_ascii, "->", palabra)


    # Mostramos la lista de números modificados
    # y la nueva palabra encriptada
    print("Codificado (+3):", valores_codificados, "->", palabra_encriptada)
    break

if not palabra == "adam":
    print("Palabra o número incorrecto")


