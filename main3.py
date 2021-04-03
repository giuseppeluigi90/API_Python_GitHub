import requests
import json

if __name__ == '__main__':
	url = 'http://httpbin.org/put'
	payload = {'nombre': 'Giuseppe', 'edad':'30', 'ano':'2021'}
	headers = {'content-Type':'application/json', 'access-token':'12345'}

	response = requests.put(url, json=payload, headers=headers)
	print(response.url)

	if response.status_code == 200:
		# print(response.content)
		headers_response = response.headers # Diccionario
		server = headers_response['Server']
		print(server)
	
		"""
		GET ----	Obtener o consultar
		POST ---	Crear o insertar
		PUT ----	Modificar o Actualizar
		DELETE --	Remover o eliminar
		"""

	