from collections import deque
import time
from datetime import datetime
from copy import deepcopy

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
procesos = leer_procesos_desde_archivo(archivo_procesos)

def fifo():
    cola_procesos = deque()

    for proceso in procesos:
        cola_procesos.append(proceso)

    while cola_procesos:
        proceso_actual = cola_procesos.popleft()
        
        hora_entrada = datetime.now().strftime("%H:%M:%S")
        
        print("Entrada:", hora_entrada, "- Prioridad:", proceso_actual.prioridad, "- Tiempo de ejecucion:", proceso_actual.tiempo_ejecucion, "- Ejecutando:", proceso_actual.nombre)
    
        time.sleep(proceso_actual.tiempo_ejecucion/2) 
        
        hora_salida = datetime.now().strftime("%H:%M:%S")
        
        print(" Salida:", hora_salida, "- Prioridad:", proceso_actual.prioridad, "- Tiempo de ejecucion:", proceso_actual.tiempo_ejecucion, "- Proceso", proceso_actual.nombre, "finalizado")

def sfj():
    procesos.sort(key=lambda x: x.tiempo_ejecucion)

    for proceso_actual in procesos:
        hora_entrada = datetime.now().strftime("%H:%M:%S")
    
        print("Entrada:", hora_entrada, "- Prioridad:", proceso_actual.prioridad, "- Tiempo de ejecucion:", proceso_actual.tiempo_ejecucion, "- Ejecutando:", proceso_actual.nombre)

        time.sleep(proceso_actual.tiempo_ejecucion/4)  # Espera el tiempo de ejecución del proceso

        hora_salida = datetime.now().strftime("%H:%M:%S")

        print(" Salida:", hora_salida, "- Prioridad:", proceso_actual.prioridad, "- Tiempo de ejecucion:", proceso_actual.tiempo_ejecucion, "- Proceso", proceso_actual.nombre, "finalizado")

def prioridades():
    procesos.sort(key=lambda x: x.prioridad)

    for proceso_actual in procesos:
        hora_entrada = datetime.now().strftime("%H:%M:%S")
    
        print("Entrada:", hora_entrada, "- Prioridad:", proceso_actual.prioridad, "- Tiempo de ejecucion:", proceso_actual.tiempo_ejecucion, "- Ejecutando:", proceso_actual.nombre)

        time.sleep(proceso_actual.tiempo_ejecucion / 4)   # Espera el tiempo de ejecución del proceso

        hora_salida = datetime.now().strftime("%H:%M:%S")

        print(" Salida:", hora_salida, "- Prioridad:", proceso_actual.prioridad, "- Tiempo de ejecucion:", proceso_actual.tiempo_ejecucion, "- Proceso", proceso_actual.nombre, "finalizado")

def roundrobin():
    cola_procesos = deque()

    procesos_aux = deepcopy(procesos)

    for proceso in procesos_aux:
        cola_procesos.append(proceso)

    tiempo_max = 3

    while cola_procesos:
        proceso_actual = cola_procesos.popleft()

        hora_entrada = datetime.now().strftime("%H:%M:%S")

        tiempo_ejecutado = min(tiempo_max, proceso_actual.tiempo_ejecucion)
        proceso_actual.tiempo_ejecucion -= tiempo_ejecutado

        time.sleep(tiempo_ejecutado / 2)

        if proceso_actual.tiempo_ejecucion > 0:
            cola_procesos.append(proceso_actual)

        hora_salida = datetime.now().strftime("%H:%M:%S")

        print("Entrada:", hora_entrada, "- Salida:", hora_salida, "- Tiempo de ejecucion:", tiempo_ejecutado, "- Tiempo restante:", proceso_actual.tiempo_ejecucion, "- Ejecutando:", proceso_actual.nombre, )

opc = 1

while opc != 0:
    print("Procesos cargados desde archivo:")
    for proceso_actual in procesos:
        print(proceso_actual.prioridad, proceso_actual.tiempo_ejecucion, proceso_actual.nombre)

    print("\n\nSelecciona alguna de las siguientes opciones:")
    print("1)FIFO")
    print("2)SFJ")
    print("3)Prioridades")
    print("4)RoundRobin")
    print("5)Agregar proceso al inicio")
    print("6)Agregar proceso al final")
    print("0)Salir")

    opc = int(input())

    if(opc == 1):
        fifo()
    elif(opc == 2):
        sfj()
    elif(opc == 3):
        prioridades()
    elif(opc == 4):
        roundrobin()
    elif(opc == 5):
        nombre = input("Nombre del proceso: " )
        prioridad = input("Prioridad del proceso: ")
        tiempo = input("Tiempo de ejecucion del proceso: ")

        procesos.insert(0, Proceso(nombre, int(prioridad), int(tiempo)))
    elif(opc == 6):
        nombre = input("Nombre del proceso: " )
        prioridad = input("Prioridad del proceso: ")
        tiempo = input("Tiempo de ejecucion del proceso: ")

        procesos.append(Proceso(nombre, int(prioridad), int(tiempo)))
    elif(opc == 0):
        break
    else:
        print("Entrada incorrecta")