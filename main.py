import requests
import json

if __name__ == '__main__':
	url = 'http://httpbin.org/get'
	args = {'nombre': 'Giuseppe', 'edad':'30'}

	response = requests.get(url, params=args)

	print(response.url)
	# print(response)
	
	if response.status_code == 200:
		"""
		response_json = response.json() # Diccionario
		origin = response_json['origin']
		print(origin)
		# content = response.content
		# print(content)
		"""

		response_json = json.loads(response.text)
		origin = response_json['origin']
		print(origin)

		# file = open('google.html', 'wb')
		# file.write(content)
		# file.close()

	


	