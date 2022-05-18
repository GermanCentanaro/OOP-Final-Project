from operator import length_hint
from tkinter import *
from tkinter.font import BOLD, Font
from tkinter import filedialog
from tkinter import ttk
from turtle import color
from PIL import Image

ventana_eleccion = Tk()
ventana_eleccion.geometry("300x300")
ventana_eleccion.title("From Data to Species")
ventana_eleccion.configure(bg='green')

def nueva_ventana(num_fotos):
  cont=0

  ventana = Toplevel(ventana_eleccion)
  ventana.geometry("500x500")
  ventana.title("From Data to Species")
  ventana.configure(bg='green')

  if(num_fotos == 1):
    pass

  titulolbl = Label(ventana, text = "From Data to Species",font = fuentetitulo, bg='green')
  titulolbl.pack()

  instruc = Label(ventana, text = "Ingrese una foto para analizar el tipo de planta de la foto", font = fuente, bg='green')
  instruc.pack()

  link_entrada = Entry(ventana, width=70)
  link_entrada.pack()

  def leer_link():
    link= link_entrada.get()
    link_entrada.delete(0,END)
    print(link)

  botonlink = Button(ventana, text ="Ingresar link", command= leer_link)
  botonlink.place(x=200, y=90)

  #otraopcion = Label(ventana, text = "Otra opción", font = fuente, bg='green')
  #otraopcion.pack()

  parte_label = Label(ventana, text = "Escriba la parte de la plante en específico de la que va a ingresar foto", font = fuente, bg = 'green')
  parte_label.place(x=60, y=310)

  parte_planta = Entry(ventana, width=40)
  parte_planta.place(x=60, y=300)

  botonarchivo = Button(ventana, text="Abrir Archivo", command = abrir_archivo)
  botonarchivo.place(x=210, y=170)

  cerrar = Button(ventana, text="Cerrar", command=closewindow)
  cerrar.place(x=220,y=450)

  ventana.mainloop
  #ventana_eleccion.destroy()

def closewindow():
  ventana_eleccion.destroy()

def abrir_archivo():
  archivo = filedialog.askopenfilename(title="Abrir Archivo", initialdir = "C:/", filetypes = (("Archivos jpg", "*.jpg"), ("Archivos png", "*.png"), ("Archivos jpeg", "*.jpeg")))
  im = Image.open(archivo)
  im.show()

def num1():
  num_fotos = 1
  nueva_ventana(num_fotos)
  ventana_eleccion.withdraw()

def num2():
  num_fotos = 2
  nueva_ventana(num_fotos)
  ventana_eleccion.withdraw()

def num3():
  num_fotos = 3
  nueva_ventana(num_fotos)
  ventana_eleccion.withdraw()

def num4():
  num_fotos = 4
  nueva_ventana(num_fotos)
  ventana_eleccion.withdraw()

def num5():
  num_fotos = 5
  nueva_ventana(num_fotos)
  ventana_eleccion.withdraw()

fuente = Font(family="Roboto Cn", size=14)

fuentetitulo = Font(family="Roboto Cn", size=18, weight= "bold")

titulolbl = Label(ventana_eleccion, text = "From Data to Species",font = fuentetitulo, bg='green' )
titulolbl.pack()

instruc = Label(ventana_eleccion, text = "Cantidad de fotos", font = fuente, bg='green')
instruc.pack()

boton_1=Button(text="1", command = num1, width=10)
boton_1.place(x=110, y=70)

boton_2=Button(text="2", command = num1, width=10)
boton_2.place(x=110, y=110)

boton_3=Button(text="3", command = num1, width=10)
boton_3.place(x=110,y=150)

boton_4=Button(text="4", command = num1, width=10)
boton_4.place(x=110, y=190)

boton_5=Button(text="5", command = num1, width=10)
boton_5.place(x=110, y=230)

ventana_eleccion.mainloop()
