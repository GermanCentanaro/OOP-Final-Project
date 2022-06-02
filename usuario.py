class Usuario:
    def __init__(self, name, nombre, contraseña):
        self.name = name
        self.nombre = nombre
        self.contraseña = contraseña

    def Iniciar(self, nombre, contraseña):
        archivo = open("usuarios.txt", "r") #abre el archivo usuarios.txt en modo leer para así buscar en el archivo el usuario específico
        linea = archivo.readline() #lee cada linea del archivo
        salir = False
        while(salir == False) and linea != "": #realiza el ciclo hasta que encuentre el usuario o no encuentre nada
            vector = linea.split("\t") #ingresa en un vector y separa por \t que separa el usuario de la contraseña
            if(vector[0] == nombre and vector[1] == contraseña):
                salir = True
            linea = archivo.readline()
        archivo.close() #cierra el archivo
        return salir #retorna un booleano para saber si encontró o no el usuario

    def Registrar(self, nombre, contraseña):
        archivo = open("usuarios.txt", "a") #abre el archivo usuarios.txt en modo escribir después de lo ya escrito

        archivo.write(nombre + "\t" + contraseña +"\t" + "\n") #escribe el nombre y contraseña digitados 
        archivo.close #cierra el archivo
