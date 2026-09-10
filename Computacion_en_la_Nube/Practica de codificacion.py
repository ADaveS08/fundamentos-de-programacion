palabra = "Adam"

valoras_ascii = [ord(caracter)for caracter in palabra]

valores_codificados = [numero + 3 for numero in valoras_ascii]

letras_codificadas = [chr(numero)for numero in valores_codificados]

palabra_encriptada = "".join(letras_codificadas)

print("Original:", valoras_ascii, "->", palabra)
print("Codificado (+3):", valores_codificados, "->", palabra_encriptada)    