from PIL import Image
from pprint import pprint
from listas import *

class Registro():
  def __init__(self):
    self.__resultado = None
    self.__fotoI = None
    self.__fotoU = None
    
  @property
  def resultado(self):
    return self.__resultado
		
  @resultado.setter
  def resultado(self, texto):
    self.__resultado = texto
    
  def añadir(self, foto):
    if (self.__fotoI == None):
      self.__fotoI = foto
      self.__fotoU = foto
    else:
      self.__fotoU.next = foto
      self.__fotoU = foto

  def mostrarFotos(self):
    foto = self.__fotoI
    while (foto != None):
      foto.mostrar()
      foto = foto.next

  def __str__(self):
    return "RESULTADO: \n" + self.__resultado

class Foto():
  def __init__(self, tlink):
    self.__ruta = tlink
    self.__next = None
    self.__data = open(tlink, 'rb')
	
  @property
  def ruta(self):
    return self.__ruta
		
  @ruta.setter
  def ruta(self, texto):
    self.__ruta = texto
    
  @property
  def next(self):
    return self.__next
    
  @next.setter
  def next(self, nueva_foto):
    self.__next = nueva_foto
  
  @property
  def data(self):
    return self.__data

  def mostrar(self):
    im = Image.open(self.__ruta)
    im.show()
	
  def __str__(self):
    return "Link: " + str(self.__ruta) + " - Data: " + str(self.__data)
