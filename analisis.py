from PIL import Image
import requests
import json
from pprint import pprint
from listas import *
from german import *

class Proceso:
  def hacer(num_fotos):
    API_KEY = "2b10M05lpZpn9sMMrQmb8xeLlu" # Set you API_KEY here
    api_endpoint = f"https://my-api.plantnet.org/v2/identify/all?api-key={API_KEY}"
    
    if(num_fotos == 1):
      ruta1 = listaarchivo[0]
      image_path_1 = ruta1
      image_data_1 = open(image_path_1, 'rb')
      
      data = {
        'organs': []
      }
      
      files = [
        ('images', (image_path_1, image_data_1))
      ]
    
    elif(num_fotos == 2):
      ruta1 = listaarchivo[0]
      ruta2 = listaarchivo[1]

      image_path_1 = ruta1
      image_data_1 = open(image_path_1, 'rb')

      image_path_2 = ruta2
      image_data_2 = open(image_path_2, 'rb')

      data = {
        'organs': []
      }

      files = [
        ('images', (image_path_1, image_data_1)),
        ('images', (image_path_2, image_data_2))
      ]
    elif(num_fotos == 3):
      ruta1 = listaarchivo[0]
      ruta2 = listaarchivo[1]
      ruta3 = listaarchivo[2]

      image_path_1 = ruta1
      image_data_1 = open(image_path_1, 'rb')

      image_path_2 = ruta2
      image_data_2 = open(image_path_2, 'rb')

      image_path_3 = ruta3
      image_data_3 = open(image_path_3, 'rb')

      data = {
        'organs': []
      }

      files = [
        ('images', (image_path_1, image_data_1)),
        ('images', (image_path_2, image_data_2)),
        ('images', (image_path_3, image_data_3))
      ]
    elif(num_fotos == 4):
      ruta1 = listaarchivo[0]
      ruta2 = listaarchivo[1]
      ruta3 = listaarchivo[2]
      ruta4 = listaarchivo[3]

      image_path_1 = ruta1
      image_data_1 = open(image_path_1, 'rb')

      image_path_2 = ruta2
      image_data_2 = open(image_path_2, 'rb')

      image_path_3 = ruta3
      image_data_3 = open(image_path_3, 'rb')

      image_path_4 = ruta4
      image_data_4 = open(image_path_4, 'rb')

      data = {
        'organs': []
      }

      files = [
        ('images', (image_path_1, image_data_1)),
        ('images', (image_path_2, image_data_2)),
        ('images', (image_path_3, image_data_3)),
        ('images', (image_path_4, image_data_4))
      ]
    elif(num_fotos == 5):
      ruta1 = listaarchivo[0]
      ruta2 = listaarchivo[1]
      ruta3 = listaarchivo[2]
      ruta4 = listaarchivo[3]
      ruta5 = listaarchivo[4]

      image_path_1 = ruta1
      image_data_1 = open(image_path_1, 'rb')

      image_path_2 = ruta2
      image_data_2 = open(image_path_2, 'rb')

      image_path_3 = ruta3
      image_data_3 = open(image_path_3, 'rb')

      image_path_4 = ruta4
      image_data_4 = open(image_path_4, 'rb')

      image_path_5 = ruta5
      image_data_5 = open(image_path_5, 'rb')

      data = {
        'organs': []
      }

      files = [
        ('images', (image_path_1, image_data_1)),
        ('images', (image_path_2, image_data_2)),
        ('images', (image_path_3, image_data_3)),
        ('images', (image_path_4, image_data_4)),
        ('images', (image_path_5, image_data_5))
      ]

    req = requests.Request('POST', url=api_endpoint, files=files, data=data)
    prepared = req.prepare()

    s = requests.Session()
    response = s.send(prepared)
    json_result = json.loads(response.text)
    

    pprint(response.status_code)
    pprint(json_result)

    for each in json_result['results']:
      if(len(each['species']['commonNames']) == 0):
        listanombreplanta.append("Nombre no identificado")
      else:
        listanombreplanta.append(each['species']['commonNames'][0])

      listanombrecientifico.append(each['species']['scientificName'])
      listapuntaje.append(each['score'])

    print(listanombreplanta)
    print(listanombrecientifico)
    print(listapuntaje)
    #pprint(species)
