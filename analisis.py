from PIL import Image
import requests
import json
from pprint import pprint

ruta1 = ("D:/Universidad/SEMESTRE III/Programación Orientada a Objetos/POO/Projecto Final/flower" + ".jpeg")

ruta2 = ("D:/Universidad/SEMESTRE III/Programación Orientada a Objetos/POO/Projecto Final/planta" + ".jpg")
# Cambiar rutas

API_KEY = "2b10M05lpZpn9sMMrQmb8xeLlu" # Set you API_KEY here
api_endpoint = f"https://my-api.plantnet.org/v2/identify/all?api-key={API_KEY}"

image_path_1 = ruta1
image_data_1 = open(image_path_1, 'rb')

image_path_2 = ruta2
image_data_2 = open(image_path_2, 'rb')

data = {
  'organs': ['flower', 'leaf']
}

files = [
  ('images', (image_path_1, image_data_1)),
  ('images', (image_path_2, image_data_2))
]

req = requests.Request('POST', url=api_endpoint, files=files, data=data)
prepared = req.prepare()

s = requests.Session()
response = s.send(prepared)
json_result = json.loads(response.text)

pprint(response.status_code)
pprint(json_result)
