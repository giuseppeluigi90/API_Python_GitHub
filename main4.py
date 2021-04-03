import requests
import json

if __name__ == '__main__':
	url = 'https://www.youtube.com/watch?v=7qrlCLbGigc&list=RD7qrlCLbGigc&start_radio=1'

	response = requests.get(url, stream=True) # Realiza la peticion sin cerrar la conexion
	with open('image.jpg', 'wb') as file:
		for chunk in response.iter_content(): # Descarga el contenido poco a poco
			file.write(chunk) 

	response.close()


	