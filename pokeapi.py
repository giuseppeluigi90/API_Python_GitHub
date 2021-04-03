#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def get_pokemons(url='https://pokeapi.co/api/v2/pokemon/', offset=0):
	args = {'offset': offset} if offset else {} 

	response = requests.get(url, params=args) 

	print(response.url)
	print("--------------------------------")

	if response.status_code == 200:

		payload = response.json()
		results = payload.get('results', [])

		if results:
			for pokemon in results:
				name = pokemon['name']
				print(name)

		siguiente = raw_input("¿Continuar listado? [Y/N]").lower()

		if siguiente == "y":
			get_pokemons(offset=offset+20)


if __name__ == '__main__':
	url = 'https://pokeapi.co/api/v2/pokemonform/'
	get_pokemons()


	