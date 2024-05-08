from collections import deque
import time
from datetime import datetime
import tkinter as tk
import threading
import time

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
lock_procesos = threading.Lock()

def detener_todos():
    global ejecutar_fifo, ejecutar_sfj, ejecutar_prioridades, ejecutar_roundrobin
    ejecutar_fifo = False
    ejecutar_sfj = False
    ejecutar_prioridades = False
    ejecutar_roundrobin = False

def agregarProceso(proceso):
    procesos.append(proceso)


def fifo():
    global ejecutar_fifo
    ejecutar_fifo = True
    while ejecutar_fifo:
        lock_procesos.acquire()
        if procesos:
            proceso_actual = procesos.pop(0)
            lock_procesos.release()
            
            hora_entrada = datetime.now().strftime("%H:%M:%S")
            
            print("Entrada:", hora_entrada, "- Prioridad:", proceso_actual.prioridad, "- Tiempo de ejecucion:", proceso_actual.tiempo_ejecucion, "- Ejecutando:", proceso_actual.nombre)
        
            time.sleep(proceso_actual.tiempo_ejecucion / 4) 
            
            hora_salida = datetime.now().strftime("%H:%M:%S")
            
            print(" Salida:", hora_salida, "- Prioridad:", proceso_actual.prioridad, "- Tiempo de ejecucion:", proceso_actual.tiempo_ejecucion, "- Proceso", proceso_actual.nombre, "finalizado")
        else:
            lock_procesos.release()
            time.sleep(1)

def sfj():
    global ejecutar_sfj
    ejecutar_sfj = True
    while ejecutar_sfj:
        lock_procesos.acquire()
        if procesos:
            procesos.sort(key=lambda x: x.tiempo_ejecucion)
            proceso_actual = procesos.pop(0)
            lock_procesos.release()

            hora_entrada = datetime.now().strftime("%H:%M:%S")
        
            print("Entrada:", hora_entrada, "- Prioridad:", proceso_actual.prioridad, "- Tiempo de ejecucion:", proceso_actual.tiempo_ejecucion, "- Ejecutando:", proceso_actual.nombre)

            time.sleep(proceso_actual.tiempo_ejecucion/4)

            hora_salida = datetime.now().strftime("%H:%M:%S")

            print(" Salida:", hora_salida, "- Prioridad:", proceso_actual.prioridad, "- Tiempo de ejecucion:", proceso_actual.tiempo_ejecucion, "- Proceso", proceso_actual.nombre, "finalizado")
        else:
            lock_procesos.release()
            time.sleep(1)

def prioridades():
    global ejecutar_prioridades
    ejecutar_prioridades = True
    while ejecutar_prioridades:
        lock_procesos.acquire()
        if procesos:
            procesos.sort(key=lambda x: x.prioridad)
            proceso_actual = procesos.pop(0)
            lock_procesos.release()

            hora_entrada = datetime.now().strftime("%H:%M:%S")
        
            print("Entrada:", hora_entrada, "- Prioridad:", proceso_actual.prioridad, "- Tiempo de ejecucion:", proceso_actual.tiempo_ejecucion, "- Ejecutando:", proceso_actual.nombre)

            time.sleep(proceso_actual.tiempo_ejecucion / 4)

            hora_salida = datetime.now().strftime("%H:%M:%S")

            print(" Salida:", hora_salida, "- Prioridad:", proceso_actual.prioridad, "- Tiempo de ejecucion:", proceso_actual.tiempo_ejecucion, "- Proceso", proceso_actual.nombre, "finalizado")
        else:
            lock_procesos.release()
            time.sleep(1)

def roundrobin():
    tiempo_max = 3
    global ejecutar_roundrobin
    ejecutar_roundrobin = True
    while ejecutar_roundrobin:
        lock_procesos.acquire()
        if procesos:
            proceso_actual = procesos.pop(0)
            lock_procesos.release()

            hora_entrada = datetime.now().strftime("%H:%M:%S")

            tiempo_ejecutado = min(tiempo_max, proceso_actual.tiempo_ejecucion)
            proceso_actual.tiempo_ejecucion -= tiempo_ejecutado

            time.sleep(tiempo_ejecutado / 4)

            if proceso_actual.tiempo_ejecucion > 0:
                lock_procesos.acquire()
                procesos.append(proceso_actual)
                lock_procesos.release()

            hora_salida = datetime.now().strftime("%H:%M:%S")

            print("Entrada:", hora_entrada, "- Salida:", hora_salida, "- Tiempo de ejecucion:", tiempo_ejecutado, "- Tiempo restante:", proceso_actual.tiempo_ejecucion, "- Ejecutando:", proceso_actual.nombre, )
        else:
            lock_procesos.release()
            time.sleep(1)

def interfaz():
    root = tk.Tk()
    root.title("Algoritmos de planificacion de procesos")
    root.geometry("825x500")

    btnFifo = tk.Button(root, text="Ejecutar FIFO", command=lambda: detener_todos() or threading.Thread(target=fifo).start())
    btnSfj = tk.Button(root, text="Ejecutar SFJ", command=lambda: detener_todos() or threading.Thread(target=sfj).start())
    btnPrioridades = tk.Button(root, text="Ejecutar Prioridades", command=lambda: detener_todos() or threading.Thread(target=prioridades).start())
    btnRoundRobin = tk.Button(root, text="Ejecutar RoundRobin", command=lambda: detener_todos() or threading.Thread(target=roundrobin).start())

    btnFifo.place(x=5, y=5, width=200, height=40)
    btnFifo.config(background="blue")
    btnSfj.place(x=210, y=5, width=200, height=40)
    btnSfj.config(background="blue")
    btnPrioridades.place(x=415, y=5, width=200, height=40)
    btnPrioridades.config(background="blue")
    btnRoundRobin.place(x=620, y=5, width=200, height=40)
    btnRoundRobin.config(background="blue")

    lblNombre = tk.Label(root, text="Nombre del proceso")
    txtNombre = tk.Entry(root)
    lblNombre.place(x=5, y=100)
    txtNombre.place(x=250, y=100, width=400)

    lblTiempo = tk.Label(root, text="Tiempo de ejecucion del proceso")
    txtTiempo = tk.Entry(root)
    lblTiempo.place(x=5, y=150)
    txtTiempo.place(x=250, y=150, width=400)

    lblPrioridad = tk.Label(root, text="Prioridad del proceso")
    txtPrioridad = tk.Entry(root)
    lblPrioridad.place(x=5, y=200)
    txtPrioridad.place(x=250, y=200, width=400)

    def agregar_proceso_desde_entrada():
        nombre = txtNombre.get()
        prioridad = int(txtPrioridad.get())
        tiempo = int(txtTiempo.get())
        agregarProceso(Proceso(nombre, prioridad, tiempo))

    btnAgregar = tk.Button(root, text="Agregar proceso", command=agregar_proceso_desde_entrada)
    btnAgregar.place(x=380, y=300, width=150, height=40)


    root.mainloop()


interfaz()