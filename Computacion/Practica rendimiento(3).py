
import psutil
import matplotlib.pyplot as plt

cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent


metricas = ["CPU","RAM"]
valores = [cpu,ram]


plt.bar(metricas, valores)
plt.title("Monitoreo de recursos")
plt.ylabel("Uso(%)")
plt.ylim(0,100)

plt.show()