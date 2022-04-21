class Planta:
    def __init__(self, color_petalo, largo_petalo, color_tallo, largo_tallo, color, nombre_planta, color_hojas, fruto):
        self.color_petalo = color_petalo
        self.largo_petalo = largo_petalo
        self.color_tallo = color_tallo
        self.largo_tallo = largo_tallo
        self.color = color
        self.nombre_planta = nombre_planta
        self.color_hojas = color_hojas
        self.fruto = fruto
    
    def describir():
        pass
    #hacer un imprimir

class Usuario:
    def Ingresar():
        pass

class Foto:
    def ingresar():
        pass

    def cancelar():
        pass

class Programa:
    def __init__():
        pass

class Historial:
    def __init__(self, nombre_planta, list_fotos):
        self.nombre_planta = nombre_planta
        self.fotos = list_fotos
	
import requests
import json
from pprint import pprint
import numpy as np

from PIL import Image
from io import BytesIO

link = []

print("Ingresar el número de fotos que introduciran:")
nfotos = int(input())
for i in range(0, nfotos):
    print("Introduzca el link de la foto:")
    link.append(input())

API_KEY = "2b10M05lpZpn9sMMrQmb8xeLlu"
api_endpoint = f"https://my-api.plantnet.org/v2/identify/all?api-key={API_KEY}"

if (nfotos == 1):
    image_path_1 = link[0]
    response = requests.get(image_path_1)
    image_data_1 = Image.open(BytesIO(response.content))


    files = [
		('images', (image_path_1, image_data_1))
    ]

elif (nfotos == 2):
    image_path_1 = link[0]
    image_data_1 = open(image_path_1, 'rb')
    
    image_path_2 = link[1]
    image_data_2 = open(image_path_2, 'rb')

    files = [
		('images', (image_path_1, image_data_1)),
		('images', (image_path_2, image_data_2)) 
    ]


elif (nfotos == 3):
    image_path_1 = link[0]
    image_data_1 = open(image_path_1, 'rb')
    
    image_path_2 = link[1]
    image_data_2 = open(image_path_2, 'rb')
    
    image_path_3 = link[2]
    image_data_3 = open(image_path_2, 'rb')

    files = [
		('images', (image_path_1, image_data_1)),
		('images', (image_path_2, image_data_2)),
        ('images', (image_path_3, image_data_3))
    ]

elif (nfotos == 4):
    image_path_1 = link[0]
    image_data_1 = open(image_path_1, 'rb')
    
    image_path_2 = link[1]
    image_data_2 = open(image_path_2, 'rb')
    
    image_path_3 = link[2]
    image_data_3 = open(image_path_2, 'rb')
    
    image_path_4 = link[3]
    image_data_4 = open(image_path_2, 'rb')

    files = [
		('images', (image_path_1, image_data_1)),
		('images', (image_path_2, image_data_2)),
        ('images', (image_path_3, image_data_3)),
        ('images', (image_path_4, image_data_4))
    ]
    
elif (nfotos == 5):
    image_path_1 = link[0]
    image_data_1 = open(image_path_1, 'rb')
    
    image_path_2 = link[1]
    image_data_2 = open(image_path_2, 'rb')
    
    image_path_3 = link[2]
    image_data_3 = open(image_path_2, 'rb')
    
    image_path_4 = link[3]
    image_data_4 = open(image_path_2, 'rb')
    
    image_path_5 = link[4]
    image_data_5 = open(image_path_2, 'rb')

    files = [
		('images', (image_path_1, image_data_1)),
		('images', (image_path_2, image_data_2)),
        ('images', (image_path_3, image_data_3)),
        ('images', (image_path_4, image_data_4)),
        ('images', (image_path_5, image_data_5))
    ]

data = {
	'organs': ['flower', 'leaf']
}

req = requests.Request('POST', url=api_endpoint, files=files, data=data)
prepared = req.prepare()

s = requests.Session()
response = s.send(prepared)
json_result = json.loads(response.text)

pprint(response.status_code)
pprint(json_result)
