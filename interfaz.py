from operator import length_hint
from tkinter import *
from tkinter.font import BOLD, Font
from tkinter import filedialog
from tkinter import ttk
from turtle import color
from PIL import Image
from analisis import Proceso
from listas import *
from german import *

class VentanaInicioSesion:
    def __init__(self):
        self.ventana_inicio = Tk()
        self.fuente = Font(family="Roboto Cn", size=14)
        self.fuente2 = Font(family = "Roboto Cn", size=12)
        self.fuentetitulo = Font(family="Roboto Cn", size=18, weight= "bold")
        self.definir_ventana() 

    def definir_ventana(self):
        ancho_ventana = 300
        alto_ventana = 800

        x_ventana = self.ventana_inicio.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.ventana_inicio.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.ventana_inicio.geometry(posicion)

        self.ventana_inicio.resizable(0,0)

        self.ventana_inicio.title("From Data to Species")
        self.ventana_inicio.configure(bg='green')

        titulolbl = Label(self.ventana_inicio, text = "From Data to Species",font = self.fuentetitulo, bg='green' )
        titulolbl.pack()

        usuariolbl = Label(self.ventana_inicio, text = "Usuario:", font = self.fuente, bg='green')
        usuariolbl.pack()

        self.usuario_text = Entry(self.ventana_inicio, width = 40)
        self.usuario_text.pack()

        contraseñalbl = Label(self.ventana_inicio, text ="Contraseña:", fornt=self.fuente, bg='green')
        contraseñalbl.pack()

        self.contraseña_text = Entry(self.ventana_inicio, width=40)
        self.contraseña_text.pack()

        self.infolbl = Label(self.ventana_inicio, text = "", font=self.fuente, bg ='green')
        self.infolbl.pack()

        self.botoninicio = Button(self.ventana_inicio, text ="Iniciar sesión", command = self.iniciar )
        self.botoninicio.pack()

        reglbl = Label(self.ventana_inicio, text = "Sino tiene cuenta puede Registrarse:", font=self.fuente, bg ='green')
        reglbl.pack()

        self.regbtn = Button(self.ventana_inicio, text ="Registrarse", command = self.registro)
        self.regbtn.pack()

    def iniciar(self):
        pass

    def registro(self):
        pass

