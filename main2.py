import requests
import json

if __name__ == '__main__':
	url = 'http://httpbin.org/post'
	payload = {'nombre': 'Giuseppe', 'edad':'30', 'ano':'2021'}
	headers = {'content-Type':'application/json', 'access-token':'12345'}

	response = requests.post(url, json=payload, headers=headers)

	if response.status_code == 200:
		# print(response.content)
		headers_response = response.headers # Diccionario
		server = headers_response['Server']
		print(server)
	


	