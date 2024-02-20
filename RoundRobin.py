from collections import deque
import time
from datetime import datetime

class Proceso:
    def __init__(self, nombre, prioridad, tiempo_ejecucion):
        self.nombre = nombre
        self.prioridad = prioridad
        self.tiempo_ejecucion = tiempo_ejecucion

def leer_procesos_desde_archivo(nombre_archivo):
    procesos = []
    with open(nombre_archivo, 'r') as file:
        for line in file:
            nombre, tiempo_ejecucion, prioridad = line.strip().split(', ')
            procesos.append(Proceso(nombre, int(prioridad), int(tiempo_ejecucion)))
    return procesos

archivo_procesos = 'procesos.txt'

cola_procesos = deque()

procesos = leer_procesos_desde_archivo(archivo_procesos)
for proceso in procesos:
    cola_procesos.append(proceso)

tiempo_max = 3

while cola_procesos:
    proceso_actual = cola_procesos.popleft()

    hora_entrada = datetime.now().strftime("%H:%M:%S")

    tiempo_ejecutado = min(tiempo_max, proceso_actual.tiempo_ejecucion)
    proceso_actual.tiempo_ejecucion -= tiempo_ejecutado

    time.sleep(tiempo_ejecutado)

    if proceso_actual.tiempo_ejecucion > 0:
        cola_procesos.append(proceso_actual)

    hora_salida = datetime.now().strftime("%H:%M:%S")

    print("Entrada:", hora_entrada, "- Salida:", hora_salida, "- Tiempo de ejecucion:", tiempo_ejecutado, "- Ejecutando:", proceso_actual.nombre, )

print("Todos los procesos han sido ejecutados.")
