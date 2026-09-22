import requests

url = "https://pokeapi.co/api/v2/pokemon/volcanion"

respuesta = requests.get(url)

datos = respuesta.json()
#print("===---POKEDEX---===")

#print("Abilidades:", datos["abilities"])
#print("Nombre:", datos["name"])
#print("Altura:", datos["height"])
#print("Peso:", datos["weight"])


import requests
url = "https://wttr.in/Queretaro?format=j1"

respuesta = requests.get(url)

datos = respuesta.json()
temperatura = datos["current_condition"][0]["temp_C"]

print("---QUERÉTARO, Querétaro---")
print("Temperatura actual:", temperatura, "C")