class Registro:
    def __init__(self):
        self.ventana_reg = Tk()
        self.fuente = Font(family="Roboto Cn", size=14)
        self.fuente2 = Font(family = "Roboto Cn", size=12)
        self.fuentetitulo = Font(family="Roboto Cn", size=18, weight= "bold")
        self.definir_ventana()
    
    def definir_ventana(self):
        ancho_ventana = 300
        alto_ventana = 800

        x_ventana = self.ventana_reg.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.ventana_reg.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.ventana_reg.geometry(posicion)

        self.ventana_reg.resizable(0,0)

        self.ventana_reg.title("From Data to Species")
        self.ventana_reg.configure(bg='green')

        titulolbl = Label(self.ventana_reg, text = "From Data to Species",font = self.fuentetitulo, bg='green' )
        titulolbl.pack()

        nombrelbl = Label(self.ventana_reg, text = "Nombre:", font = self.fuente, bg='green')
        nombrelbl.pack()

        self.nombre_text = Entry(self.ventana_reg, width = 40)
        self.nombre_text.pack()

        usuariolbl = Label(self.ventana_reg, text = "Usuario:", font = self.fuente, bg='green')
        usuariolbl.pack()

        self.usuario_text = Entry(self.ventana_reg, width = 40)
        self.usuario_text.pack()

        contraseñalbl = Label(self.ventana_reg, text ="Contraseña:", fornt=self.fuente, bg='green')
        contraseñalbl.pack()

        self.contraseña_text = Entry(self.ventana_reg, width=40)
        self.contraseña_text.pack()

        self.infolbl = Label(self.ventana_reg, text = "", font=self.fuente, bg ='green')
        self.infolbl.pack()

        self.regbtn = Button(self.ventana_inicio, text ="Registrarse", command = self.registro)
        self.regbtn.pack()

    def registro(self):
        pass

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
        ancho_ventana = 300
        alto_ventana = 300

        x_ventana = self.ventana_eleccion.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.ventana_eleccion.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.ventana_eleccion.geometry(posicion)

        self.ventana_eleccion.resizable(0,0)

        #self.ventana_eleccion.geometry("300x300")
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
        ancho_ventana = 510
        alto_ventana = 510

        x_ventana = self.ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.ventana.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.ventana.geometry(posicion)

        self.ventana.resizable(0,0)

        #self.ventana.geometry("510x510")
        self.ventana.title("From Data to Species")
        self.ventana.configure(bg='green')

        titulolbl = Label(self.ventana, text = "From Data to Species",font = self.fuentetitulo, bg='green')
        titulolbl.pack()

        instruc = Label(self.ventana, text = "Ingrese una foto para analizar el tipo de planta de la foto", font = self.fuente, bg='green')
        instruc.pack()

        parte_label = Label(self.ventana, text = "Seleccione la parte de la planta en específico de la que va a ingresar foto", font = self.fuente2, bg = 'green')
        parte_label.pack()

        self.lista_desplegable = ttk.Combobox(self.ventana, width=15, state='readonly')
        self.lista_desplegable.pack()
        opciones = ["Hoja", "Flor", "Fruto", "Tallo", "Otro"]
        self.lista_desplegable['values']=opciones

        botonlabel = Label(self.ventana, text = "Eliga la imagen a analizar", font = self.fuente, bg = 'green')
        botonlabel.pack()

        botonarchivo = Button(self.ventana, text="Abrir Archivo", command = lambda: self.abrir_archivo())
        botonarchivo.pack()     

        #self.parte_planta = Entry(self.ventana, width=40)
        #self.parte_planta.place(x=130, y=210)

        self.infolabel = Label(self.ventana, text = "Info", font = self.fuente2, bg ='green')
        self.infolabel.place(x=60, y= 190)

        self.contadorlabel = Label(self.ventana, text = "Fotos ingresadas: "+ str(self.cont) , font = self.fuente2, bg = 'green')
        self.contadorlabel.place(x=10, y=210)

        self.marco = ttk.Frame(self.ventana, borderwidth=2, relief="raised", padding=(10,10))
        #self.marco.config(width=480,height=320)
        self.marco.place(x=10, y =260)

        xd = Label(self.marco, text="Aquí tendrá un resultado")
        xd.pack()
       
        cerrar = Button(self.ventana, text="Cerrar", command=self.closewindow)
        cerrar.place(x=230,y=460)

    def abrir_archivo(self):
        if(self.cont < self.num_fotos):
            if(self.lista_desplegable.get() != ""):
                archivo = filedialog.askopenfilename(title="Abrir Archivo", initialdir = "C:/", filetypes = (("Archivos jpg", "*.jpg"), ("Archivos png", "*.png"), ("Archivos jpeg", "*.jpeg")))
                #im = Image.open(archivo)
                #im.show()
                if(archivo != ""):               
                    parte= self.lista_desplegable.get()
                    foto = Foto(archivo, parte)
                    listaarchivo.append(foto.path)
                    self.cont = self.cont + 1
                    self.contadorlabel['text'] = "Fotos ingresadas: "+ str(self.cont)
                    listaparte.append(foto.parte)
                    if(self.cont == self.num_fotos):
                        Proceso.hacer(self.num_fotos)
                else:
                    self.infolabel['text'] = "No fue ingresada la foto, intente de nuevo"
            else:
                self.infolabel['text'] = "Debe ingresar la parte de la planta"
        else:
            self.infolabel['text'] = "No puede ingresar mas fotos"

    def closewindow(self):
        self.ventana.destroy()

Aplicacion = VentanaCantidad()
