from tkinter import *
from tkinter.font import BOLD, Font
from tkinter import filedialog
from tkinter import ttk

ventana = Tk()
ventana.geometry("500x500")
ventana.title("From Data to Species")
ventana.configure(bg='green')

def abrir_archivo():
  archivo = filedialog.askopenfilename(title="Abrir Archivo", initialdir = "C:/", filetypes = (("Archivos jpg", "*.jpg"), ("Archivos png", "*.png"), ("Archivos jpeg", "*.jpeg")))
  print(archivo)

def leer_link():
  ola = link.get()
  print(ola)

fuente = Font(family="Roboto Cn", size=14)

fuentetitulo = Font(family="Roboto Cn", size=18, weight= "bold")

titulolbl = Label(ventana, text = "From Data to Species",font = fuentetitulo )
titulolbl.pack()

instruc = Label(ventana, text = "Ingrese una foto para analizar el tipo de planta de la foto", font = fuente)
instruc.pack()

# Crear caja de texto.
link = ttk.Entry(width=50)
# Posicionarla en la ventana.
link.place(x=50, y=100)

botonlink = Button(ventana, text ="Ingresar link", command= leer_link)
botonlink.place(x=80, y=125)

botonarchivo = Button(ventana, text="Abrir Archivo", command = abrir_archivo)
botonarchivo.pack()

ventana.mainloop()
