import tkinter as tk
from tkinter import scrolledtext
import threading
import time

sem = threading.Semaphore()
rw_mutex = threading.Semaphore()
read_count = 0

def leer(textbox):
    sem.acquire()
    textbox.config(state="normal")
    textbox.delete("1.0", tk.END)
    global read_count
    read_count += 1
    if read_count == 1:
        rw_mutex.acquire()
    sem.release()

    with open('archivo.txt', 'r') as f:
        texto = f.read()
        for palabra in texto.split():
            textbox.insert(tk.END, palabra + ' ')
            textbox.update()
            time.sleep(0.1)

    sem.acquire()
    read_count -= 1
    if read_count == 0:
        rw_mutex.release()
    textbox.config(state="disabled")
    sem.release()

def editar(textbox):
    rw_mutex.acquire()
    textbox.config(state="normal")

def guardar(textbox):
    with open('archivo.txt', 'w') as f:
        f.write(textbox.get("1.0", tk.END))
    textbox.config(state="disabled")
    rw_mutex.release()

def crear_interfaz():

    root = tk.Tk()
    root.title("Lector-Escritor")
    root.geometry("1350x600")

    frame1 = tk.Frame(root, width=400, height=470, background="yellow")
    frame2 = tk.Frame(root, width=400, height=470, background="yellow")
    frame3 = tk.Frame(root, width=400, height=470, background="yellow")

    frame1.place(x=45, y=20)
    frame2.place(x=470, y=20)
    frame3.place(x=895, y=20)

    textbox1 = scrolledtext.ScrolledText(frame1)
    textbox1.place(x=10, y=10, width=380, height=360)
    btnLeer1 = tk.Button(frame1, text="Leer", command=lambda: threading.Thread(target=leer, args=(textbox1,)).start())
    btnLeer1.place(x=10, y=400, width=120, height=50)
    btnEditar1 = tk.Button(frame1, text="Editar", command=lambda: threading.Thread(target=editar, args=(textbox1,)).start())
    btnEditar1.place(x=140, y=400, width=120, height=50)
    btnGuardar1 = tk.Button(frame1, text="Guardar", command=lambda: threading.Thread(target=guardar, args=(textbox1,)).start())
    btnGuardar1.place(x=270, y=400, width=120, height=50)
    btnEditar1.config(background="green")
    btnLeer1.config(background="green")
    btnGuardar1.config(background="green")
    textbox1.config(state="disabled")


    textbox2 = scrolledtext.ScrolledText(frame2)
    textbox2.place(x=10, y=10, width=380, height=360)
    btnLeer2 = tk.Button(frame2, text="Leer", command=lambda: threading.Thread(target=leer, args=(textbox2,)).start())
    btnLeer2.place(x=10, y=400, width=120, height=50)
    btnEditar2 = tk.Button(frame2, text="Editar", command=lambda: threading.Thread(target=editar, args=(textbox2,)).start())
    btnEditar2.place(x=140, y=400, width=120, height=50)
    btnGuardar2 = tk.Button(frame2, text="Guardar", command=lambda: threading.Thread(target=guardar, args=(textbox2,)).start())
    btnGuardar2.place(x=270, y=400, width=120, height=50)
    btnEditar2.config(background="green")
    btnLeer2.config(background="green")
    btnGuardar2.config(background="green")

    textbox3 = scrolledtext.ScrolledText(frame3)
    textbox3.place(x=10, y=10, width=380, height=360)
    btnLeer3 = tk.Button(frame3, text="Leer", command=lambda: threading.Thread(target=leer, args=(textbox3,)).start())
    btnLeer3.place(x=10, y=400, width=120, height=50)
    btnEditar3 = tk.Button(frame3, text="Editar", command=lambda: threading.Thread(target=editar, args=(textbox3,)).start())
    btnEditar3.place(x=140, y=400, width=120, height=50)
    btnGuardar3 = tk.Button(frame3, text="Guardar", command=lambda: threading.Thread(target=guardar, args=(textbox3,)).start())
    btnGuardar3.place(x=270, y=400, width=120, height=50)
    btnEditar3.config(background="green")
    btnLeer3.config(background="green")
    btnGuardar3.config(background="green")

    root.mainloop()

crear_interfaz()
