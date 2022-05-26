from operator import length_hint
from tkinter import *
from tkinter.font import BOLD, Font
from tkinter import filedialog
from tkinter import ttk
from turtle import color
from PIL import Image
from analisis import Proceso
from listas import *

class VentanaCantidad:

    def __init__(self):
        self.ventana_eleccion = Tk()
        self.fuente = Font(family="Roboto Cn", size=14)
        self.fuente2 = Font(family = "Roboto Cn", size=12)
        self.fuentetitulo = Font(family="Roboto Cn", size=18, weight= "bold")
        self.definir_ventana()        

    def run(self):
        self.ventana_eleccion.mainloop()

    def definir_ventana(self):
        self.ventana_eleccion.geometry("300x300")
        self.ventana_eleccion.title("From Data to Species")
        self.ventana_eleccion.configure(bg='green')

        titulolbl = Label(self.ventana_eleccion, text = "From Data to Species",font = self.fuentetitulo, bg='green' )
        titulolbl.pack()

        instruc = Label(self.ventana_eleccion, text = "Cantidad de fotos", font = self.fuente, bg='green')
        instruc.pack()

        boton_1=Button(text="1", command = self.num1, width=10)
        boton_1.place(x=110, y=70)

        boton_2=Button(text="2", command = self.num2, width=10)
        boton_2.place(x=110, y=110)

        boton_3=Button(text="3", command = self.num3, width=10)
        boton_3.place(x=110,y=150)

        boton_4=Button(text="4", command = self.num4, width=10)
        boton_4.place(x=110, y=190)

        boton_5=Button(text="5", command = self.num5, width=10)
        boton_5.place(x=110, y=230)
    
    def num1(self):
        num_fotos = 1
        self.ventana_eleccion.destroy()
        VentanaEjecucion(num_fotos)
        
    def num2(self):
        num_fotos = 2
        self.ventana_eleccion.destroy()
        VentanaEjecucion(num_fotos)
        
    def num3(self):
        num_fotos = 3
        self.ventana_eleccion.destroy()
        VentanaEjecucion(num_fotos)
        
    def num4(self):
        num_fotos = 4
        self.ventana_eleccion.destroy()
        VentanaEjecucion(num_fotos)
        
    def num5(self):
        num_fotos = 5
        self.ventana_eleccion.destroy()
        VentanaEjecucion(num_fotos)


class VentanaEjecucion:
    def __init__(self, num_fotos):
        self.num_fotos = num_fotos
        self.cont = 0
        self.ventana = Tk()
        self.fuente = Font(family="Roboto Cn", size=14)
        self.fuente2 = Font(family = "Roboto Cn", size=12)
        self.fuentetitulo = Font(family="Roboto Cn", size=18, weight= "bold")
        self.definir_ventana_ejecucion()

    def run(self):
        self.ventana.mainloop()

    def definir_ventana_ejecucion(self):
        self.ventana.geometry("500x500")
        self.ventana.title("From Data to Species")
        self.ventana.configure(bg='green')

        titulolbl = Label(self.ventana, text = "From Data to Species",font = self.fuentetitulo, bg='green')
        titulolbl.pack()

        instruc = Label(self.ventana, text = "Ingrese una foto para analizar el tipo de planta de la foto", font = self.fuente, bg='green')
        instruc.pack()

        self.link_entrada = Entry(self.ventana, width=70)
        self.link_entrada.pack()

        otraopcion = Label(self.ventana, text = "Otra opción", font = self.fuente, bg='green')
        otraopcion.place(x=200, y=100)

        botonarchivo = Button(self.ventana, text="Abrir Archivo", command = lambda: self.abrir_archivo())
        botonarchivo.place(x=210, y=140)

        parte_label = Label(self.ventana, text = "Escriba la parte de la plante en específico de la que va a ingresar foto", font = self.fuente2, bg = 'green')
        parte_label.place(x=10, y=180)

        self.parte_planta = Entry(self.ventana, width=40)
        self.parte_planta.place(x=130, y=210)  

        botonlink = Button(self.ventana, text ="Ingresar", command=lambda: self.leer_link(), width=12)
        botonlink.place(x=200, y=290)

        self.contadorlabel = Label(self.ventana, text = "Fotos ingresadas: "+ str(self.cont) , font = self.fuente2, bg = 'green')
        self.contadorlabel.place(x=10, y=400)

        self.infolabel = Label(self.ventana, text = "Info", font = self.fuente2, bg ='green')
        self.infolabel.place(x=60, y= 350)

        cerrar = Button(self.ventana, text="Cerrar", command=self.closewindow)
        cerrar.place(x=220,y=450)

    def abrir_archivo(self):
        if(self.cont < self.num_fotos):
            if(self.parte_planta.get() != ""):
                archivo = filedialog.askopenfilename(title="Abrir Archivo", initialdir = "C:/", filetypes = (("Archivos jpg", "*.jpg"), ("Archivos png", "*.png"), ("Archivos jpeg", "*.jpeg")))
                #im = Image.open(archivo)
                #im.show()
                listaarchivo.append(archivo)
            
                parte= self.parte_planta.get()
                self.parte_planta.delete(0,END)
                self.cont = self.cont + 1
                self.contadorlabel['text'] = "Fotos ingresadas: "+ str(self.cont)
                listaparte.append(parte)
                if(self.cont == self.num_fotos):
                    Proceso.hacer(self.num_fotos)
            else:
                self.infolabel['text'] = "Debe ingresar la parte de la planta"
        else:
            self.infolabel['text'] = "No puede ingresar mas fotos"
            
            

    def leer_link(self):
        if(self.cont < self.num_fotos):
            if(self.link_entrada.get() != "" and self.parte_planta.get() != ""):
                
                link= self.link_entrada.get()
                self.link_entrada.delete(0,END)
                print(link)
                listaarchivo.append(link)

                parte= self.parte_planta.get()
                self.parte_planta.delete(0,END)
                print(parte)
                self.cont = self.cont+1
                listaparte.append(parte)
            else:
                self.infolabel['text'] = "Asegúrese bien de llenar el link y la parte de la planta"           
        else:

            self.infolabel['text'] = "No puede ingresar mas fotos"

    def closewindow(self):
        self.ventana.destroy()

Aplicacion = VentanaCantidad()
