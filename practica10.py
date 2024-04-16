import threading
import time
import random
import tkinter as tk

class Estacionamiento:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.estacionamiento = []
        self.frecuencia_entrada = 1
        self.frecuencia_salida = 1

    def añadir_auto(self):
        while True:
            if len(self.estacionamiento) < self.capacidad:
                self.estacionamiento.append('auto')
                print('Auto añadido. Autos en el estacionamiento: ', len(self.estacionamiento))
            time.sleep(self.frecuencia_entrada)

    def retirar_auto(self):
        while True:
            if self.estacionamiento:
                self.estacionamiento.pop()
                print('Auto retirado. Autos en el estacionamiento: ', len(self.estacionamiento))
            time.sleep(self.frecuencia_salida)

def actualizar_frecuencias():
    estacionamiento.frecuencia_entrada = float(entrada.get())
    estacionamiento.frecuencia_salida = float(salida.get())

estacionamiento = Estacionamiento(12)

thread_añadir = threading.Thread(target=estacionamiento.añadir_auto)
thread_retirar = threading.Thread(target=estacionamiento.retirar_auto)

thread_añadir.start()
thread_retirar.start()

root = tk.Tk()

entrada = tk.Entry(root)
entrada.pack()
entrada.insert(0, "1")

salida = tk.Entry(root)
salida.pack()
salida.insert(0, "1")

boton = tk.Button(root, text="Actualizar frecuencias", command=actualizar_frecuencias)
boton.pack()

root.mainloop()
