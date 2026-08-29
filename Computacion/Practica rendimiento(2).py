import requests

url = "https://www.google.com"

try:
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        print(" :D  Sitio disponible")
    else:
        print(f"Estado: {respuesta.status_code}")

except Exception as e:
    print("Error:", e)