from pytube import YouTube
from tkinter import *
from tkinter import messagebox as messagebox

def descargar(formato):
    enlace = url_entry.get()
    video = YouTube(enlace)
    titulo_original = video.title

    if formato == 'mp3':
        descarga = video.streams.get_audio_only()
    elif formato == 'mp4':
        descarga = video.streams.get_highest_resolution()

    nombre_archivo = f"{titulo_original} - {formato}.{descarga.subtype}"
    descarga.download(filename=nombre_archivo)
    messagebox.showinfo("✔", f"Descarga completa: {nombre_archivo}")

def popup():
    messagebox.showinfo(":)", "Programita hecho por nurvoz")

root = Tk()
root.config(bd=15)
root.title("Script youtube")

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Más info", menu=helpmenu)
helpmenu.add_command(label="Autor", command=popup)
menubar.add_command(label="Salir", command=root.destroy)

intrucciones = Label(root, text="Introduce la URL: ")
intrucciones.grid(row=0, column=0)

url_entry = Entry(root)
url_entry.grid(row=0, column=1)

boton = Button(root, text="Descargar solo audio", command=lambda: descargar('mp3'))
boton.grid(row=2, column=0)

boton1 = Button(root, text="Descargar video", command=lambda: descargar('mp4'))
boton1.grid(row=2, column=1)

root.mainloop()
