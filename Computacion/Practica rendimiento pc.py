
import psutil
import time

for i in range(10):
    cpu = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory().percent
    temp = psutil.cpu_count()

print(f"Temperatura: {temp}°")
print(f"CPU: {cpu}%")
print(f"Memoria RAM: {memoria}")
print("-"* 30)

time.sleep(2)