from tkinter import *
from tkinter.font import BOLD, Font
from tkinter import filedialog

ventana = Tk()
ventana.geometry("500x500")
ventana.title("From Data to Species")
ventana.configure(bg='green')

def saludo():
    print("Xd")
    titulolbl.configure(text = "hola")

def abrir_archivo():
  archivo = filedialog.askopenfilename(title="Abrir Archivo", initialdir = "C:/", filetypes = (("Archivos jpg", "*.jpg"), ("Archivos png", "*.png"), ("Archivos jpeg", "*.jpeg")))
  print(archivo)

fuente = Font(family="Roboto Cn", size=14)

fuentetitulo = Font(family="Roboto Cn", size=18, weight= "bold")

titulolbl = Label(ventana, text = "From Data to Species",font = fuentetitulo )
titulolbl.pack()

instruc = Label(ventana, text = "Ingrese una foto para analizar el tipo de planta de la foto", font = fuente)
instruc.pack()

boton = Button(ventana, text = "Ingresar", command = saludo)
boton.pack()

botonarchivo = Button(ventana, text="Abrir Archivo", command = abrir_archivo)
botonarchivo.pack

ventana.mainloop()
