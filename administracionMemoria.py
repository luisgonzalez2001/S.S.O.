import re
import itertools
from copy import deepcopy

class BloqueMemoria:
    def __init__(self, size, id_archivo = None):
        self.size = size
        self.id_archivo = id_archivo

class Memoria:
    def __init__(self, size):
        self.bloques = []
        for bloque in size:
            self.bloques.append(BloqueMemoria(bloque))
        self.ultimo_asignado = 0
        #self.bloques = [BloqueMemoria(size)]

    def agregarBloque(self, bloque, posicion):
        if (posicion == "1"):
            self.bloques.append(bloque)
        else:
            self.bloques.insert(0, bloque)

    def primerAjuste(self, id_archivo, size):
        for block in self.bloques:
            if block.id_archivo is None and block.size >= size:
                if block.size > size:
                    restante = block.size - size
                    block.size = size
                    self.bloques.insert(self.bloques.index(block) + 1, BloqueMemoria(restante))
                block.id_archivo = id_archivo
                return True
        return False

    def mejorAjuste(self, id_archivo, size):
        mejor_ajuste = None
        for block in self.bloques:
            if block.id_archivo is None and block.size >= size:
                if mejor_ajuste is None or block.size < mejor_ajuste.size:
                    mejor_ajuste = block
        if mejor_ajuste is not None:
            if mejor_ajuste.size > size:
                restante = mejor_ajuste.size - size
                mejor_ajuste.size = size
                self.bloques.insert(self.bloques.index(mejor_ajuste) + 1, BloqueMemoria(restante))
            mejor_ajuste.id_archivo = id_archivo
            return True
        return False
    
    def siguienteAjuste(self, id_archivo, size):
        for i in itertools.chain(range(self.ultimo_asignado, len(self.bloques)), range(0, self.ultimo_asignado)):
            block = self.bloques[i]
            if block.id_archivo is None and block.size >= size:
                if block.size > size:
                    restante = block.size - size
                    block.size = size
                    self.bloques.insert(i + 1, BloqueMemoria(restante))
                block.id_archivo = id_archivo
                self.ultimo_asignado = i
                return True
        return False
    
    def peorAjuste(self, id_archivo, size):
        peor_ajuste = None
        for block in self.bloques:
            if block.id_archivo is None and block.size >= size:
                if peor_ajuste is None or block.size > peor_ajuste.size:
                    peor_ajuste = block
        if peor_ajuste is not None:
            if peor_ajuste.size > size:
                restante = peor_ajuste.size - size
                peor_ajuste.size = size
                self.bloques.insert(self.bloques.index(peor_ajuste) + 1, BloqueMemoria(restante))
            peor_ajuste.id_archivo = id_archivo
            return True
        return False

    def desasignar(self, id_archivo):
        for block in self.bloques:
            if block.id_archivo == id_archivo:
                block.id_archivo = None
                self.merge()
                return True
        return False

    def merge(self):
        i = 0
        while i < len(self.bloques) - 1:
            if self.bloques[i].id_archivo is None and self.bloques[i+1].id_archivo is None:
                self.bloques[i].size += self.bloques[i+1].size
                del self.bloques[i+1]
            else:
                i += 1

    def imprimir_memoria(self):
        for i, block in enumerate(self.bloques):
            print(f"Bloque {i+1}: Tamaño {block.size}, Archivo: {block.id_archivo if block.id_archivo else 'Libre'}")

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as file:
        for line in file:
            yield re.split(',\s*', line.strip())

procesos = []
bloques = [1000,400,1800,700,900,1200,1500]
mem = Memoria(bloques)
for id_archivo, size in leer_archivo('processes.txt'):
    size = int(size.replace('kb', ''))
    procesos.append((id_archivo, size))

while True:
    print("\nSelecciona alguna de las siguientes opciones:")
    print("1)Agregar bloque de memoria")
    print("2)Agregar nuevos archivos")
    print("3)Primer Ajuste")
    print("4)Mejor Ajuste")
    print("5)Siguiente Ajuste")
    print("6)Peor Ajuste")
    print("0)Salir")

    opc = int(input())

    if(opc == 1):
        size = int(input("Define el tamaño en Kbs: "))
        estatus = input("0)Disponible. o 1)Ocupado: ")
        posicion = input("0)Al inicio. o 1)Al final: ")
            
        if (estatus == "1"):
            nombre = input("Define el nombre para el bloque ocupado: ")
            bloque = BloqueMemoria(size, nombre)
            
        else:
            bloque = BloqueMemoria(size)

        mem.agregarBloque(bloque, posicion)

    elif(opc == 2):
        mood = bool(input("0)Agregar archivos fisicos. O 1)Agregar archivos virtuales: "))

        if mood:
            size = int(input("Define el tamaño en Kbs: "))
            id_archivo = input("Define el nombre del archivo: ")
            posicion = bool(input("0)Al inicio. O 1)Al final: "))

            if (posicion == "1"):
                procesos.append((id_archivo, size))
            else:
                procesos.insert(0, ((id_archivo, size)))

    elif(opc == 3):
        memAux = deepcopy(mem)
        for id_archivo, size in procesos:
            memAux.primerAjuste(id_archivo, size)
        print("\n************PRIMER AJUSTE***************")
        memAux.imprimir_memoria()

    elif(opc == 4):
        memAux = deepcopy(mem)
        for id_archivo, size in procesos:
            memAux.mejorAjuste(id_archivo, size)
        print("\n************MEJOR AJUSTE***************")
        memAux.imprimir_memoria()

    elif(opc == 5):
        memAux = deepcopy(mem)
        for id_archivo, size in procesos:
            memAux.siguienteAjuste(id_archivo, size)
        print("\n************SIGUIENTE AJUSTE***************")
        memAux.imprimir_memoria()

    elif(opc == 6):
        memAux = deepcopy(mem)
        for id_archivo, size in procesos:
            memAux.peorAjuste(id_archivo, size)
        print("\n************PEOR AJUSTE***************")
        memAux.imprimir_memoria()

    elif(opc == 0):
        break
    
    else:
        print("Entrada incorrecta")

