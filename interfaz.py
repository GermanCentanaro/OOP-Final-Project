from operator import length_hint
from tkinter import *
from tkinter.font import BOLD, Font
from tkinter import filedialog
from tkinter import ttk
from turtle import color
from PIL import Image
from analisis import *
from listas import *
from usuario import *

class VentanaInicioSesion:
    def __init__(self):
        self.ventana_inicio = Tk()
        self.fuente = Font(family="Roboto Cn", size=14)
        self.fuente2 = Font(family = "Roboto Cn", size=12)
        self.fuentetitulo = Font(family="Roboto Cn", size=18, weight= "bold")
        self.definir_ventana()

    def run(self):
        self.ventana_inicio.mainloop()

    def definir_ventana(self):
        ancho_ventana = 500
        alto_ventana = 300

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

        self.usuario_text = Entry(self.ventana_inicio, width = 50)
        self.usuario_text.pack()

        contraseñalbl = Label(self.ventana_inicio, text ="Contraseña:", font=self.fuente, bg='green')
        contraseñalbl.pack()

        self.contraseña_text = Entry(self.ventana_inicio, width=50)
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
        nombre= self.usuario_text.get()
        contraseña = self.contraseña_text.get()
        if(nombre == ""):
            self.infolbl['text'] = "Ingrese un nombre"
        elif(contraseña == ""):
            self.infolbl['text'] = "Ingrese una contraseña"
        else:
            user = Usuario(None, nombre, contraseña)
            x = user.Iniciar(nombre, contraseña)
            if(x == False):
                self.infolbl['text'] = "Usuario no registrado, vuelva a intentarlo"
            else:
                print("Ingreso realizado correctamente.\n")
                self.ventana_inicio.destroy()
                VentanaEjecucion()

    def registro(self):
        self.ventana_inicio.destroy()
        VentanaRegistrarse()

class VentanaRegistrarse:
    def __init__(self):
        self.ventana_reg = Tk()
        self.fuente = Font(family="Roboto Cn", size=14)
        self.fuente2 = Font(family = "Roboto Cn", size=12)
        self.fuentetitulo = Font(family="Roboto Cn", size=18, weight= "bold")
        self.definir_ventana()
    
    def definir_ventana(self):
        ancho_ventana = 500
        alto_ventana = 300

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

        contraseñalbl = Label(self.ventana_reg, text ="Contraseña:", font=self.fuente, bg='green')
        contraseñalbl.pack()

        self.contraseña_text = Entry(self.ventana_reg, width=40)
        self.contraseña_text.pack()

        self.infolbl = Label(self.ventana_reg, text = "", font=self.fuente, bg ='green')
        self.infolbl.pack()

        self.regbtn = Button(self.ventana_reg, text ="Registrarse", command = self.registro)
        self.regbtn.pack()

        self.volverbtn = Button(self.ventana_reg, text = "Volver", command = self.volver)
        self.volverbtn.pack()

    def registro(self):
        nombre= self.usuario_text.get()
        contraseña = self.contraseña_text.get()
        name = self.nombre_text.get()
        if(nombre == ""):
            self.infolbl['text'] = "Ingrese un nombre"
        elif(contraseña == ""):
            self.infolbl['text'] = "Ingrese una contraseña"
        else:
            user = Usuario(name, nombre, contraseña)
            user.Registrar(nombre, contraseña)
            self.infolbl['text'] = "Fue registrado exitosamente"

    def volver(self):
        self.ventana_reg.destroy()
        VentanaInicioSesion()

class VentanaEjecucion:
    def __init__(self):
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
        alto_ventana = 600

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

        botonresultado = Button(self.ventana, text = "Encontrar resultado", command = lambda: self.procesar())
        botonresultado.place(x=200, y=180)

        #self.parte_planta = Entry(self.ventana, width=40)
        #self.parte_planta.place(x=130, y=210)

        self.infolabel = Label(self.ventana, text = "", font = self.fuente2, bg ='green')
        self.infolabel.place(x=60, y= 190)

        self.contadorlabel = Label(self.ventana, text = "Fotos ingresadas: "+ str(self.cont) , font = self.fuente2, bg = 'green')
        self.contadorlabel.place(x=10, y=210)

        self.marco = ttk.Frame(self.ventana, borderwidth=2, relief="raised", padding=(10,10))
        #self.marco.config(width=480,height=320)
        self.marco.place(x=10, y =240)

        self.resultadolbl = Label(self.marco, text="Aquí tendrá un resultado")
        self.resultadolbl.pack()
       
        cerrar = Button(self.ventana, text="Cerrar", command=self.closewindow)
        cerrar.place(x=230,y=560)

    def abrir_archivo(self):
        if(self.cont < 5):
            if(self.lista_desplegable.get() != ""):
                archivo = filedialog.askopenfilename(title="Abrir Archivo", initialdir = "C:/", filetypes = (("Archivos jpg", "*.jpg"), ("Archivos png", "*.png"), ("Archivos jpeg", "*.jpeg")))
                if(archivo != ""):
                    parte= self.lista_desplegable.get()
                    self.reg = Registro()
                    foto = Foto(archivo)
                    self.reg.añadir(foto)
                    listaarchivo.append(archivo)
                    listaparte.append(parte)
                    self.cont = self.cont + 1
                    self.contadorlabel['text'] = "Fotos ingresadas: "+ str(self.cont)
            else:
                self.infolabel['text'] = "Debe ingresar la parte de la planta"
        else:
            self.infolabel['text'] = "No puede ingresar mas fotos"
                    
    def procesar(self):
        if(self.cont == 0):
            self.infolabel['text'] = "No ha ingresado ninguna foto"
        else:
            Proceso.hacer(self.cont)
            res = ("El resultado mas cercano es: "+listanombreplanta[0]+
            "\nNombre cientifico: "+listanombrecientifico[0]+ "\n Porcentaje:" +(str(listapuntaje[0]*100))+
            " %\n\nSegundo resultado: "+listanombreplanta[1]+ "\nNombre cientifico: "+listanombrecientifico[1]+ 
            "\n Porcentaje:" +(str(listapuntaje[1]*100))+" %\n\nTercer resultado: "+listanombreplanta[2]+ 
            "\nNombre cientifico: "+listanombrecientifico[2]+ "\n Porcentaje:" +(str(listapuntaje[2]*100))+" %\n\nCuarto resultado: "
            +listanombreplanta[3]+ "\nNombre cientifico: "+listanombrecientifico[3]+ "\n Porcentaje:" +(str(listapuntaje[3]*100))+
            " %\n\nCuarto resultado: "+listanombreplanta[4]+ "\nNombre cientifico: "+listanombrecientifico[4]+ 
            "\n Porcentaje:" +(str(listapuntaje[4]*100))+" %")
            
            self.reg.resultado = res
            self.resultadolbl['text'] = self.reg.resultado


    def closewindow(self):
        self.ventana.destroy()

Aplicacion = VentanaInicioSesion()
