class Usuario:
    def __init__(self, name, nombre, contraseña):
        self.name = name
        self.nombre = nombre
        self.contraseña = contraseña

    def Iniciar(self, nombre, contraseña):
        archivo = open("usuarios.txt", "r")
        linea = archivo.readline()
        salir = False
        while(salir == False) and linea != "":
            vector = linea.split("\t")
            if(vector[0] == nombre and vector[1] == contraseña):
                salir = True
            linea = archivo.readline()
        archivo.close()
        return salir

    def Registrar(self, nombre, contraseña):
        archivo = open("usuarios.txt", "a")

        archivo.write(nombre + "\t" + contraseña +"\t" + "\n")
        print("\nUsuario ingresado con exito.\n")
        archivo.close
