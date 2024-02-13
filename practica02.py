import os
import random
import string
import shutil

def copiar_carpeta(carpeta_origen, carpeta_destino):
    if os.path.exists(carpeta_destino):
        print("La carpeta de destino ya existe. Por favor, elija otro nombre.")
        return

    shutil.copytree(carpeta_origen, carpeta_destino)
    print("Carpeta copiada exitosamente.")

def cambiar_contenido(archivo):
    with open(archivo, 'r+') as file:
        contenido = file.read()
        contenido_modificado = ''

        for char in contenido:
            if char.isalpha():
                contenido_modificado += str(random.randint(0, 9))
            elif char.isdigit():
                contenido_modificado += random.choice(string.ascii_uppercase)
            else:
                contenido_modificado += char

        file.seek(0)
        file.write(contenido_modificado)
        file.truncate()

def modificar_archivos_en_carpeta(carpeta):
    for root, _, files in os.walk(carpeta):
        for file_name in files:
            archivo = os.path.join(root, file_name)
            cambiar_contenido(archivo)
    print("Contenido de los archivos modificado exitosamente.")

carpeta_origen = "/home/dev_luis/Documentos/Universidad/S_SO/Prueba"
carpeta_destino = "/home/dev_luis/Documentos/Universidad/S_SO/Prueba_copia"

copiar_carpeta(carpeta_origen, carpeta_destino)

modificar_archivos_en_carpeta(carpeta_destino)
