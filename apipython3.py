#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

if __name__ == '__main__':

	client_id = 'a3c5228f989faca0eccb'
	client_secret = 'def2bcdde7aa19f45ccd196d31df171f3235e544'
	code = '79bb951cefc1b0621210'

	a_token_test = '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'

	url = 'https://api.github.com/user/repos'
	payload = {'name':'API_Python_GitHub'}
	headers = {'Accept':'application/json', 'Authorization':'token ' + a_token_test  }

	response = requests.post(url, headers=headers, json=payload)

	if response.status_code == 200:
		response_json = response.json()
		name = response_json['name']
		full_name = response_json['full_name']
		print("************************************")
		print(name)
		print(full_name)
	else:
		print("Error - No se ha creado Repositorio:")
		print("*******************************")
		# print(response.content)

	# https://github.com/login/oauth/authorize?client_id=a3c5228f989faca0eccb&scope=repo


